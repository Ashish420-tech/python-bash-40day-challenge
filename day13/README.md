# Day 13 – Advanced OOP & DevOps Automation with Python and Bash

## Overview

Day 13 focuses on applying **Object-Oriented Programming (OOP)** concepts and integrating **Python with Bash scripting** to solve real-world DevOps automation tasks. The exercises demonstrate how Python can manage server inventories while Bash collects system health information, providing a foundation for infrastructure automation.

---

# Learning Objectives

* Understand Inheritance in Python
* Learn Method Overriding
* Implement Multiple Inheritance
* Use `super()` to invoke parent constructors
* Explore Polymorphism
* Build a menu-driven Server Inventory Manager
* Store and retrieve server information using files
* Create Bash scripts for server administration
* Execute Bash scripts from Python
* Generate automated server health reports

---

# Technologies Used

* Python 3
* Bash Shell
* Linux (Ubuntu/WSL)
* VS Code
* Git & GitHub

---

# Project Structure

```text
day13/
│
├── python/
│   ├── inheritance.py
│   ├── overriding.py
│   ├── multiple_inheritance.py
│   ├── super_demo.py
│   ├── polymorphism.py
│   ├── inventory.py
│   └── health_runner.py
│
├── bash/
│   ├── arrays.sh
│   ├── readfile.sh
│   ├── menu.sh
│   └── health.sh
│
├── servers.txt
├── health_report.txt
└── README.md
```

---

# Python Programs

## 1. Inheritance

Demonstrates how a child class inherits properties and methods from a parent class.

**Topics Covered**

* Parent Class
* Child Class
* Code Reusability

---

## 2. Method Overriding

Shows how a child class can provide its own implementation of a parent method.

**Topics Covered**

* Runtime Polymorphism
* Customized Behavior

---

## 3. Multiple Inheritance

Illustrates inheriting features from more than one parent class.

**Topics Covered**

* Multiple Parent Classes
* Shared Functionalities

---

## 4. Using `super()`

Demonstrates invoking the constructor of a parent class from a child class.

**Topics Covered**

* Parent Constructor
* Constructor Chaining

---

## 5. Polymorphism

Demonstrates different objects responding to the same method in different ways.

**Topics Covered**

* Dynamic Method Dispatch
* Flexible Code Design

---

## 6. Server Inventory Manager

A menu-driven Python application to manage server records.

### Features

* Add new server
* View server list
* Delete server (optional enhancement)
* Save inventory to a file
* Load inventory from a file
* Exit application

### Sample Menu

```text
===== Server Inventory Manager =====

1. Add Server
2. View Servers
3. Save Servers
4. Exit
```

### Learning Outcomes

* Lists
* Loops
* Conditional Statements
* File Handling
* User Input
* Menu-Driven Programming

---

# Bash Scripts

## Arrays

Demonstrates storing multiple server names using Bash arrays.

### Concepts

* Arrays
* Looping
* Variable Expansion

---

## Reading from a File

Reads server names from a text file.

### Concepts

* while loop
* read command
* File Input

---

## Menu-Driven Bash Script

Implements a simple interactive administration menu.

### Options

* List Files
* Show Date
* Exit

---

## Server Health Monitoring Script

Collects essential Linux system information.

### Displays

* Hostname
* System Uptime
* Memory Usage
* Disk Usage
* CPU Information

This script can be used as a lightweight system health check for Linux servers.

---

# Python + Bash Integration

Python executes the Bash health script and redirects the output to a report file.

### Workflow

```text
Python
      │
      ▼
Executes health.sh
      │
      ▼
Collects System Information
      │
      ▼
Generates health_report.txt
```

This demonstrates cross-language automation commonly used in DevOps environments.

---

# DevOps Use Cases

The concepts learned in this project are applicable to:

* Linux Server Administration
* Infrastructure Automation
* Server Inventory Management
* System Health Monitoring
* Automation Scripts
* DevOps Operations
* Site Reliability Engineering (SRE)

---

# Key Python Concepts Learned

* Classes and Objects
* Inheritance
* Multiple Inheritance
* Method Overriding
* Polymorphism
* Constructors
* `super()`
* Lists
* Functions
* File Handling
* User Input
* Loops

---

# Key Bash Concepts Learned

* Arrays
* Variables
* while Loop
* case Statement
* Shell Functions
* Reading Files
* Linux System Commands

---

# Commands Used

## Run Python Programs

```bash
python3 inheritance.py
python3 overriding.py
python3 multiple_inheritance.py
python3 super_demo.py
python3 polymorphism.py
python3 inventory.py
python3 health_runner.py
```

## Run Bash Scripts

```bash
chmod +x *.sh

./arrays.sh
./readfile.sh
./menu.sh
./health.sh
```

---

# Git Commands

```bash
git checkout -b day13-advanced-oop

git add .

git commit -m "Day 13: Advanced OOP, Bash Automation and Server Inventory Manager"

git push origin day13-advanced-oop
```

---

# Skills Gained

* Object-Oriented Programming
* Linux Automation
* Bash Scripting
* Python File Handling
* Python-Bash Integration
* Server Inventory Automation
* System Health Monitoring
* DevOps Automation Fundamentals

---

# Conclusion

Day 13 bridges core Python OOP concepts with practical DevOps automation. By combining Python and Bash, this project demonstrates how automation tools can manage server inventories, execute administrative tasks, and generate health reports—skills directly applicable to DevOps, System Administration, and SRE roles.
