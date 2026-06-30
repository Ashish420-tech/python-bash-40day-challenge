# Day 14 – File Manager & DevOps Log Manager (Python + Bash)

## 📌 Overview

Day 14 focuses on building a real-world **DevOps Log Manager** using **Python Object-Oriented Programming (OOP)** and **Bash Scripting**.

This project demonstrates how to perform file operations, implement reusable classes, handle exceptions, and create menu-driven applications. These are practical skills frequently used by DevOps Engineers, Linux Administrators, and SREs for automation and log management.

---

# 🎯 Learning Objectives

## Python

* Object-Oriented Programming (OOP)
* Class Inheritance
* File Handling
* Exception Handling
* Date & Time Module
* Menu-Driven Applications

## Bash

* Functions
* User Input
* File Operations
* Conditional Statements
* Case Statement
* Log File Backup

---

# 📂 Project Structure

```text
day14/
│
├── python/
│   ├── file_manager.py
│   ├── logger.py
│   ├── main.py
│   ├── sample.txt
│   └── README.md
│
├── bash/
│   ├── log_manager.sh
│   ├── backup/
│   └── README.md
│
└── README.md
```

---

# 🐍 Python Project

## file_manager.py

Implements a reusable `FileManager` class for common file operations.

### Features

* Create a file
* Write data
* Append data
* Read file contents
* Delete a file
* Check if a file exists

---

## logger.py

Extends the `FileManager` class using inheritance.

### Features

* Automatically adds timestamps to log messages
* Appends log entries to a file
* Demonstrates class inheritance

Example Log Entry:

```text
[2026-06-30 14:15:20] Application Started
```

---

## main.py

Interactive menu-driven application.

### Menu

```text
1. Create Log File
2. Write Log
3. Append Log
4. Read Log
5. Check File Exists
6. Delete Log
7. Exit
```

---

# 💻 Bash Project

The Bash Log Manager provides a simple command-line interface to manage log files.

### Features

* Create log file
* View log file
* Delete log file
* Backup log file
* Exit application

---

# ▶️ How to Run

## Python

Move into the Python directory:

```bash
cd day14/python
```

Run the application:

```bash
python3 main.py
```

---

## Bash

Move into the Bash directory:

```bash
cd day14/bash
```

Provide execute permission:

```bash
chmod +x log_manager.sh
```

Run:

```bash
./log_manager.sh
```

---

# 📚 Python Concepts Practiced

* Classes
* Objects
* Constructors
* Inheritance
* Methods
* Exception Handling
* File Handling
* Modules
* Date & Time

---

# 📚 Bash Concepts Practiced

* Variables
* Functions
* User Input
* File Commands
* Case Statement
* If-Else Conditions

---

# 🛠 Skills Gained

* File management using Python
* Menu-driven application development
* Object-oriented programming
* Exception handling
* Log management automation
* Bash scripting for Linux administration
* DevOps automation fundamentals

---

# 🚀 Real-World DevOps Use Cases

* Application log management
* Server log monitoring
* Deployment logging
* Automation scripts
* Configuration backups
* Linux administration tasks

---

# 📖 Key Takeaways

* Built reusable Python classes.
* Implemented inheritance for code reusability.
* Managed files safely using exception handling.
* Created a menu-driven log management application.
* Practiced Bash scripting for file operations.
* Strengthened automation skills used in DevOps environments.

---

# 🎯 Outcome

By completing Day 14, you have developed a practical log management application using Python and Bash, reinforcing essential programming concepts while applying them to real-world DevOps automation scenarios.

---

## 👨‍💻 Author

**Ashish Mondal**

**40 Days Python + Bash Scripting for DevOps Challenge**
