# Basic File Handling

File handling saves information to and reads information from files. Common modes are w (write/replace), r (read), and a (append). with open(...) closes the file automatically.

Each example is saved separately as a `.py` file.

## Example 1: Create a File — Easy

**Purpose:** Creates a text file in write mode.

**Code:**

```python
with open("sample.txt", "w") as file:
    file.write("My first Python file.")
print("File created.")
```

**Explanation:**
- `with open("sample.txt", "w") as file:` — Opens a file using the specified file mode.
- `file.write("My first Python file.")` — Writes text into the opened file.
- `print("File created.")` — Displays information in the terminal.

**Sample output/result:**

```text
File created. A sample.txt file is created.
```

## Example 2: Write Text — Easy

**Purpose:** Writes two lines to a file.

**Code:**

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python\n")
    file.write("Practicing file handling\n")
print("Text saved.")
```

**Explanation:**
- `with open("notes.txt", "w") as file:` — Opens a file using the specified file mode.
- `file.write("Learning Python\n")` — Writes text into the opened file.
- `file.write("Practicing file handling\n")` — Writes text into the opened file.
- `print("Text saved.")` — Displays information in the terminal.

**Sample output/result:**

```text
Text saved.
```

## Example 3: Read Text — Easy

**Purpose:** Reads and displays the contents of a file. Run Example 2 first.

**Code:**

```python
with open("notes.txt", "r") as file:
    content = file.read()
print(content)
```

**Explanation:**
- `with open("notes.txt", "r") as file:` — Opens a file using the specified file mode.
- `content = file.read()` — Stores a value or calculation in a variable.
- `print(content)` — Displays information in the terminal.

**Sample output/result:**

```text
Learning Python; Practicing file handling
```

## Example 4: Append Text — Intermediate

**Purpose:** Adds a line without replacing existing file contents.

**Code:**

```python
with open("notes.txt", "a") as file:
    file.write("New line added.\n")
print("Text appended.")
```

**Explanation:**
- `with open("notes.txt", "a") as file:` — Opens a file using the specified file mode.
- `file.write("New line added.\n")` — Writes text into the opened file.
- `print("Text appended.")` — Displays information in the terminal.

**Sample output/result:**

```text
Text appended.
```

## Example 5: Read First Line — Intermediate

**Purpose:** Reads only the first line of a file.

**Code:**

```python
with open("notes.txt", "r") as file:
    first_line = file.readline()
print(first_line)
```

**Explanation:**
- `with open("notes.txt", "r") as file:` — Opens a file using the specified file mode.
- `first_line = file.readline()` — Stores a value or calculation in a variable.
- `print(first_line)` — Displays information in the terminal.

**Sample output/result:**

```text
Learning Python (after Example 2)
```

## Example 6: Count File Lines — Intermediate

**Purpose:** Reads all lines and counts them.

**Code:**

```python
with open("notes.txt", "r") as file:
    lines = file.readlines()
print("Line count:", len(lines))
```

**Explanation:**
- `with open("notes.txt", "r") as file:` — Opens a file using the specified file mode.
- `lines = file.readlines()` — Stores a value or calculation in a variable.
- `print("Line count:", len(lines))` — Displays information in the terminal.

**Sample output/result:**

```text
Line count depends on the file contents.
```

## Example 7: Save Student Details — Hard

**Purpose:** Saves user-entered information into a file.

**Code:**

```python
name = input("Name: ")
course = input("Course: ")
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Course: " + course + "\n")
print("Information saved.")
```

**Explanation:**
- `name = input("Name: ")` — Prompts the user and stores the typed response.
- `course = input("Course: ")` — Prompts the user and stores the typed response.
- `with open("student.txt", "w") as file:` — Opens a file using the specified file mode.
- `file.write("Name: " + name + "\n")` — Writes text into the opened file.
- `file.write("Course: " + course + "\n")` — Writes text into the opened file.
- `print("Information saved.")` — Displays information in the terminal.

**Sample output/result:**

```text
Sample inputs Alex and BSIT: Information saved.
```

## Example 8: Simple Notes Program — Hard

**Purpose:** Appends a note, then reads and displays all saved notes.

**Code:**

```python
note = input("Write a note: ")
with open("my_notes.txt", "a") as file:
    file.write(note + "\n")
with open("my_notes.txt", "r") as file:
    saved = file.read()
print("--- SAVED NOTES ---")
print(saved)
```

**Explanation:**
- `note = input("Write a note: ")` — Prompts the user and stores the typed response.
- `with open("my_notes.txt", "a") as file:` — Opens a file using the specified file mode.
- `file.write(note + "\n")` — Writes text into the opened file.
- `with open("my_notes.txt", "r") as file:` — Opens a file using the specified file mode.
- `saved = file.read()` — Stores a value or calculation in a variable.
- `print("--- SAVED NOTES ---")` — Displays information in the terminal.
- `print(saved)` — Displays information in the terminal.

**Sample output/result:**

```text
Displays the newly entered note and any older saved notes.
```
