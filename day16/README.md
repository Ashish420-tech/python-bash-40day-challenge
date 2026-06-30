# 🚀 Day 16 - Linux Process Management & System Monitoring

> **Python + Bash Scripting for DevOps – 40 Days Challenge**

## 📌 Overview

Welcome to **Day 16** of the **Python + Bash Scripting for DevOps** challenge!

Today's focus is on **Linux Process Management and System Monitoring**, one of the most important skills for Linux Administrators, System Engineers, and DevOps Engineers.

Understanding how Linux manages processes and system resources is essential for troubleshooting production servers, optimizing performance, and ensuring application availability.

---

# 🎯 Learning Objectives

By completing this project, you will learn how to:

- Understand Linux processes and Process IDs (PID)
- Monitor running applications
- Identify CPU and memory-intensive processes
- Manage foreground and background jobs
- Terminate unresponsive processes safely
- Monitor system resources using Bash
- Access system information using Python
- Perform basic Linux performance troubleshooting

---

# 📂 Project Structure

```text
day16/
│── process_info.sh
│── process_monitor.sh
│── top_processes.sh
│── kill_process.sh
│── process_list.py
│── cpu_memory_monitor.py
└── README.md
```

---

# 📖 Topics Covered

## Linux Process Management

- Process
- PID (Process ID)
- Parent Process
- Child Process
- Process States

---

## Process Monitoring Commands

```bash
ps
ps -ef
top
htop
grep
```

---

## Process Control

```bash
kill
kill -9
jobs
bg
fg
```

---

## System Monitoring

```bash
free -h
df -h
mpstat
```

---

# 🐚 Bash Scripts

## 1️⃣ Process Information

Displays

- Current user
- Current date
- Running processes

```bash
./process_info.sh
```

---

## 2️⃣ Process Monitor

Displays

- CPU Usage
- Memory Usage

Automatically refreshes every 5 seconds.

```bash
./process_monitor.sh
```

---

## 3️⃣ Top CPU Processes

Lists the highest CPU-consuming processes.

```bash
./top_processes.sh
```

---

## 4️⃣ Kill Process

Accepts a PID and terminates the selected process.

```bash
./kill_process.sh
```

---

# 🐍 Python Programs

## process_list.py

Displays

- Current Process ID
- Parent Process ID

Run

```bash
python3 process_list.py
```

---

## cpu_memory_monitor.py

Reads Linux system information from

```
/proc/meminfo
```

Displays

- Load Average
- Memory Information

Run

```bash
python3 cpu_memory_monitor.py
```

---

# 💻 Commands Practiced

```bash
ps
ps -ef
top
htop
grep
kill
kill -9
jobs
bg
fg
free -h
df -h
mpstat
```

---

# 🧪 Practice Tasks

✔ Display all running processes

✔ Find all Python processes

✔ Find Docker processes

✔ Kill a running process

✔ Display CPU usage

✔ Display memory usage

✔ Display disk usage

✔ Create a real-time monitoring script

✔ Read Linux process information using Python

---

# 🌍 Real-World DevOps Use Cases

These skills are used daily by DevOps Engineers to:

- Monitor production Linux servers
- Identify high CPU usage
- Detect memory leaks
- Troubleshoot slow applications
- Monitor Docker containers
- Debug Kubernetes worker nodes
- Monitor Jenkins build agents
- Perform server health checks
- Investigate application failures

---

# 📚 Key Linux Concepts Learned

- Linux Processes
- PID
- Parent & Child Processes
- Foreground & Background Jobs
- Process Monitoring
- CPU Monitoring
- Memory Monitoring
- Disk Usage
- System Load
- Linux `/proc` Filesystem

---

# 🎯 Interview Questions

1. What is a Linux process?
2. What is a Process ID (PID)?
3. Difference between a process and a service?
4. How do you terminate a process?
5. What is the difference between `kill` and `kill -9`?
6. How do you monitor CPU usage?
7. How do you check memory utilization?
8. What does the `top` command display?
9. How do you identify resource-intensive processes?
10. How would you troubleshoot a Linux server with 100% CPU usage?

---

# 🛠 Technologies Used

- Linux
- Bash Shell
- Python 3
- Ubuntu
- Process Management Utilities

---

# 🎓 Learning Outcome

After completing Day 16, I can confidently:

- Monitor Linux processes
- Analyze CPU and memory utilization
- Identify performance bottlenecks
- Manage running applications
- Write Bash scripts for system monitoring
- Read Linux system information using Python
- Troubleshoot basic Linux performance issues

---

# 📸 Sample Output

```bash
Current User: ashish

Current Date:
Tue Jun 30 2026

Running Processes

UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 ?        00:00:01 systemd
ashish    2456  2410  0 pts/0    00:00:00 bash
ashish    3102  2456  0 pts/0    00:00:00 python3
```

---

# 🚀 Git Commands

```bash
git checkout -b day16

git add .

git commit -m "Day 16: Linux Process Management and System Monitoring"

git push origin day16
```

---

# 🌟 Connect With Me

### 👨‍💻 Ashish Mondal

**GitHub:** https://github.com/Ashish420-tech

Passionate about Linux, Python, Bash Scripting, Cloud, Automation, and DevOps.

---

## ⭐ If you found this project helpful, consider giving the repository a Star!
