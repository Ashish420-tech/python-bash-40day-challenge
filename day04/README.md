# Day 04 - Loops & Iteration

Master loop constructs, iteration patterns, and batch processing for automation and data processing.

## 📚 Overview

Day 04 focuses on for loops, while loops, and iteration techniques for processing sequences, files, and ranges - fundamental for DevOps automation tasks like batch operations and monitoring.

---

## 📁 Python Loop Files

### Basic Loop Structures

#### **for_loop.py**
- **Purpose**: Iterate over a sequence/list
- **Pattern**: Loop through each item in a collection
- **Input**: List of items
- **Output**: Print each item
- **DevOps Use**: Process list of servers, users, or configuration items
- **Run**: `python3 for_loop.py`
- **Code Example**:
  ```python
  for item in items_list:
      print(item)
  ```

#### **while_loop.py**
- **Purpose**: Repeat block while condition is true
- **Pattern**: Condition-based iteration
- **Exit**: When condition becomes false
- **DevOps Use**: Retry logic, health check loops, monitoring
- **Run**: `python3 while_loop.py`
- **Code Example**:
  ```python
  while condition:
      perform_action()
      counter += 1
  ```

#### **range_for.py**
- **Purpose**: Generate numeric sequence and iterate
- **Function**: `range(start, end, step)`
- **Input**: Range parameters
- **Output**: Numbers in range
- **DevOps Use**: Generate IDs, iterate N times, scheduling
- **Run**: `python3 range_for.py`
- **Common Patterns**:
  ```python
  for i in range(5):        # 0, 1, 2, 3, 4
      print(i)
  
  for i in range(1, 6):     # 1, 2, 3, 4, 5
      print(i)
  
  for i in range(0, 10, 2): # 0, 2, 4, 6, 8
      print(i)
  ```

---

### Advanced Iteration

#### **enumerate.py**
- **Purpose**: Get both index and value during iteration
- **Function**: `enumerate(sequence)`
- **Output**: (index, value) tuples
- **DevOps Use**: Track item position, numbered logging
- **Run**: `python3 enumerate.py`
- **Code Example**:
  ```python
  for index, item in enumerate(items):
      print(f"Item {index}: {item}")
  ```

#### **loop_dir.py**
- **Purpose**: Iterate through directory files
- **Module**: `os` module
- **Operation**: List and process files
- **DevOps Use**: Batch file processing, directory scanning
- **Run**: `python3 loop_dir.py`
- **Code Example**:
  ```python
  import os
  for file in os.listdir(directory):
      print(file)
  ```

---

### File Processing

#### **read_file.py**
- **Purpose**: Read and iterate through file lines
- **Operation**: Process each line
- **Input**: Text file
- **Output**: Processed lines
- **DevOps Use**: Log analysis, configuration parsing
- **Run**: `python3 read_file.py`
- **Code Example**:
  ```python
  with open('file.txt', 'r') as f:
      for line in f:
          print(line.strip())
  ```

#### **task2.py**
- **Purpose**: Complex iteration task
- **Operations**: Nested loops, conditionals
- **Difficulty**: Intermediate
- **Run**: `python3 task2.py`

---

## 📁 Bash Loop Files

### Basic Loop Structures

#### **for_loop.sh**
- **Purpose**: Iterate over list of items
- **Syntax**: `for item in list`
- **Input**: List of values
- **Output**: Print each item
- **DevOps Use**: Process server names, users, files
- **Run**: `bash for_loop.sh`
- **Code Pattern**:
  ```bash
  for item in item1 item2 item3
  do
      echo $item
  done
  ```

#### **while_loop.sh**
- **Purpose**: Repeat while condition is true
- **Syntax**: `while [ condition ]`
- **Exit**: When condition becomes false
- **DevOps Use**: Retry mechanisms, monitoring loops
- **Run**: `bash while_loop.sh`
- **Code Pattern**:
  ```bash
  while [ $counter -lt 10 ]
  do
      echo $counter
      ((counter++))
  done
  ```

#### **cstyle.sh**
- **Purpose**: C-style for loop
- **Syntax**: `for ((init; condition; increment))`
- **Benefit**: Traditional loop familiar to C programmers
- **DevOps Use**: When traditional loop style is needed
- **Run**: `bash cstyle.sh`
- **Code Pattern**:
  ```bash
  for ((i=0; i<5; i++))
  do
      echo $i
  done
  ```

---

### Range & Sequence Generation

#### **series.sh**
- **Purpose**: Generate numeric sequence
- **Function**: `seq start end [step]`
- **Output**: Number series
- **DevOps Use**: Generate batch IDs, iteration counts
- **Run**: `bash series.sh`
- **Examples**:
  ```bash
  seq 1 5           # 1 2 3 4 5
  seq 1 2 10        # 1 3 5 7 9
  seq -w 01 05      # 01 02 03 04 05
  ```

---

### File Processing

#### **loop_files.sh**
- **Purpose**: Iterate through files in directory
- **Pattern**: Glob expansion
- **Input**: File pattern
- **Output**: Process each file
- **DevOps Use**: Batch file processing, log rotation
- **Run**: `bash loop_files.sh`
- **Code Pattern**:
  ```bash
  for file in *.txt
  do
      echo "Processing $file"
  done
  ```

#### **read_file.sh**
- **Purpose**: Read file line by line
- **Method**: `while read` loop
- **Input**: File path
- **Output**: Processed lines
- **DevOps Use**: Parse logs, configuration files
- **Run**: `bash read_file.sh`
- **Code Pattern**:
  ```bash
  while IFS= read -r line
  do
      echo "$line"
  done < file.txt
  ```

