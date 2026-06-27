# 🚀 Day 11 – Python Modules, Packages & Advanced Bash Scripting

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Bash](https://img.shields.io/badge/Bash-Scripting-black?logo=gnubash)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=ubuntu)
![DevOps](https://img.shields.io/badge/DevOps-Automation-success)
![Day-11](https://img.shields.io/badge/40DaysChallenge-Day11-red)

## 📌 Objective

Day 11 focuses on writing **modular, reusable, and maintainable automation scripts** using Python and Bash.

Instead of writing everything in a single file, today's learning introduces:

- Creating custom Python modules
- Organizing code using packages
- Using Python standard libraries
- Managing dependencies with virtual environments
- Writing reusable Bash functions
- Passing command-line arguments
- Building practical Linux automation scripts

These are essential skills for **DevOps Engineers, SREs, Cloud Engineers, and Linux Administrators**.

---

# 📚 Topics Covered

## 🐍 Python

- Creating Custom Modules
- Importing Modules
- Import Specific Functions
- Module Aliasing
- Python Packages
- `__init__.py`
- Standard Library
  - math
  - random
  - datetime
  - os
- Virtual Environment (venv)
- Installing Packages using pip
- requirements.txt

---

## 🐧 Bash

- Functions
- Function Arguments
- Returning Values
- Command-Line Arguments
- Loop Through Arguments
- Backup Automation Script
- System Health Monitoring Script

---

# 📂 Folder Structure

```
Day11/
│
├── Python/
│   ├── math_utils.py
│   ├── task1_custom_module.py
│   ├── task2_import.py
│   ├── task3_alias.py
│   ├── task4_package/
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   ├── greeting.py
│   │   └── main.py
│   ├── task5_math.py
│   ├── task6_random.py
│   ├── task7_datetime.py
│   ├── task8_os.py
│   ├── task9_requests.py
│   └── requirements.txt
│
└── Bash/
    ├── task1_function.sh
    ├── task2_function_arguments.sh
    ├── task3_return_value.sh
    ├── task4_cli_arguments.sh
    ├── task5_loop_arguments.sh
    ├── task6_backup.sh
    └── task7_system_health.sh
```

---

# 🐍 Python Programs

## 1️⃣ Custom Module

Created a reusable Python module containing arithmetic operations.

### Concepts Learned

- import
- reusable code
- functions
- modules

Example:

```python
import math_utils

print(math_utils.add(10,20))
```

---

## 2️⃣ Import Specific Functions

Imported only required functions.

```python
from math_utils import add
```

Learned:

- selective importing
- cleaner code

---

## 3️⃣ Module Aliasing

Used aliases for shorter code.

```python
import math_utils as mu
```

Benefit:

- improved readability
- shorter syntax

---

## 4️⃣ Python Package

Created a package containing multiple modules.

```
task4_package/

calculator.py

greeting.py

__init__.py
```

Learned:

- package structure
- organizing projects
- importing from packages

---

## 5️⃣ math Module

Used Python's built-in math library.

Functions used:

- sqrt()
- factorial()
- pow()
- pi

---

## 6️⃣ random Module

Generated random numbers.

Functions:

- randint()
- choice()

Useful for:

- automation
- testing
- simulations

---

## 7️⃣ datetime Module

Displayed current date and time.

Functions:

- now()
- date()
- time()

Common DevOps use cases:

- timestamps
- logging
- backups

---

## 8️⃣ os Module

Retrieved system information.

Functions:

- getcwd()
- listdir()

Useful for:

- filesystem automation
- deployment scripts
- CI/CD pipelines

---

## 9️⃣ requests Module

Installed third-party package.

Example:

```python
import requests

response=requests.get("https://api.github.com")
```

Learned:

- HTTP requests
- REST APIs
- external libraries

---

# 📦 Virtual Environment

Created isolated Python environments.

Create

```bash
python3 -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

Install package

```bash
pip install requests
```

Freeze dependencies

```bash
pip freeze > requirements.txt
```

Install later

```bash
pip install -r requirements.txt
```

Deactivate

```bash
deactivate
```

---

# 🐧 Bash Programs

## 1️⃣ Functions

Created reusable Bash functions.

```bash
welcome(){

echo "Welcome"

}
```

---

## 2️⃣ Function Arguments

Passed parameters into functions.

```bash
greet Ashish
```

---

## 3️⃣ Return Values

Captured output from functions.

```bash
result=$(add 10 20)
```

---

## 4️⃣ Command-Line Arguments

Learned

```
$1
$2
$#
$@
```

Example

```bash
bash task4_cli_arguments.sh AWS Docker
```

Output

```
First Argument : AWS

Second Argument : Docker

Total Arguments : 2
```

---

## 5️⃣ Loop Through Arguments

Processed unlimited arguments.

```bash
for arg in "$@"
```

---

## 6️⃣ Backup Script

Created a reusable backup utility.

Features

- accepts directory
- creates tar.gz archive
- validates input
- success/error handling

Example

```bash
bash task6_backup.sh /home/user/Documents
```

---

## 7️⃣ System Health Monitoring

Collected Linux system information.

Displays

- Hostname
- Date
- Disk Usage
- Memory Usage
- CPU Load
- Logged-in Users
- Current Directory

Useful for

- Server monitoring
- Health checks
- Automation
- Daily reports

---

# 💻 Commands Practiced

```bash
python3

pip

venv

import

from

source

deactivate

hostname

pwd

date

df -h

free -h

uptime

who

tar

echo
```

---

# 🎯 Learning Outcomes

After completing Day 11, I can:

✅ Create custom Python modules

✅ Import modules efficiently

✅ Build Python packages

✅ Use Python standard libraries

✅ Create isolated virtual environments

✅ Install external packages

✅ Manage project dependencies

✅ Write reusable Bash functions

✅ Pass command-line arguments

✅ Build backup automation scripts

✅ Generate Linux system health reports

---

# 💼 DevOps Real-World Use Cases

These concepts are widely used for:

- Infrastructure Automation
- Linux Administration
- CI/CD Pipelines
- Server Monitoring
- Log Collection
- Backup Automation
- Deployment Scripts
- Cloud Automation
- Configuration Management
- Scheduled Cron Jobs

---

# 🧠 Interview Questions

### Python

- What is a module?
- What is a package?
- Difference between module and package?
- What is `__init__.py`?
- Explain `import` vs `from import`.
- Why use virtual environments?
- What is `requirements.txt`?
- Difference between built-in and third-party modules?

### Bash

- What are Bash functions?
- How do you pass arguments to a script?
- Difference between `$@` and `$*`?
- What does `$#` represent?
- How do you return values from a Bash function?
- How would you automate backups in Linux?
- How would you create a reusable monitoring script?

---

# 🚀 Key Takeaways

✔ Modular programming improves maintainability.

✔ Packages help organize larger projects.

✔ Virtual environments isolate dependencies.

✔ Bash functions reduce code duplication.

✔ Command-line arguments make scripts flexible.

✔ Automation scripts simplify Linux administration.

✔ These skills are essential for DevOps, SRE, Cloud, and Automation Engineers.

---

# 📅 40 Days Python + Bash Scripting Challenge

**Day 11 Complete ✅**

**Previous Topics**

- Python Basics
- Variables
- Operators
- Conditions
- Loops
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Functions
- File Handling
- Exception Handling

**Today's Focus**

- Python Modules
- Packages
- Virtual Environment
- Bash Functions
- CLI Arguments
- Automation Scripts

➡️ **Next:** Day 12 – Object-Oriented Programming (OOP) in Python + Advanced Bash Automation

---

## 👨‍💻 Author

**Ashish Mondal**

**Python + Bash Scripting for DevOps – 40 Days Challenge**

If you found this repository helpful, consider giving it a ⭐ and following my journey toward becoming a DevOps Engineer.
