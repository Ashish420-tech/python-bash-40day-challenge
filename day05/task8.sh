#!/bin/bash

read -p "Enter filename: " file

if [ -L "$file" ]
then
   echo " It is a symbolic link."
else
   echo " It is a sysmbolic link."
fi
