#!/bin/bash
# Purpose: Accept user input with validation and display conditional output
# Use Case: Demonstrates argument validation and conditional logic
# DevOps Context: Critical for deployment safety; prevents execution without required parameters

# Check if number of arguments ($#) is less than 1
# This validation ensures the script receives required input before processing
if [ $# -lt 1 ]
then
    # Display usage instructions when argument validation fails
    echo "Usage: ./greet.sh <name>"
else
    # Echo greeting with the validated argument
    echo "Hello $1"
fi
