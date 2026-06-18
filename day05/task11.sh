#!/bin/bash

read -p "Enter filename:" filename

if [ -f "$filename" ]
then
   while read line
   do
     echo " Employee: $line"
   done < employee.txt
else
   echo " File does not exists"
fi
