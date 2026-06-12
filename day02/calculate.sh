#!/bin/bash

apache_logs=150
nginx_logs=250

total=$((apache_logs + nginx_logs))

echo "Total Logs: $total"
