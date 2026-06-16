#!/bin/bash

echo "Enter file name need to read"
read filename


if [ -f "$filename" ]
then 
  while read -r line
  do
    echo "$line"

  done < "$filename"
else
   echo "Enter correct filename"
fi
