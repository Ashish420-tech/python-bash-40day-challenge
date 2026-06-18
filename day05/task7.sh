#!/bin/bash

read -p "Enter filename: " file

if [ -s "$file" ]
then
   echo "File is not empty"
else
   echo "FIle is empty or does not exist"
fi
