#!/bin/bash
# Purpose: Capture multiple user inputs interactively and display formatted output
# Use Case: Demonstrates collecting and processing multiple data points
# DevOps Context: Used in automated onboarding systems and configuration prompts

# Read student name from user input; -p displays the prompt string
# Variable 'name' stores the entered value for later use
read -p "Enter name:" name

# Read student age from user input; -p displays the prompt string
# Variable 'age' stores the entered value for later use
read -p "Enter age:" age

# Display student information with variable expansion using $ prefix
echo "Student name: $name"
echo "Student age: $age"
