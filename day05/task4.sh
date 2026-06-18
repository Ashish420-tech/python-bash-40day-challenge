#!/bin/bash

read -p "Enter file name: " file

if [ -r "$file" ]
then
   echo "File is readable"
else
   echo "Read permission denied"
fi 
