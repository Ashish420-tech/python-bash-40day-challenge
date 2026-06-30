#!/bin/bash

echo "Hostname : $(hostname)"
echo "Uptime :"
uptime

echo

echo "Memory"
free -h

echo

echo "Disk"
df -h

echo

echo "CPU"

top -bn1 | head -5