#### **file_print.sh**
- **Purpose**: Advanced file printing with formatting
- **Operations**: Read, format, display
- **DevOps Use**: Log formatting, report generation
- **Run**: `bash file_print.sh`

#### **count_file.sh**
- **Purpose**: Count lines in file
- **Method**: Combination of `wc` and loops
- **Output**: Line count and statistics
- **DevOps Use**: Log size analysis, data validation
- **Run**: `bash count_file.sh`

---

### Number Filtering

#### **even.sh**
- **Purpose**: Filter and display even numbers
- **Logic**: `number % 2 == 0`
- **Output**: Even numbers from range
- **DevOps Use**: Load balancing, round-robin distribution
- **Run**: `bash even.sh`
- **Example Output**: 2, 4, 6, 8, 10...

#### **odd.sh**
- **Purpose**: Filter and display odd numbers
- **Logic**: `number % 2 != 0`
- **Output**: Odd numbers from range
- **DevOps Use**: Scheduling alternating tasks
- **Run**: `bash odd.sh`
- **Example Output**: 1, 3, 5, 7, 9...

---

### Advanced Tasks

#### **task1.sh**
- **Purpose**: Complex loop iteration task
- **Operations**: Nested loops, conditionals, file processing
- **Difficulty**: Intermediate
- **DevOps Use**: Real-world automation scenarios
- **Run**: `bash task1.sh`

---

## 📁 Test Data Files

#### **names.txt**
- **Purpose**: Sample data for file loop exercises
- **Contents**: List of names
- **Usage**: Test file reading and iteration
- **Run**: Used by read_file scripts

#### **hi.txt, hi1.txt, hi2.txt, hi3.txt**
- **Purpose**: Multiple test files
- **Usage**: Practice batch file processing
- **Run**: Used by loop_files.sh

#### **backup/ Directory**
- **Purpose**: Directory for backup operations
- **Usage**: Test directory iteration and file operations

---

## 🚀 Quick Start Commands

### Run All Python Loops
```bash
cd day04
python3 for_loop.py
python3 while_loop.py
python3 range_for.py
python3 enumerate.py
python3 loop_dir.py
python3 read_file.py
python3 task2.py
```

### Run All Bash Loops
```bash
cd day04
chmod +x *.sh
bash for_loop.sh
bash while_loop.sh
bash cstyle.sh
bash series.sh
bash loop_files.sh
bash read_file.sh
bash file_print.sh
bash count_file.sh
bash even.sh
bash odd.sh
bash task1.sh
```

---

## 📊 Loop Types Reference

### Python Loops

| Type | Syntax | Use Case |
|------|--------|----------|
| For Loop | `for item in list:` | Iterate over sequence |
| While Loop | `while condition:` | Repeat until condition false |
| Range Loop | `for i in range(n):` | Generate numeric sequence |
| Enumerate | `for i, v in enumerate(list):` | Get index and value |

### Bash Loops

| Type | Syntax | Use Case |
|------|--------|----------|
| For Loop | `for item in list; do` | Iterate over items |
| While Loop | `while [ cond ]; do` | Repeat until condition false |
| C-style For | `for ((i=0; i<n; i++)); do` | Traditional numeric loop |

---

## 💡 Loop Control Statements

### Python

```python
# Skip to next iteration
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    print(i)

# Exit loop immediately
for i in range(10):
    if i == 5:
        break     # Exit loop
    print(i)
```

### Bash

```bash
# Skip to next iteration
for i in {1..10}; do
    if [ $i -eq 3 ]; then
        continue  # Skip this iteration
    fi
    echo $i
done

# Exit loop immediately
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break     # Exit loop
    fi
    echo $i
done
```

---

## 💡 DevOps Applications

### 1. Process Multiple Servers
```bash
for server in web1 web2 web3 db1 db2; do
    echo "Deploying to $server"
    ssh "$server" "bash /opt/deploy.sh"
done
```

### 2. Health Check Loop
```bash
for i in {1..5}; do
    if curl -f http://localhost:8080/health
    then
        echo "Service healthy"
        break
    else
        echo "Attempt $i failed"
        sleep 2
    fi
done
```

### 3. Log Analysis
```bash
while IFS= read -r line; do
    if [[ "$line" == *"ERROR"* ]]; then
        echo "Error found: $line"
    fi
done < /var/log/app.log
```

### 4. Batch Configuration
```python
for server in servers_list:
    for config_file in config_files:
        apply_config(server, config_file)
```

### 5. Retry Mechanism
```bash
attempt=0
while [ $attempt -lt 3 ]; do
    if perform_operation; then
        echo "Success"
        break
    fi
    ((attempt++))
    sleep 5
done
```

---

## 📈 Performance Considerations

1. **Stream Processing**: Use `while read` for large files instead of reading all at once
2. **Efficiency**: Use `seq` instead of Python range for shell scripts
3. **Break Early**: Use `break` to exit loops as soon as goal is achieved
4. **Avoid Nested Loops**: When possible, use single pass iteration
5. **Parallel Processing**: Use `xargs -P` for parallel file processing

---

## 🔗 Related Topics

- **Day 03**: Conditionals (used inside loops for control)
- **Day 05**: File operations (process files with loops)
- **Day 06**: Functions (encapsulate loop logic)

---

**Created**: 2026-06-19  
**Last Updated**: 2026-06-19  
**Difficulty Level**: Beginner to Intermediate  
**Time to Complete**: 2-3 hours
