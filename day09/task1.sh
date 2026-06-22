#!/bin/bash

ps

top

pgrep bash

PID=$1

kill $PID

sudo systemctl status ssh


sudo systemctl restart ssh

ps -e| wc -l

free -h

lscpu


echo "========System Report================"


echo "Hostname"
hostname

echo

echo "Memory:"

free -h

echo

echo "CPU:"

lscpu|grep "model name:"

echo

echo "Running Process:"

ps -e|wc -l


