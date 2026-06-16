#!/bin/bash

count=0

while (( count <= 20)) 
do
  if (( count %2 == 0))
  then
     echo "$count"
  fi
  ((count++))
done 
