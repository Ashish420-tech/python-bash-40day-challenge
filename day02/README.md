# Day 02 - Arithmetic Operators & Mathematical Operations

Master arithmetic operations, mathematical calculations, and numeric data manipulation in Python and Bash.

## 📚 Overview

Day 02 focuses on fundamental arithmetic operations, mathematical functions, and numeric computations essential for DevOps calculations, capacity planning, and system resource management.

---

## 📁 Files & Descriptions

### Basic Arithmetic Operations

#### **add.py**
- **Purpose**: Perform addition operation
- **Input**: Two numbers (10, 20)
- **Output**: Sum of numbers
- **DevOps Use**: Calculate total resource usage, aggregate metrics
- **Run**: `python3 add.py`
- **Expected Output**: `Addition: 30`

#### **subtract.py**
- **Purpose**: Perform subtraction operation
- **Input**: Two numbers (50, 20)
- **Output**: Difference between numbers
- **DevOps Use**: Calculate resource reduction, find delta values
- **Run**: `python3 subtract.py`
- **Expected Output**: `Subtract: 30`

#### **multiply.py**
- **Purpose**: Perform multiplication operation
- **Input**: Two numbers (5, 4)
- **Output**: Product of numbers
- **DevOps Use**: Calculate capacity (nodes × resources), scale calculations
- **Run**: `python3 multiply.py`
- **Expected Output**: `Multiply: 20`

#### **div.py**
- **Purpose**: Perform true division (returns float)
- **Input**: Two numbers (10, 3)
- **Output**: Quotient as floating-point
- **DevOps Use**: Calculate average distribution, resource per unit
- **Run**: `python3 div.py`
- **Expected Output**: `Division: 3.333...`

#### **floordiv.py**
- **Purpose**: Perform floor division (returns integer)
- **Input**: Two numbers (10, 3)
- **Output**: Quotient rounded down
- **DevOps Use**: Distribute items equally (integer-only distribution)
- **Run**: `python3 floordiv.py`
- **Expected Output**: `Floor Division: 3`

#### **modulus.py**
- **Purpose**: Perform modulo operation (remainder)
- **Input**: Two numbers
- **Output**: Remainder after division
- **DevOps Use**: Load balancing (round-robin), rotation scheduling, cycle detection
- **Run**: `python3 modulus.py`
- **Example**: Server ID = `request_id % num_servers` for round-robin

#### **power.py**
- **Purpose**: Perform exponentiation
- **Input**: Base and exponent
- **Output**: Result of base raised to power
- **DevOps Use**: Exponential growth calculations, data size predictions
- **Run**: `python3 power.py`
- **Example**: Storage growth = `initial_size * 2^years`

---

### Type Conversion & Casting

#### **typecast.py**
- **Purpose**: Convert between different data types
- **Input**: String representations of numbers
- **Operations**:
  - Convert string to integer: `int("123")`
  - Convert string to float: `float("3.14")`
  - Convert number to string: `str(42)`
- **DevOps Use**: Parse configuration values, process input from files/APIs
- **Run**: `python3 typecast.py`

#### **typecast1.py**
- **Purpose**: Advanced type casting with validation
- **Input**: Mixed data types
- **Operations**: Safe type conversion with error handling
- **DevOps Use**: Validate and convert metrics from monitoring systems
- **Run**: `python3 typecast1.py`

---

### Calculator Scripts

#### **calculator.py**
- **Purpose**: Interactive calculator supporting multiple operations
- **Operations**: +, -, *, /, //, **, %
- **Input**: User selects operation and provides numbers
- **DevOps Use**: Quick calculations for resource planning, cost estimation
- **Run**: `python3 calculator.py`
- **Interactive**: Prompts for operation and operands

#### **bashcalculator.sh**
- **Purpose**: Bash-based calculator for shell operations
- **Operations**: Basic arithmetic in shell scripts
- **DevOps Use**: Inline calculations in deployment scripts
- **Run**: `bash bashcalculator.sh`
- **Syntax**: Uses `$(( ))` for arithmetic evaluation

#### **calculate.sh**
- **Purpose**: Simple bash arithmetic
- **Operations**: Basic calculations
- **DevOps Use**: Quick math in automation scripts
- **Run**: `bash calculate.sh`

---

### Pattern Generation (ASCII Art)

#### **pyramid.py**
- **Purpose**: Generate pyramid pattern using asterisks
- **Output**: Right-aligned pyramid
- **Pattern Example**:
  ```
      *
     **
    ***
   ****
  *****
  ```
- **DevOps Use**: Test nested loop logic, visual output testing
- **Run**: `python3 pyramid.py`

#### **invertedpyramid.py**
- **Purpose**: Generate inverted pyramid pattern
- **Output**: Upside-down pyramid
- **DevOps Use**: Visualization of resource deallocation
- **Run**: `python3 invertedpyramid.py`

#### **diamond.py**
- **Purpose**: Generate diamond shape pattern
- **Output**: Diamond pattern
- **DevOps Use**: Complex iteration testing, visual alignment checks
- **Run**: `python3 diamond.py`

#### **rightanle.py**
- **Purpose**: Generate right-angled triangle
- **Output**: Right-angle triangle pattern
- **DevOps Use**: Testing loop nesting
- **Run**: `python3 rightanle.py`

#### **Invertedangled.py**
- **Purpose**: Generate inverted right-angled triangle
- **Output**: Reversed right-angle pattern
- **DevOps Use**: Pattern transformation testing
- **Run**: `python3 Invertedangled.py`

#### **hollowsquare.py**
- **Purpose**: Generate hollow square pattern
- **Output**: Square with empty interior
- **Pattern Example**:
  ```
  ****
  *  *
  *  *
  ****
  ```
