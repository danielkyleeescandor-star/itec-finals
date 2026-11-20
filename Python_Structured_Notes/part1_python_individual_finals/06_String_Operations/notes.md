# String Operations

A string stores text. String functions and methods can count, change, combine, and split text.

Each example is saved separately as a `.py` file.

## Example 1: String Length — Easy

**Purpose:** Counts characters using len().

**Code:**

```python
message = "Hello"
print(len(message))
```

**Explanation:**
- `message = "Hello"` — Stores a value or calculation in a variable.
- `print(len(message))` — Displays information in the terminal.

**Sample output/result:**

```text
5
```

## Example 2: Uppercase — Easy

**Purpose:** Changes letters to uppercase.

**Code:**

```python
word = "python"
print(word.upper())
```

**Explanation:**
- `word = "python"` — Stores a value or calculation in a variable.
- `print(word.upper())` — Displays information in the terminal.

**Sample output/result:**

```text
PYTHON
```

## Example 3: Lowercase — Easy

**Purpose:** Changes letters to lowercase.

**Code:**

```python
word = "HELLO"
print(word.lower())
```

**Explanation:**
- `word = "HELLO"` — Stores a value or calculation in a variable.
- `print(word.lower())` — Displays information in the terminal.

**Sample output/result:**

```text
hello
```

## Example 4: Join Strings — Intermediate

**Purpose:** Combines two strings with a space.

**Code:**

```python
first = "Alex"
last = "Santos"
full = first + " " + last
print(full)
```

**Explanation:**
- `first = "Alex"` — Stores a value or calculation in a variable.
- `last = "Santos"` — Stores a value or calculation in a variable.
- `full = first + " " + last` — Stores a value or calculation in a variable.
- `print(full)` — Displays information in the terminal.

**Sample output/result:**

```text
Alex Santos
```

## Example 5: Replace Text — Intermediate

**Purpose:** Replaces a word using replace().

**Code:**

```python
sentence = "I like Java"
print(sentence.replace("Java", "Python"))
```

**Explanation:**
- `sentence = "I like Java"` — Stores a value or calculation in a variable.
- `print(sentence.replace("Java", "Python"))` — Displays information in the terminal.

**Sample output/result:**

```text
I like Python
```

## Example 6: Split Sentence — Intermediate

**Purpose:** Splits a sentence into a list of words.

**Code:**

```python
sentence = "Python is fun"
print(sentence.split())
```

**Explanation:**
- `sentence = "Python is fun"` — Stores a value or calculation in a variable.
- `print(sentence.split())` — Displays information in the terminal.

**Sample output/result:**

```text
['Python', 'is', 'fun']
```

## Example 7: Count a Letter — Hard

**Purpose:** Counts how many times a character appears.

**Code:**

```python
word = "banana"
print(word.count("a"))
```

**Explanation:**
- `word = "banana"` — Stores a value or calculation in a variable.
- `print(word.count("a"))` — Displays information in the terminal.

**Sample output/result:**

```text
3
```

## Example 8: Word Counter — Hard

**Purpose:** Counts words by splitting the entered sentence.

**Code:**

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))
```

**Explanation:**
- `sentence = input("Enter a sentence: ")` — Prompts the user and stores the typed response.
- `words = sentence.split()` — Stores a value or calculation in a variable.
- `print("Word count:", len(words))` — Displays information in the terminal.

**Sample output/result:**

```text
Input: Python is easy; Word count: 3
```
