#!/bin/bash
echo "Enter filename"
read file

if [ -e "$file" ]
then 
    echo "Exists"
else
    echo "Not found"
fi
