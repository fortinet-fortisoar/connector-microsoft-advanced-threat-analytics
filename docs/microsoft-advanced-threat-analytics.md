## About the connector
Microsoft Advanced Threat Analytics (ATA) is an on-premises platform that helps protect your enterprise from multiple types of advanced targeted cyber attacks and insider threats.
<p>This document provides information about the Microsoft Advanced Threat Analytics Connector, which facilitates automated interactions, with a Microsoft Advanced Threat Analytics server using FortiSOAR&trade; playbooks. Add the Microsoft Advanced Threat Analytics Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Microsoft Advanced Threat Analytics.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-microsoft-advanced-threat-analytics</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Microsoft Advanced Threat Analytics server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Microsoft Advanced Threat Analytics server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Microsoft Advanced Threat Analytics</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Microsoft Advanced Threat Analytics server URL to connect and perform the automated operations.
</td>
</tr><tr><td>Username</td><td>Specify the Microsoft Advanced Threat Analytics username to connect and perform the automated operations.
</td>
</tr><tr><td>Password</td><td>Specify the Microsoft Advanced Threat Analytics password to connect and perform the automated operations..
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Suspicious Activities List</td><td>Retrieves the suspicious activities by the activity ID, status, severity from Microsoft Advanced Threat Analytics.</td><td>get_suspicious_activities_list <br/>Investigation</td></tr>
<tr><td>Set Suspicious Activity Status</td><td>Sets status of suspicious activity by the activity ID, status in Microsoft Advanced Threat Analytics.</td><td>set_suspicious_activity_status <br/>Investigation</td></tr>
<tr><td>Get Monitoring Alerts List</td><td>Retrieves the monitoring alerts from Microsoft Advanced Threat Analytics.</td><td>get_monitoring_alerts_list <br/>Investigation</td></tr>
<tr><td>Get Entity</td><td>Retrieves the information of specific entity from Microsoft Advanced Threat Analytics.</td><td>get_entity <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Suspicious Activities List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Suspicious Activity ID</td><td>Specify the ID of the suspicious activity to retrieve.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Set Suspicious Activity Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Suspicious Activity ID</td><td>Specify the ID of the suspicious activity whose status needs to be updated.
</td></tr><tr><td>Status</td><td>Specify the status of the suspicious activity. e.g., Open, Closed, Suppressed
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Monitoring Alerts List
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Entity
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Entity ID</td><td>Specify the ID of the entity to retrieve from Microsoft Advanced Threat Analytics.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - microsoft-advanced-threat-analytics - 1.0.0` playbook collection comes bundled with the Microsoft Advanced Threat Analytics connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Microsoft Advanced Threat Analytics connector.

- Get Entity
- Get Monitoring Alerts List
- Get Suspicious Activities List
- Set Suspicious Activity Status

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
