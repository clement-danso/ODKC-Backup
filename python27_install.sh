ls#!/bin/bash

#########################################
# Installing python and necessary packages
# locally. This script will install python
# into the ~/local/bin directory and install the following packages
#requests==2.26.0
#urllib3==1.26.7
#########################################

# installing python 2.7.3
sudo apt update
sudo apt install -y python2

# installing pip
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py


# installing requests
pip install requests
pip freeze
