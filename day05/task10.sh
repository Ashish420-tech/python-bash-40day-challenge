#!/bin/bash

read -p "Enter file name:" filename

if [ -f "$filename" ]
then
   while read line
   do
     echo "$line"
   done < names.txt
else
   echo " Does not exist"
fi
