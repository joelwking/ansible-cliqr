#!/usr/bin/env python
# action_result.py
#
"""
     Copyright (c) 2017 World Wide Technology, Inc.
     All rights reserved.

     author: Joel W. King, World Wide Technology

     Revision history:

       - 16 February 2017  | 1.0  | Initial release

"""

class ActionResult(object):

    def __init__(self, param):
        " param is a dictionary of parameters"
        self.param = param
        print "ActionResult __init__"

    def set_status(self, status_state):
        print "ActionResult set_status %s" % status_state
        return

    def add_data(self, a_dictionary):
        print "ActionResult add_data %s" % a_dictionary
        return
