#!/bin/bash

system_info(){

echo "Hostname: $(hostname)"
echo "Date: $(date)"

echo

echo "Disk Usage"

df -h

echo

echo "Memory"

free -h

echo

echo "CPU Load"

uptime

}

system_info
