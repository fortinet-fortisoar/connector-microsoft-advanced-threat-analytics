"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from requests_ntlm import HttpNtlmAuth
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('microsoft-advanced-threat-analytics')


def make_api_call(method="GET", endpoint="", config=None, params=None, data=None, json_data=None):
    try:
        headers = {
            "Content-Type": "application/json"
        }
        server_url = config.get('url').strip('/')
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://" + server_url
        server_url = server_url + '/api/management' + endpoint
        response = requests.request(method=method, url=server_url,
                                    auth=HttpNtlmAuth(config.get('username'), config.get('password')),
                                    headers=headers, data=data, json=json_data, params=params,
                                    verify=config.get('verify_ssl'))
        if response.ok:
            return response.json()
        else:
            if response.text != "":
                err_resp = response.json()
                failure_msg = err_resp.get('errors')
                error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason,
                                                                     failure_msg if failure_msg else '')
            else:
                error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
            logger.error(error_msg)
            raise ConnectorError(error_msg)
    except requests.exceptions.SSLError:
        logger.error('An SSL error occurred')
        raise ConnectorError('An SSL error occurred')
    except requests.exceptions.ConnectionError:
        logger.error('A connection error occurred')
        raise ConnectorError('A connection error occurred')
    except requests.exceptions.Timeout:
        logger.error('The request timed out')
        raise ConnectorError('The request timed out')
    except requests.exceptions.RequestException:
        logger.error('There was an error while handling the request')
        raise ConnectorError('There was an error while handling the request')
    except Exception as err:
        raise ConnectorError(str(err))


def get_suspicious_activities_list(config, params):
    endpoint = "/suspiciousActivities/{suspicious_activity_id}".format(suspicious_activity_id=params.get('activity_id'))
    return make_api_call(endpoint=endpoint, config=config)


def set_suspicious_activity_status(config, params):
    body = {
        'Status': params.get('status')
    }
    endpoint = "/suspiciousActivities/{suspicious_activity_id}".format(suspicious_activity_id=params.get('activity_id'))
    return make_api_call(method='POST', endpoint=endpoint, config=config, json_data=body)


def get_monitoring_alerts_list(config, params):
    endpoint = "/monitoringAlerts"
    return make_api_call(endpoint=endpoint, config=config)


def get_entity(config, params):
    endpoint = "/uniqueEntities/{entity_id}".format(entity_id=params.get('entity_id'))
    return make_api_call(endpoint=endpoint, config=config, params=params)


def _check_health(config):
    try:
        get_monitoring_alerts_list(config, params={})
        return True
    except Exception as e:
        logger.error("Invalid Credentials: %s" % str(e))
        raise ConnectorError("Invalid Credentials")


operations = {
    'get_suspicious_activities_list': get_suspicious_activities_list,
    'set_suspicious_activity_status': set_suspicious_activity_status,
    'get_monitoring_alerts_list': get_monitoring_alerts_list,
    'get_entity': get_entity
}
