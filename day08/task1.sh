#!/bin/bash

mkdir project

if [ $? -eq 0 ]
then 
  echo "Directory created"
else
  echo " Not created"
fi
