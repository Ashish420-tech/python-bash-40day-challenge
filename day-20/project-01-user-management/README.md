# 🚀 Project 01 - Linux User & Group Management Automation

## 📌 Project Overview

This project automates **Linux user and group management** using Bash scripting. Instead of manually creating users, groups, passwords, and directory structures, the entire process is performed through reusable shell scripts.

This project simulates a real-world **Linux System Administrator** onboarding task and is ideal for practicing Linux administration and Bash scripting.

---

# 🎯 Objectives

* Create Linux users automatically
* Create Linux groups automatically
* Assign users to appropriate groups
* Set user passwords
* Create a company directory structure
* Practice Linux administration using automation
* Learn Bash scripting fundamentals

---

# 🏢 Scenario

You are a Linux Administrator at **ABC Technologies**.

The HR department has hired new employees, and you need to:

* Create employee accounts
* Create department groups
* Assign users to departments
* Configure passwords
* Build the company folder structure

Instead of running commands one by one, everything is automated using Bash scripts.

---

# 📁 Project Structure

```text
project-01-user-management/
│
├── create_users.sh
├── set_password.sh
├── company_structure.sh
├── README.md
└── screenshots/
```

---

# 👥 Users Created

| Username | Department |
| -------- | ---------- |
| dev1     | Developers |
| dev2     | Developers |
| qa1      | QA         |
| devops1  | DevOps     |
| manager1 | Management |

---

# 👨‍💻 Groups Created

* developers
* qa
* devops
* managers

---

# 📂 Directory Structure

```text
/company
│
├── HR
├── IT
├── Finance
└── Developers
    ├── Backend
    └── Frontend
```

---

# 🛠 Technologies Used

* Kali Linux
* Bash Shell
* Linux User Management
* Linux Group Management
* File Permissions
* Shell Scripting

---

# 📜 Scripts

## 1. create_users.sh

This script:

* Creates required Linux groups
* Creates users with home directories
* Assigns the Bash shell
* Adds users to the appropriate groups
* Prevents duplicate creation

Run:

```bash
sudo ./create_users.sh
```

---

## 2. set_password.sh

This script:

* Sets passwords for all created users
* Uses the `chpasswd` command for automation

Run:

```bash
sudo ./set_password.sh
```

---

## 3. company_structure.sh

This script:

* Creates the company directory hierarchy
* Generates the required folder structure
* Displays the directory tree

Run:

```bash
sudo ./company_structure.sh
```

---

# ✅ Verification Commands

## Verify Users

```bash
cat /etc/passwd
```

```bash
getent passwd
```

```bash
id dev1
```

---

## Verify Groups

```bash
cat /etc/group
```

```bash
getent group
```

---

## Verify Home Directories

```bash
ls -l /home
```

---

## Verify User Membership

```bash
groups dev1
```

```bash
id devops1
```

---

## Verify Company Directory

```bash
tree /company
```

---

# 📚 Linux Concepts Practiced

* Linux User Management
* Linux Group Management
* Home Directory Creation
* Login Shell Configuration
* Bash Scripting
* Variables
* Arrays
* Loops
* Conditional Statements
* Command Exit Status
* File System Management
* Automation
* Linux Administration

---

# 📸 Suggested Screenshots

Include screenshots of:

* Project directory
* Script execution
* User creation
* Group creation
* Home directories
* `id` command output
* `groups` command output
* Company directory tree

---

# 🎓 Skills Gained

After completing this project, you will be able to:

* Manage Linux users
* Manage Linux groups
* Automate repetitive administrative tasks
* Write reusable Bash scripts
* Verify Linux system configurations
* Build production-style Linux automation

---

# 🚀 Future Improvements

* Read users from a CSV file
* Generate random passwords automatically
* Log all operations to a log file
* Add error handling and validation
* Send email notifications after account creation
* Add colored terminal output
* Create a menu-driven version of the script

---

# 📖 Learning Outcome

This project demonstrates the core Linux administration tasks performed by System Administrators and DevOps Engineers. By automating user provisioning with Bash scripting, you gain hands-on experience with Linux system management, scripting, and operational best practices that are directly applicable to enterprise environments.

---

**Author:** Ashish Mondal

**Platform:** Kali Linux

**Project:** Linux Mastery Series – Project 01

**Level:** Beginner → Intermediate

**Category:** Linux Administration & Bash Scripting
