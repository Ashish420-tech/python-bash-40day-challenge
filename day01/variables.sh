#!/bin/bash
# Purpose: Demonstrate variable declaration and usage in Bash
# Use Case: Shows fundamental concepts of variable assignment and parameter expansion
# DevOps Context: Foundation for configuration management and parameter passing in deployment scripts

# Assign string value to variable (no spaces around = for proper syntax)
# Variables store data for reuse throughout script execution
name="Ashish"
# Assign numeric value to variable
age=25

# Display variables using echo; $ prefix required to expand variable value
echo "Name: $name"
echo "Age: $age"
