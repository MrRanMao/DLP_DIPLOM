#!/bin/bash

mkdir -p $PWD/logs
#mitmdump --listen-port 9999 --set confdir=./certs --set keep_host_header --ssl-insecure -s proxy_addons.py >> $PWD/logs/proxy-$(date +"%d-%m-%Y-%H%M%S").log
mitmdump --listen-port 9999 --set confdir=./certs --set keep_host_header --ssl-insecure -s proxy_addons.py

