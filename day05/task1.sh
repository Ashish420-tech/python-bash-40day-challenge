#!/bin/bash
read -p "Enter file or directory:" path

if [ -e "$path" ]
then
    echo "$path exists"
else
    echo "$path does not exists"
fi
