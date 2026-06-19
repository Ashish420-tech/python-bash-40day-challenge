# Day 06 - Functions & Code Reusability

Day 06 covers function definition, parameters, return values, and code modularity for creating reusable automation components.

## 📚 Learning Objectives

- Master function definition and calls
- Understand parameter passing and return values
- Learn function scope and local variables
- Create modular, reusable automation scripts
- Implement best practices for function design

## 📁 Files Overview

### Python Functions

| File | Purpose | DevOps Use Case |
|------|---------|-----------------|
| **task1.py** | Basic function definition | Foundation for code organization |
| **task2.py** | Function with parameters | Pass configuration to functions |
| **task3.py** | Function with return values | Process data and return results |
| **task4.py** | Multiple functions | Complex task decomposition |

### Bash Functions

| File | Purpose | DevOps Application |
|------|---------|-------------------|
| **task1.sh** | Basic function definition | Organize deployment steps |
| **task2.sh** | Function with parameters | Parameterized configuration |
| **task3.sh** | Function with return values | Error handling and status codes |
| **task4.sh** | Multiple functions | Complex workflow orchestration |

### Advanced Scripts

| File | Purpose | Complexity |
|------|---------|-----------|
| **system_report.sh** | System information function | Advanced - real-world reporting |
| **tas3.sh** | Data processing function | Intermediate - text manipulation |

## 🚀 Quick Start

### Running Python Functions

```bash
# Basic functions
python3 day06/task1.py
python3 day06/task2.py

# Advanced functions
python3 day06/task3.py
python3 day06/task4.py
```

### Running Bash Functions

```bash
# Make scripts executable
chmod +x day06/*.sh

# Basic functions
bash day06/task1.sh
bash day06/task2.sh

# Advanced scripts
bash day06/system_report.sh
```

## 💡 Key Concepts

### Function Definition

**Python:**
```python
# Basic function
def greet(name):
    """Function documentation"""
    print(f"Hello, {name}")
    return f"Greeted {name}"

# Function call
result = greet("Alice")
print(result)
```

**Bash:**
```bash
# Basic function
greet() {
    local name=$1
    echo "Hello, $name"
    return 0
}

# Function call
greet "Alice"
```

### Parameters & Arguments

**Python:**
```python
# Positional parameters
def process(file, mode):
    pass

# Default parameters
def backup(source, dest="backup/"):
    pass

# Variable-length arguments
def log(*messages):
    for msg in messages:
        print(msg)
```

**Bash:**
```bash
# Positional parameters
process() {
    local file=$1
    local mode=$2
}

# Named parameters
deploy() {
    local -r server="$1"
    local -r version="$2"
}

# All arguments
process_all() {
    for arg in "$@"; do
        echo "$arg"
    done
}
```

### Return Values

**Python:**
```python
def divide(a, b):
    if b == 0:
        return None
    return a / b

result = divide(10, 2)
```

**Bash:**
```bash
# Exit status (0 = success, non-zero = failure)
check_file() {
    if [ -f "$1" ]; then
        return 0  # Success
    else
        return 1  # Failure
    fi
}

if check_file "config.conf"; then
    echo "File found"
fi
```

### Function Scope

**Python:**
```python
global_var = "global"

def test():
    local_var = "local"
    global global_var
    global_var = "modified"
    print(local_var, global_var)

test()
```

**Bash:**
```bash
global_var="global"

test() {
    local local_var="local"
    global_var="modified"
    echo "$local_var $global_var"
}

test
```

## 📊 Common DevOps Function Patterns

### 1. Logging Function

```bash
log() {
    local level=$1
    shift
    local message="$@"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $message" | tee -a app.log
}

log "INFO" "Deployment started"
log "ERROR" "Connection failed"
```

### 2. Error Handling Function

```bash
check_status() {
    if [ $? -ne 0 ]; then
        echo "ERROR: Previous command failed"
        exit 1
    fi
}

run_command() {
    "$@"
    check_status
}
```

### 3. Configuration Validation

```python
def validate_config(config):
    """Validate configuration parameters"""
    required = ['host', 'port', 'username']
    for key in required:
        if key not in config:
            return False, f"Missing: {key}"
    return True, "Valid"
```

### 4. Health Check Function

```bash
check_service() {
    local service=$1
    
    if systemctl is-active --quiet "$service"; then
        return 0
    else
        echo "Service $service is down"
        return 1
    fi
}

# Usage
for svc in nginx mysql redis; do
    check_service "$svc" || echo "Starting $svc"
done
```

### 5. Retry Mechanism

```bash
retry() {
    local max_attempts=$1
    shift
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        if "$@"; then
            return 0
        fi
        echo "Attempt $attempt failed, retrying..."
        ((attempt++))
        sleep 2
    done
    
    return 1
}

# Usage
retry 3 curl -f https://api.example.com/health
```

## 📋 Real-World DevOps Example

### System Report Script

```bash
#!/bin/bash

# Get system CPU usage
get_cpu_usage() {
    top -bn1 | grep "Cpu(s)" | awk '{print $2}'
}

# Get memory usage
get_memory_usage() {
    free | grep Mem | awk '{printf("%.2f", $3/$2 * 100.0)}'
}

# Get disk usage
get_disk_usage() {
    df / | awk 'NR==2 {printf("%.2f", $3/$2 * 100.0)}'
}

# Generate report
generate_report() {
    echo "=== System Report $(date) ==="
    echo "CPU Usage: $(get_cpu_usage)%"
    echo "Memory Usage: $(get_memory_usage)%"
    echo "Disk Usage: $(get_disk_usage)%"
}

generate_report
```

## 📝 DevOps Applications

1. **Deployment Orchestration**: Functions for each deployment step
2. **Health Monitoring**: Reusable health check functions
3. **Configuration Management**: Functions to validate and apply configs
4. **Backup & Recovery**: Modular backup and restore functions
5. **Log Analysis**: Functions to parse and analyze logs
6. **Service Management**: Functions to manage services
7. **Error Handling**: Centralized error handling functions
8. **Reporting**: Functions to generate various reports

## Best Practices

### Python Functions

1. **Use docstrings**: Document function purpose and parameters
   ```python
   def deploy(service, version):
       """Deploy service to specific version.
       
       Args:
           service: Service name
           version: Version to deploy
       """
   ```

2. **Type hints**: Add parameter and return type annotations
   ```python
   def process(data: list) -> dict:
       pass
   ```

3. **Error handling**: Use try-except blocks
   ```python
   try:
       result = operation()
   except Exception as e:
       log.error(f"Operation failed: {e}")
   ```

### Bash Functions

1. **Use local variables**: Prevent scope pollution
   ```bash
   func() {
       local var="value"
   }
   ```

2. **Check parameters**: Validate inputs
   ```bash
   func() {
       if [ $# -lt 2 ]; then
           echo "Usage: func arg1 arg2"
           return 1
       fi
   }
   ```

3. **Return meaningful codes**: Use exit codes for status
   ```bash
   if func; then
       echo "Success"
   else
       echo "Failed"
   fi
   ```

## 🔗 Related Days

- **Day 01-05**: Foundation for function usage
- **Day 07**: Advanced functions and libraries

---

**Created**: 2026-06-19  
**Category**: Functions & Modularity  
**Difficulty**: Intermediate
