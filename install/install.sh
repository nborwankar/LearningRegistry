#!/bin/bash
apt-get install python-pip
apt-get install nginx
pip install pylons
pip install flup
pip install --upgrade couchdb 
cp nginx.conf /etc/nginx/nginx.conf
