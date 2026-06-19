#!/bin/bash

echo "=============================="
echo " SYSTEM REPORT"
echo "=============================="

echo " Hostname:"
 hostname
echo "Current user:$USER"


echo "IP Address:"
hostname -I

echo "Kernel Version:$(uname -r)"

echo "Disk usage:"
df -h
echo "Memory Usage:"
free -h

echo "Uptime:"
uptime

echo "====================================="
