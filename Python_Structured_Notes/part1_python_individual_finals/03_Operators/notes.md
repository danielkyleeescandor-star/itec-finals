# Operators

Operators perform calculations and comparisons. Arithmetic operators include +, -, *, /, and %. Comparison operators return True or False. Logical operators include and, or, and not.

Each example is saved separately as a `.py` file.

## Example 1: Addition — Easy

**Purpose:** Adds two values.

**Code:**

```python
a = 10
b = 5
print(a + b)
```

**Explanation:**
- `a = 10` — Stores a value or calculation in a variable.
- `b = 5` — Stores a value or calculation in a variable.
- `print(a + b)` — Displays information in the terminal.

**Sample output/result:**

```text
15
```

## Example 2: Subtraction — Easy

**Purpose:** Subtracts one value from another.

**Code:**

```python
a = 10
b = 5
print(a - b)
```

**Explanation:**
- `a = 10` — Stores a value or calculation in a variable.
- `b = 5` — Stores a value or calculation in a variable.
- `print(a - b)` — Displays information in the terminal.

**Sample output/result:**

```text
5
```

## Example 3: Multiply and Divide — Easy

**Purpose:** Multiplies and divides numbers.

**Code:**

```python
a = 12
b = 3
print(a * b)
print(a / b)
```

**Explanation:**
- `a = 12` — Stores a value or calculation in a variable.
- `b = 3` — Stores a value or calculation in a variable.
- `print(a * b)` — Displays information in the terminal.
- `print(a / b)` — Displays information in the terminal.

**Sample output/result:**

```text
36; 4.0
```

## Example 4: Remainder — Intermediate

**Purpose:** The modulo operator gives the remainder.

**Code:**

```python
print(17 % 5)
```

**Explanation:**
- `print(17 % 5)` — Displays information in the terminal.

**Sample output/result:**

```text
2
```

## Example 5: Comparisons — Intermediate

**Purpose:** Compares values using >, ==, and !=.

**Code:**

```python
a = 10
b = 7
print(a > b)
print(a == b)
print(a != b)
```

**Explanation:**
- `a = 10` — Stores a value or calculation in a variable.
- `b = 7` — Stores a value or calculation in a variable.
- `print(a > b)` — Displays information in the terminal.
- `print(a == b)` — Displays information in the terminal.
- `print(a != b)` — Displays information in the terminal.

**Sample output/result:**

```text
True; False; True
```

## Example 6: Logical Operators — Intermediate

**Purpose:** Combines or reverses conditions.

**Code:**

```python
age = 18
has_id = True
print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

**Explanation:**
- `age = 18` — Stores a value or calculation in a variable.
- `has_id = True` — Stores a value or calculation in a variable.
- `print(age >= 18 and has_id)` — Displays information in the terminal.
- `print(age < 18 or has_id)` — Displays information in the terminal.
- `print(not has_id)` — Displays information in the terminal.

**Sample output/result:**

```text
True; True; False
```

## Example 7: Assignment Operators — Intermediate

**Purpose:** Updates a variable using += and *=.

**Code:**

```python
points = 10
points += 5
points *= 2
print(points)
```

**Explanation:**
- `points = 10` — Stores a value or calculation in a variable.
- `points += 5` — Stores a value or calculation in a variable.
- `points *= 2` — Stores a value or calculation in a variable.
- `print(points)` — Displays information in the terminal.

**Sample output/result:**

```text
30
```

## Example 8: Discount Calculator — Hard

**Purpose:** Calculates a subtotal, discount, and final cost.

**Code:**

```python
price = 500
quantity = 2
discount_rate = 0.10
subtotal = price * quantity
discount = subtotal * discount_rate
total = subtotal - discount
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final:", total)
```

**Explanation:**
- `price = 500` — Stores a value or calculation in a variable.
- `quantity = 2` — Stores a value or calculation in a variable.
- `discount_rate = 0.10` — Stores a value or calculation in a variable.
- `subtotal = price * quantity` — Stores a value or calculation in a variable.
- `discount = subtotal * discount_rate` — Stores a value or calculation in a variable.
- `total = subtotal - discount` — Stores a value or calculation in a variable.
- `print("Subtotal:", subtotal)` — Displays information in the terminal.
- `print("Discount:", discount)` — Displays information in the terminal.
- `print("Final:", total)` — Displays information in the terminal.

**Sample output/result:**

```text
Subtotal: 1000; Discount: 100.0; Final: 900.0
```
