#!/bin/bash

read -p "Enter filename" file

if [ -f "$file" ]
then
   echo  "It is a regular file."
else
   echo "It is not a regular file."
fi
