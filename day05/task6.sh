#!/bin/bash

read -p "Enter file name:" file

if [ -x "$file" ]
then
   echo "File is executable"
else
   echo "File is not  executable"
fi

