# Functions

A function is a reusable block of code. def creates a function, parameters receive information, and return sends a result back.

Each example is saved separately as a `.py` file.

## Example 1: First Function — Easy

**Purpose:** Defines and calls a function.

**Code:**

```python
def greet():
    print("Welcome to Python!")
greet()
```

**Explanation:**
- `def greet():` — Defines a function that can be called later.
- `print("Welcome to Python!")` — Displays information in the terminal.
- `greet()` — Performs the operation shown in this statement.

**Sample output/result:**

```text
Welcome to Python!
```

## Example 2: Function with Parameter — Easy

**Purpose:** Passes a name into a function.

**Code:**

```python
def greet(name):
    print("Hello,", name)
greet("Alex")
```

**Explanation:**
- `def greet(name):` — Defines a function that can be called later.
- `print("Hello,", name)` — Displays information in the terminal.
- `greet("Alex")` — Performs the operation shown in this statement.

**Sample output/result:**

```text
Hello, Alex
```

## Example 3: Add Function — Easy

**Purpose:** Adds two numbers inside a function.

**Code:**

```python
def add(a, b):
    print("Sum:", a + b)
add(4, 6)
```

**Explanation:**
- `def add(a, b):` — Defines a function that can be called later.
- `print("Sum:", a + b)` — Displays information in the terminal.
- `add(4, 6)` — Performs the operation shown in this statement.

**Sample output/result:**

```text
Sum: 10
```

## Example 4: Return a Value — Intermediate

**Purpose:** Returns a multiplication result.

**Code:**

```python
def multiply(a, b):
    return a * b
answer = multiply(5, 3)
print(answer)
```

**Explanation:**
- `def multiply(a, b):` — Defines a function that can be called later.
- `return a * b` — Sends a result back to the code that called the function.
- `answer = multiply(5, 3)` — Stores a value or calculation in a variable.
- `print(answer)` — Displays information in the terminal.

**Sample output/result:**

```text
15
```

## Example 5: Even or Odd Function — Intermediate

**Purpose:** Returns whether a number is even or odd.

**Code:**

```python
def check_number(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
print(check_number(9))
```

**Explanation:**
- `def check_number(number):` — Defines a function that can be called later.
- `if number % 2 == 0:` — Checks a condition to decide which code should run.
- `return "Even"` — Sends a result back to the code that called the function.
- `return "Odd"` — Sends a result back to the code that called the function.
- `print(check_number(9))` — Displays information in the terminal.

**Sample output/result:**

```text
Odd
```

## Example 6: Rectangle Area Function — Intermediate

**Purpose:** Calculates area and returns it.

**Code:**

```python
def rectangle_area(length, width):
    return length * width
print(rectangle_area(8, 5))
```

**Explanation:**
- `def rectangle_area(length, width):` — Defines a function that can be called later.
- `return length * width` — Sends a result back to the code that called the function.
- `print(rectangle_area(8, 5))` — Displays information in the terminal.

**Sample output/result:**

```text
40
```

## Example 7: Average Function — Hard

**Purpose:** Calculates the average of three scores.

**Code:**

```python
def average(a, b, c):
    return (a + b + c) / 3
print(average(85, 90, 95))
```

**Explanation:**
- `def average(a, b, c):` — Defines a function that can be called later.
- `return (a + b + c) / 3` — Sends a result back to the code that called the function.
- `print(average(85, 90, 95))` — Displays information in the terminal.

**Sample output/result:**

```text
90.0
```

## Example 8: Mini Calculator Functions — Hard

**Purpose:** Uses separate functions for arithmetic operations.

**Code:**

```python
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(add(8, 2))
print(subtract(8, 2))
print(multiply(8, 2))
print(divide(8, 2))
```

**Explanation:**
- `def add(a, b):` — Defines a function that can be called later.
- `return a + b` — Sends a result back to the code that called the function.
- `def subtract(a, b):` — Defines a function that can be called later.
- `return a - b` — Sends a result back to the code that called the function.
- `def multiply(a, b):` — Defines a function that can be called later.
- `return a * b` — Sends a result back to the code that called the function.
- `def divide(a, b):` — Defines a function that can be called later.
- `if b == 0:` — Checks a condition to decide which code should run.
- `return "Cannot divide by zero"` — Sends a result back to the code that called the function.
- `return a / b` — Sends a result back to the code that called the function.
- `print(add(8, 2))` — Displays information in the terminal.
- `print(subtract(8, 2))` — Displays information in the terminal.
- `print(multiply(8, 2))` — Displays information in the terminal.
- `print(divide(8, 2))` — Displays information in the terminal.

**Sample output/result:**

```text
10; 6; 16; 4.0
```
