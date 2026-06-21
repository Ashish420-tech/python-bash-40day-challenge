#!/bin/bash

str="$1"
reverse=""

for ((i=${#str}-1;i>=0;i--));do
     reverse="${reverse}${str:$i:1}"
done

echo "$reverse"
