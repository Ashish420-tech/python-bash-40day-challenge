# 🚀 Day 12 – Object-Oriented Programming (OOP) + Bash Automation

Welcome to **Day 12** of the **Python + Bash Scripting for DevOps – 40 Days Challenge**.

Today focuses on one of the most important programming paradigms used in real-world software development and DevOps automation: **Object-Oriented Programming (OOP)**. You'll also strengthen your Bash scripting skills by creating reusable automation scripts for system administration tasks.

---

# 📚 Topics Covered

## 🐍 Python – Object-Oriented Programming (OOP)

- What is OOP?
- Classes and Objects
- Constructors (`__init__`)
- Instance Variables
- Methods
- `self` Keyword
- Updating Object Attributes
- Class Variables
- Inheritance
- Method Overriding
- Encapsulation
- Mini Project – Server Manager

---

## 🐧 Bash Scripting

- Functions
- Arrays
- Loops
- Service Health Check
- Directory Backup
- Log Cleanup Automation

---

# 📂 Project Structure

```text
day12/
│
├── README.md
├── server.py
├── constructor.py
├── methods.py
├── class_variable.py
├── inheritance.py
├── encapsulation.py
├── server_manager.py
│
└── bash/
    ├── functions.sh
    ├── service_status.sh
    ├── backup.sh
    ├── cleanup_logs.sh
    └── health_check.sh
```

---

# 🐍 Python Programs

## 1. Server Class

Create a simple class and instantiate objects.

**Concepts**

- Class
- Object

---

## 2. Constructor Example

Initialize object attributes using `__init__()`.

Example:

```python
class Server:

    def __init__(self, name):
        self.name = name

server = Server("Production")

print(server.name)
```

Output

```
Production
```

---

## 3. Methods

Objects can perform actions.

Example:

```python
class Server:

    def __init__(self, name):
        self.name = name

    def start(self):
        print(self.name, "started")

    def stop(self):
        print(self.name, "stopped")

server = Server("Database")

server.start()
server.stop()
```

Output

```
Database started
Database stopped
```

---

## 4. Class Variables

Variables shared by every object.

```python
class Employee:

    company = "ABC Pvt Ltd"

    def __init__(self, name):
        self.name = name
```

---

## 5. Inheritance

Reuse existing class functionality.

```python
class Linux:

    def install(self):
        print("Installing Linux")

class Ubuntu(Linux):
    pass

u = Ubuntu()
u.install()
```

---

## 6. Method Overriding

Modify inherited methods.

```python
class Linux:

    def install(self):
        print("Linux Install")

class Ubuntu(Linux):

    def install(self):
        print("Ubuntu Install")

u = Ubuntu()
u.install()
```

---

## 7. Encapsulation

Hide internal object data.

```python
class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def show(self):
        print(self.__balance)

b = Bank(5000)
b.show()
```

---

## 8. Mini Project – Server Manager

A simple infrastructure management application.

Features:

- Create server objects
- Store Server Name
- Store IP Address
- Store Status
- Start Server
- Stop Server
- Display Server Information

Example

```
Name   : Production
IP     : 10.0.0.1
Status : Running
```

---

# 🐧 Bash Scripts

## Functions

Reusable Bash functions.

```bash
backup(){
    echo "Backup Started"
}

backup
```

---

## Service Health Checker

Checks whether important Linux services are running.

Example:

```bash
nginx Running
ssh Running
cron Running
```

---

## Backup Script

Copies files from source directory to backup directory.

```bash
cp -r ~/Documents ~/backup
```

---

## Log Cleanup Script

Deletes old log files.

```bash
find /var/log -name "*.log" -mtime +7 -delete
```

> **Note:** Test the `find` command carefully before using the `-delete` option, especially on production systems.

---

# 🎯 Learning Outcomes

After completing Day 12, you will be able to:

- Design reusable Python classes.
- Create and manage objects.
- Use constructors effectively.
- Understand instance and class variables.
- Implement inheritance and method overriding.
- Apply encapsulation to protect data.
- Build object-oriented automation scripts.
- Create reusable Bash functions.
- Automate system administration tasks using Bash.

---

# 💼 DevOps Use Cases

The OOP concepts learned today are widely used in:

- Infrastructure Automation
- AWS SDK (Boto3)
- Azure SDK
- Google Cloud SDK
- Terraform Providers
- Kubernetes Python Client
- Docker SDK
- Jenkins Automation
- Ansible Python Modules

Example:

```python
server.start()
container.stop()
ec2.launch()
pod.restart()
```

These are all examples of object-oriented programming in real-world DevOps.

---

# 🧠 Key Takeaways

- OOP makes code modular, reusable, and scalable.
- Classes represent real-world entities.
- Objects store data and perform actions.
- Constructors initialize object state.
- Inheritance reduces code duplication.
- Encapsulation improves security and maintainability.
- Bash functions simplify automation by promoting code reuse.

---

# 🔥 Day 12 Challenge

Build an **Infrastructure Manager** application that:

- Creates multiple server objects.
- Tracks server name, IP, environment, and status.
- Starts and stops servers.
- Displays server details.
- Stores all servers in a list.
- Prints an infrastructure summary.

---

# 📅 What's Next?

➡️ **Day 13 – Advanced Object-Oriented Programming & File-Based Projects**

Topics include:

- Polymorphism
- Abstraction
- Special Methods (`__str__`, `__repr__`)
- Exception Handling in OOP
- Building a Real-World CLI Application

---

## 👨‍💻 Author

**Ashish Mondal**

**40 Days Python + Bash Scripting for DevOps Challenge**

⭐ If you found this repository helpful, consider **starring** it and following the journey!
