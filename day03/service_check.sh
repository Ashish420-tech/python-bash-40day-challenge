#!/bin/bash

echo "Enter directory:"
read dir

if [ -d $dir ]
then
  echo "Directory Found"
else
  echo "Directory Not Found"
fi
