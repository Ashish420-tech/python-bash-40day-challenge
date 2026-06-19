#!/bin/bash


servers=("web01" "web02" "db01")

for server in "${servers[@]}"
do
   echo $server
done
