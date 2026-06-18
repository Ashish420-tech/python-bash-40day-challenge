#!/bin/bash

read -p "Enter file name:" filename

if [ -f "$filename" ]
then
   > report.txt
   

   i=1

   while IFS= read -r line
   do

     echo "Employee $i: $line"
     echo "Employee $i: $line" >> report.txt     
     ((i++))
   done < "$filename"

   echo "Total Employee: $((i-1))"
else
   echo "File not exist"
fi
