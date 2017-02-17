#!/usr/bin/env python
#
"""
ATC.py

  Ansible Tower Connector


    References:
         https://github.com/datacenter/cloudcenter-content/tree/master/other/ansible-tower

    Directory Structure:

        $HOME/ATC.py

        $HOME/phantom/__init__.py                    #  touch this file, http://stackoverflow.com/questions/448271/what-is-init-py-for
        $HOME/phantom/app.pyc                        #  import phantom.app as phantom
        $HOME/phantom/action_result.pyc              #  from phantom.action_result import ActionResult
        $HOME/phantom/base_connector.pyc             #  from phantom.base_connector import BaseConnector

        $HOME/phantom/ansible_tower_connector.pyc    #  Original Ansible Phantom Tower code from GitHub
                                                     #  https://github.com/joelwking/Phantom-Cyber/blob/master/ansible_tower/

    Configuration Variables:
        export TOWER_INSTANCE=ansible-tower.sandbox.wwtatc.local
        export USERNAME=admin
        export PASSWORD=redacted

    Parameters:
        export DEBUG_LEVEL=5                         # Debug greater than 3, we generate more output NOT IMPLEMENTED!!
        export JOB_TEMPLATE_ID=32
        export DEAD_INTERVAL=10
        export EXTRA_VARS="name=dropzone_192.0.2.1,dstIp=192.0.2.1,fvTenant=mediaWIKI,ap=test_mediaWIKI,epg=Outside,srcPort=https,prot=tcp"

        The minimum you need is the job template number of name, example follows
        export JOB_TEMPLATE_ID=f5_check
        export -n DEAD_INTERVAL
        export -n EXTRA_VARS
        export -n DEBUG_LEVEL


"""
#
import phantom.ansible_tower_connector as ansible_tower_connector
import os
import json
import string
#
def main():
    #  Format of the JSON file Phantom uses for an ap
    in_json = {"app_config": None, 
               "asset_id": "22", 
               "config": {"tower_instance": "10.255.40.23", "username": "admin", "password": "redacted"},
               "debug_level": 3,
               "identifier": "run job",
               "parameters": 
                        [
                           {
                             "dead interval": 10,
                             "job template id": "32",
                             "extra vars": "name=dropzone_192.0.2.1,dstIp=192.0.2.1,fvTenant=mediaWIKI,ap=test_mediaWIKI,epg=Outside,srcPort=https,prot=tcp"
                           }
                       ]
                }


    # Process parameters
    for key in in_json["parameters"][0].keys():
        value = os.environ.get(string.replace(key, " ", "_").upper())
        if value:                                          # retuns a value of of None if it doesn't exist
            in_json["parameters"][0][key] = value
        else:
            del in_json["parameters"][0][key]     

    # Configuration variables
    in_json["config"]["tower_instance"] = os.environ.get('tower_instance'.upper())
    in_json["config"]["username"] = os.environ.get('username'.upper())
    in_json["config"]["password"] = os.environ.get('password'.upper())

    if os.environ.get('debug_level'.upper()):
        try: 
            in_json["debug_level"] = int(os.environ.get('debug_level'.upper()))
        except ValueError:
            pass

    # Run the Phantom Cyber code
    connector = ansible_tower_connector.Tower_Connector()
    ret_val = connector._handle_action(json.dumps(in_json), None)

if __name__ == '__main__':
    
    main()
    exit(0)