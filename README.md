# Ansible Tower and Cisco Cloud Center (CliQr) modules
This code emulates the framework of Phantom Cyber, enabling code reuse, without modification, of the Ansible Tower app for Phantom. For additional information on this app, refer to these links:

> [Phantom app: Ansible Tower](http://www.slideshare.net/joelwking/phantom-app-ansible-tower)

> [Data Exfiltration Monitoring with Phantom, Ansible, and Cisco ACI](https://blog.phantom.us/2016/08/22/data-exfiltration-monitoring-with-phantom-ansible-and-cisco-aci/)

## Reference material
This use case was presented on the 13th July 2017 at the Ansible Durham meetup.
> [Slides](https://www.slideshare.net/joelwking/integrating-ansible-tower-with-security-orchestration-and-cloud-management)

> [Integrating Ansible Tower with security orchestration and cloud management](https://www.meetup.com/Ansible-Durham/events/240765174/)

## Initiating Ansible Tower Jobs from Cloud Center
See the documentation on [External Services] (http://docs.cloudcenter.cisco.com/display/CCD46/External+Service)

### Environmental variables
The program uses environmental variables as input. Set them from Cloud Center. We need the IP address or host name of the Ansible Tower instance, along with the job template ID to execute (it can be either the numeric value or the text name) and optionally any extra variables needed to launch the job. The extra vars are key, value pairs separated by a comma. Extra vars is optional. If you specify extra vars, the Ansible Tower template must have the `prompt on launch` box checked.
```
export TOWER_INSTANCE=ansible-tower.sandbox.wwtatc.local
export USERNAME=admin
export PASSWORD=redacted
export JOB_TEMPLATE_ID=32
export EXTRA_VARS="name=dropzone_192.0.2.1,dstIp=192.0.2.1,fvTenant=mediaWIKI,ap=test_mediaWIKI,epg=Outside,srcPort=https,prot=tcp"
```
Here is another example, now using the name of the job template and specifying the dead interval, and removing the previously specified extra vars
```
export JOB_TEMPLATE_ID=f5_check
export DEAD_INTERVAL=10
export -n EXTRA_VARS
```
### Download
`curl https://raw.githubusercontent.com/joelwking/ansible-cliqr/master/atc.sh -o atc.sh`
### Run the program
` /bin/bash ./atc.sh`

## cliqr_gather_facts
This module was written to experiment with the CliQr API to return facts to an Ansible playbook.
