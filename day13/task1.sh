#!/bin/bash

servers=("web1" "web2" "db01")

for server in "${servers[@]}"
do 
  echo "$server"
done
