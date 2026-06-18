#!/bin/bash

read -p "Enter filename:" file

if [ -w "$file" ]
then
   echo " File is writable"
else
   echo "File is not writable"
fi

