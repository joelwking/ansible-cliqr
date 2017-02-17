#!/bin/bash
#
#  atc.sh
#
#    Copyright (c) 2017 World Wide Technology, Inc.
#    All rights reserved.
#    author: Joel W. King, World Wide Technology
#    Revision history:
#      - 17 February 2017  | 1.0  | Initial release
#
#
echo "CloudCenter_EXTERNAL_SERVICE_LOG_MSG_START"
echo $0 $1

if [ $# -gt 1 ]; then
    echo usage: atc -r
    echo 
    echo     -r     optional, runs the program after setup
    exit 1
fi

git clone https://github.com/joelwking/ansible-cliqr

# Download the Phantom app into the repository
curl -o ./ansible-cliqr/phantom/ansible_tower_connector.py https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/ansible_tower/ansible_tower_connector.py

echo "Input environmental variables"
echo 
echo "Tower credentials:" $TOWER_INSTANCE $USERNAME $PASSWORD
echo "Job Template ID:  " $JOB_TEMPLATE_ID
echo "Dead Interval:    " $DEAD_INTERVAL
echo "Extra vars:       " $EXTRA_VARS
echo "Debug level:      " $DEBUG_LEVEL

if [ "$1" == "-r" ]; then
    /usr/bin/python2.7 ./ansible-cliqr/ATC.py
fi

echo "CloudCenter_EXTERNAL_SERVICE_LOG_MSG_END"