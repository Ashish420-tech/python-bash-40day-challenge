# Day 05 - File Operations & Text Processing

Day 05 focuses on file handling, text processing, and data manipulation in both Python and Bash, essential for DevOps automation.

## 📚 Learning Objectives

- Master file read/write operations
- Understand text processing and manipulation
- Learn file system operations
- Implement data extraction and transformation
- Create file-based automation scripts

## 📁 Files Overview

### Python File Operations

| File | Purpose | DevOps Use Case |
|------|---------|-----------------|
| **tas1.py** | Basic file reading | Parse configuration files |
| **tas2.py** | String manipulation | Format output for reports |
| **tas3.py** | List operations | Aggregate data from files |
| **tas4.py** | File validation | Check file integrity |
| **tas5.py** | Line counting | Count entries in logs |
| **tas6.py** | Content filtering | Extract specific data |
| **tas7.py** | Line manipulation | Transform log entries |
| **tas8.py** | Data parsing | Extract structured data |
| **tas9.py** | Complex filtering | Multi-condition data extraction |
| **tas10.py** | Advanced processing | Complex text transformation |
| **tas11.py** | Comprehensive task | Real-world file processing scenario |

### Bash File Operations

| File | Purpose | DevOps Application |
|------|---------|-------------------|
| **task1.sh** | File existence check | Pre-deployment validation |
| **task2.sh** | File creation | Generate logs and reports |
| **task3.sh** | File copying | Backup operations |
| **task4.sh** | Content appending | Log aggregation |
| **task5.sh** | Line extraction | Filter relevant log entries |
| **task6.sh** | String replacement | Configuration updates |
| **task7.sh** | Permission management | Security configuration |
| **task8.sh** | Directory operations | File organization |
| **task9.sh** | Advanced processing | Complex file manipulation |
| **task10.sh** | Batch operations | Process multiple files |
| **task11.sh** | Data extraction | Parse structured data |
| **task12.sh** | Text search | Find patterns in files |
| **task13.sh** | Content sorting | Order log entries |
| **task14.sh** | Statistics | Count occurrences |
| **task15.sh** | File merging | Combine multiple files |
| **task16.sh** | Filtering | Select specific entries |
| **task17.sh** | Transformation | Convert data format |
| **filetest.sh** | File validation | Check file properties |

### Advanced Processing

| File | Purpose | Use Case |
|------|---------|----------|
| **employee_report.sh** | Generate employee reports | HR data processing |
| **backup.sh** | Backup operations | System backup automation |

### Data Files

| File | Purpose |
|------|---------|
| **names.txt** | Employee names list |
| **employee.txt** | Employee data |
| **report.txt** | Sample report output |
| **backup.log** | Backup operation log |
| **employee_link** | Symbolic link to employee data |

## 🚀 Quick Start

### Running Python File Operations

```bash
# Basic file operations
python3 day05/tas1.py

# Text processing
python3 day05/tas2.py
python3 day05/tas3.py

# Advanced processing
python3 day05/tas11.py
```

### Running Bash File Operations

```bash
# Make scripts executable
chmod +x day05/*.sh

# Basic operations
bash day05/task1.sh

# File processing
bash day05/filetest.sh
bash day05/employee_report.sh

# Advanced tasks
bash day05/task9.sh
bash day05/task11.sh
```

## 💡 Key Concepts

### File Reading

**Python:**
```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

**Bash:**
```bash
# Read entire file
cat file.txt

# Read line by line
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Using grep
grep "pattern" file.txt
```

### File Writing

**Python:**
```python
# Write to file
with open('file.txt', 'w') as f:
    f.write("content")

# Append to file
with open('file.txt', 'a') as f:
    f.write("new line\n")
```

**Bash:**
```bash
# Write to file
echo "content" > file.txt

# Append to file
echo "new line" >> file.txt
```

### Text Processing Commands (Bash)

| Command | Purpose | Example |
|---------|---------|---------|
| `grep` | Find pattern | `grep "error" log.txt` |
| `sed` | Stream editor | `sed 's/old/new/g' file.txt` |
| `awk` | Text processor | `awk '{print $1}' file.txt` |
| `cut` | Extract columns | `cut -d: -f1 /etc/passwd` |
| `sort` | Sort lines | `sort file.txt` |
| `uniq` | Remove duplicates | `uniq file.txt` |
| `wc` | Count lines/words | `wc -l file.txt` |
| `tr` | Translate characters | `tr 'a-z' 'A-Z' < file.txt` |

## 📊 Common DevOps Patterns

### 1. Log File Analysis

```bash
# Find errors in logs
grep -i "error" /var/log/app.log | wc -l

# Extract timestamp and error message
grep "ERROR" /var/log/app.log | awk '{print $1, $2, $NF}'
```

### 2. Configuration File Updates

```bash
# Update configuration value
sed -i 's/^TIMEOUT=.*/TIMEOUT=30/' config.conf

# Replace all occurrences
sed -i 's/old_value/new_value/g' settings.txt
```

### 3. Backup Operations

```bash
# Create backup with timestamp
cp important.conf "important.conf.$(date +%Y%m%d)"

# Backup directory
tar -czf backup_$(date +%Y%m%d).tar.gz /home/data/
```

### 4. Report Generation

```python
# Parse and generate report
with open('access.log', 'r') as f:
    requests = [line for line in f if '200' in line]
print(f"Successful requests: {len(requests)}")
```

### 5. Data Extraction

```bash
# Extract IP addresses from logs
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# Get unique users
cut -d: -f1 /etc/passwd | sort
```

## 🔒 File Permissions in DevOps

```bash
# Check file permissions
ls -l file.txt

# Change permissions
chmod 644 config.conf      # rw-r--r--
chmod 755 script.sh        # rwxr-xr-x
chmod 600 secrets.conf     # rw-------

# Change ownership
chown user:group file.txt
```

## 📝 DevOps Applications

1. **Log Analysis**: Parse and analyze system/application logs
2. **Configuration Management**: Read, update, and backup config files
3. **Data Processing**: Extract and transform data from multiple sources
4. **Reporting**: Generate operational reports from logs/metrics
5. **Backup & Recovery**: Automated backup operations with versioning
6. **Security Scanning**: Search for suspicious patterns in logs
7. **Audit Trails**: Maintain records of system changes
8. **Data Migration**: Move and transform data between systems

## Performance Optimization

1. **Stream processing**: Use `sed`/`awk` for large files instead of Python
2. **Grep efficiency**: Use `-F` for fixed strings (faster than regex)
3. **Parallel processing**: Use `xargs -P` for multiple file processing
4. **Memory**: Process large files line-by-line, not all at once
5. **Compression**: Use gzip for log backup to save storage

## 🔗 Related Days

- **Day 04**: Loops (iterate through file lines)
- **Day 03**: Conditionals (filter file content)
- **Day 06**: Functions (reusable file operations)

---

**Created**: 2026-06-19  
**Category**: File Operations  
**Difficulty**: Intermediate-Advanced
