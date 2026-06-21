# 🚀 Day 08 – Exception Handling & Error Management | Python + Bash Scripting for DevOps

Welcome to **Day 08** of my **40 Days Python + Bash Scripting for DevOps Challenge**.

Today I learned how to build **fault-tolerant automation scripts** by handling runtime errors gracefully in Python and Bash. Exception handling is a critical skill for DevOps engineers because automation should continue to run reliably even when unexpected errors occur.

---

# 📚 Topics Covered

## 🐍 Python

* Exception Handling
* `try`
* `except`
* `else`
* `finally`
* Handling Specific Exceptions

  * `ZeroDivisionError`
  * `ValueError`
  * `FileNotFoundError`
* Generic Exception Handling
* Custom Exceptions using `raise`
* File Handling with Exceptions

---

## 🐧 Bash

* Exit Status (`$?`)
* Success & Failure Detection
* Output Redirection (`>`)
* Error Redirection (`2>`)
* Combining Output & Error (`2>&1`)
* Logical Operators

  * `&&`
  * `||`
* File Existence Checking
* Directory Creation
* Custom Exit Codes

---

# 📂 Project Structure

```text
day08/
│
├── mini_challange.py
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── task5.py
├── task6.py
├── task7.py
├── task8.py
├── task9.py
├── task10.py
├── task11.py
│
├── task1.sh
├── task2.sh
├── task3.sh
├── task4.sh
├── reverse_string.sh
├── string1.sh
│
├── error.log
├── location.txt
├── project/
└── Test/
```

---

# 🐍 Python Programs

## task1.py

Basic Exception Handling using `try` and `except`.

### Concepts

* User Input
* Exception Handling

---

## task2.py

Handling Multiple Exceptions.

### Concepts

* `ZeroDivisionError`
* `ValueError`

---

## task3.py

Using Generic Exception Object.

### Concepts

* `Exception as e`
* Displaying Error Messages

---

## task4.py

Using `finally` block.

### Concepts

* File Handling
* Cleanup
* Always Executed Block

---

## task5.py

Printing Exception Message.

### Concepts

* Exception Object

---

## task6.py

Creating Custom Exception.

### Concepts

* `raise Exception`

---

## task7.py

Division Program with Zero Division Handling.

---

## task8.py

Handling Invalid User Input.

---

## task9.py

Opening File with Exception Handling.

---

## task10.py

Using `else` Block.

### Concepts

* Executes only if no exception occurs.

---

## task11.py

Using `finally`.

### Concepts

* Guaranteed execution.

---

# ⭐ Mini Challenge

## mini_challange.py

### Objective

Create a program that

* Accepts a filename
* Opens the file
* Displays its contents
* Counts the total number of lines
* Handles missing files gracefully

### Features

* File Handling
* Exception Handling
* Line Counter
* User Input
* File Reading

Example Output

```text
Enter a file name: demo.txt

Python
Bash
DevOps
Linux

Number of line: 8
```

---

# 🐧 Bash Programs

## task1.sh

Create a directory and verify success using Exit Status.

---

## task2.sh

Check whether a file exists.

---

## task3.sh

Redirect error messages into `error.log`.

---

## task4.sh

Save current working directory into `location.txt`.

---

# 📝 Additional Bash Practice

## reverse_string.sh

Reverse a string using Bash loops.

### Example

```bash
./reverse_string.sh DevOps
```

Output

```text
spOveD
```

---

## string1.sh

Two-fer challenge.

Example

```bash
./string1.sh Ashish
```

Output

```text
One for Ashish, one for me.
```

---

# 🎯 Learning Outcomes

By completing Day 08, I learned how to:

* Handle runtime exceptions in Python
* Prevent program crashes
* Read files safely
* Create custom exceptions
* Use `try`, `except`, `else`, and `finally`
* Capture Linux command errors
* Work with Exit Status (`$?`)
* Redirect output and errors
* Build reliable automation scripts

---

# 🛠️ Skills Practiced

* Python
* Bash
* Linux
* Error Handling
* Exception Handling
* File Handling
* Shell Scripting
* DevOps Automation
* Problem Solving

---

# 🚀 DevOps Relevance

Exception handling is one of the most important skills in DevOps automation.

These concepts are widely used in:

* CI/CD Pipelines
* Deployment Scripts
* Log Processing
* Monitoring Automation
* Infrastructure Automation
* Backup Scripts
* Production Maintenance
* System Administration

---

# 📊 Day 08 Summary

| Category           | Completed |
| ------------------ | --------- |
| Python Programs    | ✅ 11      |
| Bash Scripts       | ✅ 6       |
| Mini Challenge     | ✅         |
| Exception Handling | ✅         |
| File Handling      | ✅         |
| Error Redirection  | ✅         |
| Exit Status        | ✅         |

---

# 💡 Key Takeaway

> "Good automation doesn't just work—it handles failures gracefully."

---

## 🔗 Repository

```text
https://github.com/Ashish420-tech/python-bash-40day-challenge
```

---

## 👨‍💻 Author

**Ashish Mondal**

DevOps | Cloud | Linux | Python | Bash | AWS | Azure | Kubernetes | Terraform

---

⭐ If you found this repository helpful, consider giving it a **Star** and following my **40 Days Python + Bash Scripting for DevOps Challenge**!