- **DevOps Use**: Border-only visualization
- **Run**: `python3 hollowsquare.py`

#### **hollowtriangle.py**
- **Purpose**: Generate hollow triangle pattern
- **Output**: Triangle with empty interior
- **DevOps Use**: Hierarchical structure visualization
- **Run**: `python3 hollowtriangle.py`

---

### Number Sequences & Mathematical Patterns

#### **numbertriangle.py**
- **Purpose**: Generate triangle with sequential numbers
- **Output**: Number sequence in triangular form
- **Pattern Example**:
  ```
  1
  1 2
  1 2 3
  1 2 3 4
  ```
- **DevOps Use**: Sequence validation, iteration testing
- **Run**: `python3 numbertriangle.py`

#### **alphabet.py**
- **Purpose**: Generate triangle with alphabetic characters
- **Output**: Alphabet sequence in triangular form
- **DevOps Use**: Character handling, ASCII operations
- **Run**: `python3 alphabet.py`

#### **reversealphabet.py**
- **Purpose**: Generate reverse alphabet sequence
- **Output**: Z to A in triangular form
- **DevOps Use**: Reverse iteration testing
- **Run**: `python3 reversealphabet.py`

#### **paskaltriangle.py**
- **Purpose**: Generate Pascal's triangle
- **Output**: Mathematical Pascal's triangle pattern
- **Pattern Example**:
  ```
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
  ```
- **DevOps Use**: Mathematical sequence testing, combinatorics
- **Run**: `python3 paskaltriangle.py`

#### **folydtriangle.py**
- **Purpose**: Generate Floyd's triangle
- **Output**: Consecutive numbers in triangular form
- **Pattern Example**:
  ```
  1
  2 3
  4 5 6
  7 8 9 10
  ```
- **DevOps Use**: Number sequence validation
- **Run**: `python3 folydtriangle.py`

---

### Utility & Specialized Calculations

#### **diskcal.py**
- **Purpose**: Calculate disk space usage and availability
- **Input**: Total space, used space
- **Calculations**:
  - Available space = Total - Used
  - Usage percentage = (Used / Total) × 100
- **DevOps Use**: Storage monitoring, capacity alerts
- **Run**: `python3 diskcal.py`
- **Example Output**: Shows available space and usage percentage

#### **samenumber.py**
- **Purpose**: Compare if two numbers are equal
- **Input**: Two numbers
- **Output**: Boolean result
- **DevOps Use**: Validation checks, configuration matching
- **Run**: `python3 samenumber.py`

#### **cstyle.sh**
- **Purpose**: C-style for loop in Bash
- **Syntax**: `for ((i=0; i<10; i++))`
- **DevOps Use**: Traditional loop patterns in shell scripts
- **Run**: `bash cstyle.sh`

#### **series.sh**
- **Purpose**: Generate number series in Bash
- **Output**: Sequence of numbers
- **DevOps Use**: Generate IDs, batch operations
- **Run**: `bash series.sh`

---

### Complex Tasks & Projects

#### **task1.py**
- **Purpose**: Multi-step calculation task combining multiple operations
- **Operations**: Combines arithmetic, conditionals, and logic
- **DevOps Use**: Real-world scenario solving
- **Run**: `python3 task1.py`
- **Complexity**: Intermediate

---

## 🚀 Quick Start Commands

### Run All Python Files
```bash
cd day02
python3 add.py
python3 subtract.py
python3 multiply.py
python3 div.py
python3 floordiv.py
python3 modulus.py
python3 power.py
python3 typecast.py
python3 calculator.py
python3 pyramid.py
python3 diamond.py
```

### Run All Bash Files
```bash
cd day02
chmod +x *.sh
bash calculate.sh
bash bashcalculator.sh
bash cstyle.sh
bash series.sh
```

---

## 📊 Arithmetic Operators Reference

| Operator | Symbol | Python | Bash | Purpose |
|----------|--------|--------|------|---------|
| Addition | + | `a + b` | `$((a+b))` | Sum values |
| Subtraction | - | `a - b` | `$((a-b))` | Find difference |
| Multiplication | * | `a * b` | `$((a*b))` | Calculate product |
| Division | / | `a / b` | `$((a/b))` | Divide values |
| Floor Division | // | `a // b` | N/A | Integer division |
| Modulo | % | `a % b` | `$((a%b))` | Find remainder |
| Exponentiation | ** | `a ** b` | N/A | Power calculation |

---

## 💡 DevOps Applications

1. **Capacity Planning**
   - Calculate total resources: `servers × cores × memory`
   - Estimate storage growth: `initial_size * growth_rate^years`

2. **Load Distribution**
   - Round-robin assignment: `server_id = request_id % num_servers`
   - Equal partition: `items_per_server = total_items // num_servers`

3. **Monitoring & Alerts**
   - CPU usage: `(used_cpu / total_cpu) * 100`
   - Memory alert: `if used_memory > (total_memory * 0.8)`

4. **Cost Calculation**
   - Monthly cost: `num_instances × cost_per_instance × hours_per_month`
   - Bandwidth cost: `data_transferred_gb × cost_per_gb`

5. **Performance Metrics**
   - Response time average: `total_time / num_requests`
   - Throughput: `completed_tasks / time_period`

---

## 🔗 Related Topics

- **Day 01**: Variables (prerequisites for math operations)
- **Day 03**: Conditionals (apply math for decision-making)
- **Day 04**: Loops (repeat calculations)
- **Day 05**: File operations (process numeric data from files)

---

**Created**: 2026-06-19  
**Last Updated**: 2026-06-19  
**Difficulty Level**: Beginner  
**Time to Complete**: 1-2 hours
