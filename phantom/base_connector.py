#!/usr/bin/env python
# base_connector.py
#
"""
     Copyright (c) 2017 World Wide Technology, Inc.
     All rights reserved.

     author: Joel W. King, World Wide Technology

     Revision history:

       - 16 February 2017  | 1.0  | Initial release

"""
import json

class BaseConnector(object):
    """ This mimics the BaseConnector from Phantom Cyber. See the documentation
      on your Phantom instance at https://phantom.example.net/docs/appdev/overview"""

    def __init__(self):

        self.print_progress_message = None
        self.json_data = None                                   # Data from a ./test_jsons file
        self.status_state = None

    def _handle_action(self, input_data, unknown):
        "You call handle_action for every param dictionary in the parameter list"
        print "BaseConnector _handle_action"
        self.json_data = json.loads(input_data)
        
        for item in self.json_data["parameters"]:          # call for every param dictionary in the parameter list.

            if self.initialize():
               something_returned =  self.handle_action(self.remove_unicode(item))

            self.finalize()
        return

    def remove_unicode(self,item):
        "Ansible Tower doesn't tollerate unicode in the extra_vars JSON string"
        string_type = {}
        for key, value in item.items():
            if isinstance(key, unicode):
                key = key.encode('utf8')
            if isinstance(value, unicode):
                value = value.encode('utf8')
            string_type[key] = value
        return string_type

    def get_config(self):
        return self.json_data["config"]

    def add_action_result(self, action_result):
        "Input is the action result object"
        print "BaseConnector add_action_result"
        return

    def set_status_save_progress(self, status_state, status_message=""):
        self.status_state = status_state
        print "BaseConnector set_status_save_progress %s" % status_message
        return

    def send_progress(self, status):
        print "BaseConnector send_progress %s" % status
        return

    def debug_print(self, message):
        print "BaseConnector debug_print %s" % message
        return

    def get_action_identifier(self):
        return self.json_data["identifier"]

    def get_status(self):    
        return self.status_state