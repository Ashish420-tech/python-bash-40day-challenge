#!/bin/bash
# Purpose: Accept a command-line argument and display a personalized greeting
# Use Case: Demonstrates parameter passing in shell scripts
# DevOps Context: Used in deployment scripts to pass configuration values and user info

# Display greeting using first positional parameter ($1 - first argument passed to script)
echo "Hello $1"
