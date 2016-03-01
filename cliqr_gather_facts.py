#!/usr/bin/env python

"""
     Copyright (c) 2016 World Wide Technology, Inc. 
     All rights reserved. 

     Revision history:
     1 March 2016  |  1.0 - initial release
     
"""

DOCUMENTATION = '''
---
module: cliqr_gather_facts
author: Joel W. King, World Wide Technology
version_added: "1.0"
short_description: Query the CliQr CCO and return facts.
description: Ansible module to query the CliQr CCO and return facts.
 

references:
    - The API documentation is at docs.cliqr.com

requirements:
    - none

options:
    host:
        description:
            - The IP address or hostname of the CCO
        required: true

    username:
        description:
            - Login username
        required: true

    api_key:
        description:
            - API access key for the username specified 
        required: true

    uri:
        description:
            - URI to query
        required: true

    debug:
        description:
            - debug switch
        required: false


'''

EXAMPLES = '''


    ansible localhost -m cliqr_gather_facts.py -a "username=netdeploy_5 api_key=redacted host=10.255.138.241 uri=/v1/aclResources"


    - name: Query a URL on CliQr
      cliqr_gather_facts:
        username: netdeploy_5
        host: 10.255.138.241
        uri: /v1/jobs/
        api_key: "{{api_key}}"

    - name: print out variables
      debug: msg=" {{item.name}} {{item.id}} {{item.displayName}} "
      with_items: jobs

'''

import sys
import time
import json
import requests

# ---------------------------------------------------------------------------
# CliQr Connection Class
# ---------------------------------------------------------------------------

class Connection(object):
    """
      Connection class for Python to CliQr API
    """

    def __init__(self, controllername, username, password):                               
        self.transport = "https://"
        self.controllername = controllername
        self.username = username
        self.password = password
        self.HEADER = {"Accept":"application/json", "Content-Type": "application/json"}
        return

    def genericGET(self, URL):
        """
          Issue a GET and return the results
        """
        URL = "%s%s%s" % (self.transport, self.controllername, URL)

        try:
            r = requests.get(URL, auth=(self.username, self.password), headers=self.HEADER, verify=False)
        except requests.ConnectionError as e:
            return (False, e)
        content = json.loads(r.content)
        return (r.status_code, content)

# ---------------------------------------------------------------------------
# MAIN program and functions
# ---------------------------------------------------------------------------

def query_cliqr_api(cntrl, uri):
    """ 
        Query the CCO using the URI specified and return the results as facts
    """
    result = { 'ansible_facts': {} }                 
    status, response = cntrl.genericGET(uri)
    result["ansible_facts"] = response
    return status, result

def main():
    "   "
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True),
            username=dict(required=True),
            api_key=dict(required=True),
            uri=dict(required=True),
            debug = dict(required=False, default=False, choices=BOOLEANS)
         ),
        check_invalid_arguments=False,
        add_file_common_args=True
    )

    cntrl = Connection(module.params["host"], module.params["username"], module.params["api_key"])
    code, response = query_cliqr_api(cntrl, module.params["uri"])
    if code == 200:
        module.exit_json(**response)
    else:
        module.fail_json(msg="status_code= %s" % code)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
