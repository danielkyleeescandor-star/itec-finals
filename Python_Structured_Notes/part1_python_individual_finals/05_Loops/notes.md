# Loops

Loops repeat instructions. for is useful for going through a sequence or repeating a set number of times. while repeats while its condition is True.

Each example is saved separately as a `.py` file.

## Example 1: Count 1 to 5 — Easy

**Purpose:** Prints numbers using a for loop.

**Code:**

```python
for number in range(1, 6):
    print(number)
```

**Explanation:**
- `for number in range(1, 6):` — Starts a loop; indented lines repeat according to the loop.
- `print(number)` — Displays information in the terminal.

**Sample output/result:**

```text
1 2 3 4 5
```

## Example 2: Repeat a Message — Easy

**Purpose:** Prints a message five times.

**Code:**

```python
for count in range(5):
    print("Keep learning Python!")
```

**Explanation:**
- `for count in range(5):` — Starts a loop; indented lines repeat according to the loop.
- `print("Keep learning Python!")` — Displays information in the terminal.

**Sample output/result:**

```text
Message printed five times
```

## Example 3: While Counter — Easy

**Purpose:** Counts while the condition remains True.

**Code:**

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

**Explanation:**
- `count = 1` — Stores a value or calculation in a variable.
- `while count <= 5:` — Starts a loop; indented lines repeat according to the loop.
- `print(count)` — Displays information in the terminal.
- `count += 1` — Stores a value or calculation in a variable.

**Sample output/result:**

```text
1 2 3 4 5
```

## Example 4: Multiplication Table — Intermediate

**Purpose:** Displays the 4 times table.

**Code:**

```python
number = 4
for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)
```

**Explanation:**
- `number = 4` — Stores a value or calculation in a variable.
- `for multiplier in range(1, 11):` — Starts a loop; indented lines repeat according to the loop.
- `print(number, "x", multiplier, "=", number * multiplier)` — Displays information in the terminal.

**Sample output/result:**

```text
4 x 1 = 4 through 4 x 10 = 40
```

## Example 5: Sum 1 to 10 — Intermediate

**Purpose:** Adds each number to a running total.

**Code:**

```python
total = 0
for number in range(1, 11):
    total += number
print("Total:", total)
```

**Explanation:**
- `total = 0` — Stores a value or calculation in a variable.
- `for number in range(1, 11):` — Starts a loop; indented lines repeat according to the loop.
- `total += number` — Stores a value or calculation in a variable.
- `print("Total:", total)` — Displays information in the terminal.

**Sample output/result:**

```text
Total: 55
```

## Example 6: Letters in a Word — Intermediate

**Purpose:** Loops through each character in a string.

**Code:**

```python
for letter in "PYTHON":
    print(letter)
```

**Explanation:**
- `for letter in "PYTHON":` — Starts a loop; indented lines repeat according to the loop.
- `print(letter)` — Displays information in the terminal.

**Sample output/result:**

```text
P Y T H O N
```

## Example 7: Even Numbers — Hard

**Purpose:** Prints even numbers from 1 to 20.

**Code:**

```python
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
```

**Explanation:**
- `for number in range(1, 21):` — Starts a loop; indented lines repeat according to the loop.
- `if number % 2 == 0:` — Checks a condition to decide which code should run.
- `print(number)` — Displays information in the terminal.

**Sample output/result:**

```text
2 4 6 8 10 12 14 16 18 20
```

## Example 8: Number Guessing — Hard

**Purpose:** Repeats until the user enters the secret number.

**Code:**

```python
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess (1-10): "))
    if guess != secret:
        print("Try again!")
print("Correct!")
```

**Explanation:**
- `secret = 7` — Stores a value or calculation in a variable.
- `guess = 0` — Stores a value or calculation in a variable.
- `while guess != secret:` — Starts a loop; indented lines repeat according to the loop.
- `guess = int(input("Guess (1-10): "))` — Prompts the user and stores the typed response.
- `if guess != secret:` — Checks a condition to decide which code should run.
- `print("Try again!")` — Displays information in the terminal.
- `print("Correct!")` — Displays information in the terminal.

**Sample output/result:**

```text
Entering 7 displays Correct!
```
