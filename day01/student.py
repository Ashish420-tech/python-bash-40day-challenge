# Purpose: Capture multiple user inputs and display formatted output
# Use Case: Demonstrates collecting and processing multiple data points interactively
# DevOps Context: Used in automated enrollment systems and configuration scripts

# Prompt user to enter name and store as string variable
name = input("Enter name:")
# Prompt user to enter age and convert to integer type for numeric operations
age = int(input("Enter age:"))

# Display captured student information with labeled output for clarity
print("Student Name:", name)
print("Student age:", age)
