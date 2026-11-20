# Conditional Statements

if, elif, and else allow a program to make decisions based on conditions.

Each example is saved separately as a `.py` file.

## Example 1: Positive Number — Easy

**Purpose:** Checks whether a number is greater than zero.

**Code:**

```python
number = 8
if number > 0:
    print("Positive")
```

**Explanation:**
- `number = 8` — Stores a value or calculation in a variable.
- `if number > 0:` — Checks a condition to decide which code should run.
- `print("Positive")` — Displays information in the terminal.

**Sample output/result:**

```text
Positive
```

## Example 2: Even or Odd — Easy

**Purpose:** Uses the remainder to identify an even or odd number.

**Code:**

```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Explanation:**
- `number = 7` — Stores a value or calculation in a variable.
- `if number % 2 == 0:` — Checks a condition to decide which code should run.
- `print("Even")` — Displays information in the terminal.
- `else:` — Checks a condition to decide which code should run.
- `print("Odd")` — Displays information in the terminal.

**Sample output/result:**

```text
Odd
```

## Example 3: Pass or Fail — Easy

**Purpose:** Checks if a score is at least 75.

**Code:**

```python
score = 82
if score >= 75:
    print("Passed")
else:
    print("Failed")
```

**Explanation:**
- `score = 82` — Stores a value or calculation in a variable.
- `if score >= 75:` — Checks a condition to decide which code should run.
- `print("Passed")` — Displays information in the terminal.
- `else:` — Checks a condition to decide which code should run.
- `print("Failed")` — Displays information in the terminal.

**Sample output/result:**

```text
Passed
```

## Example 4: Grade Description — Intermediate

**Purpose:** Uses elif to select a score description.

**Code:**

```python
score = 91
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Very Good")
elif score >= 75:
    print("Passed")
else:
    print("Failed")
```

**Explanation:**
- `score = 91` — Stores a value or calculation in a variable.
- `if score >= 90:` — Checks a condition to decide which code should run.
- `print("Excellent")` — Displays information in the terminal.
- `elif score >= 80:` — Checks a condition to decide which code should run.
- `print("Very Good")` — Displays information in the terminal.
- `elif score >= 75:` — Checks a condition to decide which code should run.
- `print("Passed")` — Displays information in the terminal.
- `else:` — Checks a condition to decide which code should run.
- `print("Failed")` — Displays information in the terminal.

**Sample output/result:**

```text
Excellent
```

## Example 5: Age Category — Intermediate

**Purpose:** Classifies an age using several conditions.

**Code:**

```python
age = 17
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

**Explanation:**
- `age = 17` — Stores a value or calculation in a variable.
- `if age < 13:` — Checks a condition to decide which code should run.
- `print("Child")` — Displays information in the terminal.
- `elif age < 20:` — Checks a condition to decide which code should run.
- `print("Teenager")` — Displays information in the terminal.
- `else:` — Checks a condition to decide which code should run.
- `print("Adult")` — Displays information in the terminal.

**Sample output/result:**

```text
Teenager
```

## Example 6: Basic Login Check — Intermediate

**Purpose:** Compares entered text with sample credentials; this is not secure authentication.

**Code:**

```python
correct_user = "student"
correct_pass = "python123"
user = input("Username: ")
password = input("Password: ")
if user == correct_user and password == correct_pass:
    print("Login successful")
else:
    print("Incorrect details")
```

**Explanation:**
- `correct_user = "student"` — Stores a value or calculation in a variable.
- `correct_pass = "python123"` — Stores a value or calculation in a variable.
- `user = input("Username: ")` — Prompts the user and stores the typed response.
- `password = input("Password: ")` — Prompts the user and stores the typed response.
- `if user == correct_user and password == correct_pass:` — Checks a condition to decide which code should run.
- `print("Login successful")` — Displays information in the terminal.
- `else:` — Checks a condition to decide which code should run.
- `print("Incorrect details")` — Displays information in the terminal.

**Sample output/result:**

```text
Matching entries: Login successful
```

## Example 7: Largest Number — Hard

**Purpose:** Finds the larger of two numbers or reports a tie.

**Code:**

```python
a = 15
b = 20
if a > b:
    print("A is larger")
elif b > a:
    print("B is larger")
else:
    print("Equal")
```

**Explanation:**
- `a = 15` — Stores a value or calculation in a variable.
- `b = 20` — Stores a value or calculation in a variable.
- `if a > b:` — Checks a condition to decide which code should run.
- `print("A is larger")` — Displays information in the terminal.
- `elif b > a:` — Checks a condition to decide which code should run.
- `print("B is larger")` — Displays information in the terminal.
- `else:` — Checks a condition to decide which code should run.
- `print("Equal")` — Displays information in the terminal.

**Sample output/result:**

```text
B is larger
```

## Example 8: Sample Electricity Bill — Hard

**Purpose:** Selects a sample rate and calculates a bill.

**Code:**

```python
units = 120
if units <= 100:
    rate = 5
else:
    rate = 7
bill = units * rate
print("Bill:", bill)
```

**Explanation:**
- `units = 120` — Stores a value or calculation in a variable.
- `if units <= 100:` — Checks a condition to decide which code should run.
- `rate = 5` — Stores a value or calculation in a variable.
- `else:` — Checks a condition to decide which code should run.
- `rate = 7` — Stores a value or calculation in a variable.
- `bill = units * rate` — Stores a value or calculation in a variable.
- `print("Bill:", bill)` — Displays information in the terminal.

**Sample output/result:**

```text
Bill: 840
```
