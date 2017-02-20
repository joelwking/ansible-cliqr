#!/bin/bash
#
#  atc.sh
#
#    Copyright (c) 2017 World Wide Technology, Inc.
#    All rights reserved.
#    author: Joel W. King, World Wide Technology
#    Revision history:
#      - 17 February 2017  | 1.1  | Initial 
#      - 20 February 2017  | 1.2  | When running under CliQr, install some dependancies 
#
echo "CloudCenter_EXTERNAL_SERVICE_LOG_MSG_START"
echo $0 $1
#
#
#
if [ -f /etc/lsb-release ]; then
    echo "Assume running in Ubuntu development environment"
else 
    echo "Assume running in CliQr production environment"
    yum install git -y
    easy_install requests
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

/usr/bin/python2.7 ./ansible-cliqr/ATC.py

echo "CloudCenter_EXTERNAL_SERVICE_LOG_MSG_END"