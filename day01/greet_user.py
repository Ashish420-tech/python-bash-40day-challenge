import sys
# Purpose: Process command-line arguments in Python for user personalization
# Use Case: Demonstrates sys module for CLI argument handling
# DevOps Context: Essential for automation scripts receiving parameters from CI/CD pipelines

# Check if minimum required arguments are provided
# len(sys.argv) includes script name at index 0, so <2 means no arguments passed
if len(sys.argv) < 2:
    # Display usage instructions for script execution
    print("Usage: python3 greet_user.py <name>")
else:
    # Access first argument (index 1) and display personalized greeting
    print("Hello ", sys.argv[1])
