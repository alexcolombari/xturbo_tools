#!/bin/bash

export TERM=linux

trap '' 2
pyxtermjs --host 192.168.172.50 -p 5000 --command python3 --cmd-args /root/tools/main.py
trap 2