#!/bin/bash
#
#  atc.sh
#
#
echo $0 $1

if [ $# -gt 1 ]; then
    echo usage: atc -r
    echo 
    echo     -r     optional, runs the program after setup
    exit 1
fi

#  We assume that "git clone https://github.com/joelwking/ansible-cliqr" has been executed
curl -o $HOME/ansible-cliqr/phantom/ansible_tower_connector.py https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/ansible_tower/ansible_tower_connector.py

echo "Input environmental variables"
echo 
echo $TOWER_INSTANCE $USERNAME $PASSWORD
echo "Job Template ID:  " $JOB_TEMPLATE_ID
echo "Dead Interval:    " $DEAD_INTERVAL
echo "Extra vars:       " $EXTRA_VARS
echo "Debug level:      " $DEBUG_LEVEL

if [ "$1" == "-r" ]; then
    /usr/bin/python2.7 $HOME/ansible-cliqr/ATC.py
fi
