#!/bin/bash

echo "=============================="
echo "System Health Report"
echo "=============================="

echo "Date:"
date

echo

echo "Hostname:"
hostname

echo

echo "Current User:"
whoami

echo

echo "Disk Usage:"
df -h

echo

echo "Memory:"
free -h

echo

echo "Uptime:"
uptime
