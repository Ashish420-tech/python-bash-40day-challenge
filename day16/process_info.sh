#!/bin/bash

ps


ps -ef


ps -u $USER


echo "Current User: $USER"

echo "Current Date: $(date)"

echo "Running Processes"

ps -ef | head
