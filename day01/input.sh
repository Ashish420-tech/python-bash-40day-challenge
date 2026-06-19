#!/bin/bash
# Purpose: Capture interactive user input and display output
# Use Case: Demonstrates read command for runtime user interaction
# DevOps Context: Used in interactive setup scripts and configuration wizards

# Read user input with prompt; -p flag displays the prompt string
# Store input in 'name' variable for later use
read -p "Enter Name: " name

# Display welcome message using the captured variable value
echo "Welcome $name"
