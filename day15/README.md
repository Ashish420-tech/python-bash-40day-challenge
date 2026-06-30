🚀 Day 15 – Exception Handling, Logging & Bash Error Handling

40 Days Python + Bash Scripting for DevOps Challenge










📖 Overview

Welcome to Day 15 of the Python + Bash Scripting for DevOps Challenge.

Today's focus is on writing reliable and production-ready scripts. In real-world DevOps environments, scripts should not fail silently—they must detect errors, log meaningful information, and recover gracefully whenever possible.

By learning Exception Handling, Logging, and Bash Error Handling, you'll build scripts that are robust, maintainable, and suitable for production environments.

🎯 Learning Objectives

After completing Day 15, you will be able to:

Handle runtime exceptions in Python
Prevent unexpected application crashes
Raise and create custom exceptions
Generate logs using Python's logging module
Understand log levels and logging best practices
Implement Bash error handling
Use exit status codes effectively
Use trap for cleanup operations
Build production-ready automation scripts
📂 Project Structure
day15/
│
├── python/
│   ├── exception_basic.py
│   ├── multiple_exception.py
│   ├── else_demo.py
│   ├── finally_demo.py
│   ├── raise_exception.py
│   ├── custom_exception.py
│   └── logging_demo.py
│
├── bash/
│   ├── error_handling.sh
│   ├── trap_demo.sh
│   └── logging.sh
│
├── logs/
│   ├── app.log
│   └── script.log
│
└── README.md
🐍 Python Topics Covered
✅ Basic Exception Handling

Learn how to use:

try
except

Handle common runtime errors like:

ZeroDivisionError
ValueError
FileNotFoundError
✅ Multiple Exceptions

Catch different exceptions individually to make debugging easier.

Example scenarios:

Invalid user input
Missing files
Division by zero
✅ else Block

The else block executes only when no exception occurs.

This helps separate successful execution from error handling.

✅ finally Block

The finally block always executes regardless of whether an exception occurs.

Useful for:

Closing files
Closing database connections
Cleaning up resources
✅ Raising Exceptions

Use the raise keyword to trigger exceptions manually.

Example:

Invalid age
Invalid salary
Invalid configuration
✅ Custom Exceptions

Create your own exception classes for business logic.

Example:

class SalaryError(Exception):
    pass

Custom exceptions make applications easier to maintain and debug.

📜 Python Logging

Instead of using:

print("Application Started")

Professional applications use the logging module.

Example features:

INFO
WARNING
ERROR
CRITICAL

Benefits:

Persistent logs
Timestamped records
Easier debugging
Production monitoring

Generated log:

INFO: Application Started
WARNING: High Memory Usage
ERROR: File Not Found
🐧 Bash Topics Covered
✅ Exit Status

Understand Linux exit codes.

echo $?

Meaning:

Exit Code	Meaning
0	Success
Non-zero	Failure
✅ set -e

Exit immediately if any command fails.

set -e

Ideal for deployment and automation scripts.

✅ set -u

Detect undefined variables.

set -u

Helps avoid unexpected script behavior.

✅ set -o pipefail

Ensures pipeline failures are detected.

set -o pipefail

Very useful in CI/CD pipelines.

✅ trap Command

Execute cleanup commands when a script exits.

Example use cases:

Delete temporary files
Stop services
Display exit messages
Cleanup resources
✅ Bash Logging

Store script execution details into log files.

Example:

Mon Jun 30 10:15 Script Started
Mon Jun 30 10:16 Backup Completed
Mon Jun 30 10:17 Script Finished
💻 Practical Programs
Python
Basic Exception Handling
Multiple Exception Handling
Else Block Demo
Finally Block Demo
Raise Exception
Custom Exception
Logging Demo
Bash
Error Handling
Exit Status Demo
Trap Demo
Logging Demo
🚀 Mini Project
Server Health Checker

Develop a simple monitoring script that checks:

CPU Usage
Memory Usage
Disk Usage
System Uptime

The script should:

Display system health information
Save output into log files
Handle runtime errors gracefully
Generate readable reports

Example Output:

==============================
Server Health Report
==============================

CPU Usage      : 18%
Memory Usage   : 42%
Disk Usage     : 61%
Uptime         : 3 Days

Status         : HEALTHY
💡 Real DevOps Use Cases

These concepts are widely used in:

CI/CD Pipelines
Infrastructure Automation
Server Monitoring
Kubernetes Scripts
Deployment Automation
Backup Scripts
Cron Jobs
Cloud Automation
Log Monitoring
Incident Response
📚 Key Takeaways
Exception handling prevents application crashes.
Logging is essential for debugging and production monitoring.
Bash error handling improves script reliability.
Exit codes communicate command success or failure.
trap enables resource cleanup and graceful exits.
Production-grade automation always includes proper error handling and logging.
🛠️ Skills Gained
Python Exception Handling
Python Logging
Custom Exceptions
Linux Exit Codes
Bash Error Handling
Bash Logging
Production Automation
DevOps Scripting Best Practices
🎯 Challenge Completed

✅ Learned Python Exception Handling

✅ Implemented Multiple Exception Handling

✅ Worked with else and finally

✅ Created Custom Exceptions

✅ Implemented Python Logging

✅ Learned Bash Error Handling

✅ Used set -e, set -u, and pipefail

✅ Implemented trap

✅ Generated Log Files

✅ Built a Server Health Checker

🤝 Connect With Me

If you found this project helpful, feel free to connect and follow my DevOps journey!

💼 LinkedIn: www.linkedin.com/in/ashish-mondal420
💻 GitHub: https://github.com/Ashish420-tech

If this repository helps you learn Python, Bash, or DevOps Automation, consider giving it a ⭐ to support the project.
