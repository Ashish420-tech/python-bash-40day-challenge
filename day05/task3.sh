#!/bin/bash

read -p "Enter directory" dir

if [ -d  "$dir" ]
then
   echo "Directory exists"
else
   echo "Not a directory"
fi
