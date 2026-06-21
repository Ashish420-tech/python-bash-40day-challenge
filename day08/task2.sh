#!/bin/bash

read -p "Enter filename" file

if [ -f "$file" ]
then
  echo "Exists"
else
  echo "Not exists"
fi
