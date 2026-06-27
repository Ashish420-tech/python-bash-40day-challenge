#!/bin/bash

services=("nginx" "ssh" "cron")

for service in "${services[@]}"
do
systemctl status "$service" >/dev/null 2>&1

if [ $? -eq 0 ]
then
echo "$service Running"
else
echo "$service Not Running"
fi
done
