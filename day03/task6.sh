#!/bin/bash

echo "Enter 1st number:"
read num1

echo "Enter 2nd number:"
read num2

if [ $num1 gt $num2 ]
then
   echo "Larger number $num1"
else
   echo "Smaller number $num2"
fi
