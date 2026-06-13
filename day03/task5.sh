#!/bin/bash

echo "Enter age:"
read age

if [ $age -ge 18 ]
then
    echo "adult"
else
    echo "Minor"
fi
