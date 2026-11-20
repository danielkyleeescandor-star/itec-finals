# Print and Input

print() displays information. input() asks the user to enter information. input() returns text, so use int() or float() when you need a number.

Each example is saved separately as a `.py` file.

## Example 1: Hello World — Easy

**Purpose:** Displays a simple message.

**Code:**

```python
print("Hello, world!")
```

**Explanation:**
- `print("Hello, world!")` — Displays information in the terminal.

**Sample output/result:**

```text
Hello, world!
```

## Example 2: Name Greeting — Easy

**Purpose:** Receives a name and greets the user.

**Code:**

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Explanation:**
- `name = input("Enter your name: ")` — Prompts the user and stores the typed response.
- `print("Hello,", name)` — Displays information in the terminal.

**Sample output/result:**

```text
If input is Alex: Hello, Alex
```

## Example 3: Personal Details — Easy

**Purpose:** Receives and displays a name and age.

**Code:**

```python
name = input("Name: ")
age = input("Age: ")
print("Name:", name)
print("Age:", age)
```

**Explanation:**
- `name = input("Name: ")` — Prompts the user and stores the typed response.
- `age = input("Age: ")` — Prompts the user and stores the typed response.
- `print("Name:", name)` — Displays information in the terminal.
- `print("Age:", age)` — Displays information in the terminal.

**Sample output/result:**

```text
If inputs are Alex and 17: Name: Alex; Age: 17
```

## Example 4: Add Two Numbers — Intermediate

**Purpose:** Converts two inputs to integers and adds them.

**Code:**

```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
```

**Explanation:**
- `a = int(input("First number: "))` — Prompts the user and stores the typed response.
- `b = int(input("Second number: "))` — Prompts the user and stores the typed response.
- `print("Sum:", a + b)` — Displays information in the terminal.

**Sample output/result:**

```text
Inputs 5 and 3: Sum: 8
```

## Example 5: Simple Receipt — Intermediate

**Purpose:** Calculates and displays the price of an item.

**Code:**

```python
item = input("Item: ")
price = float(input("Price: "))
print("--- RECEIPT ---")
print("Item:", item)
print("Price: PHP", price)
```

**Explanation:**
- `item = input("Item: ")` — Prompts the user and stores the typed response.
- `price = float(input("Price: "))` — Prompts the user and stores the typed response.
- `print("--- RECEIPT ---")` — Displays information in the terminal.
- `print("Item:", item)` — Displays information in the terminal.
- `print("Price: PHP", price)` — Displays information in the terminal.

**Sample output/result:**

```text
Inputs Notebook and 45: Item: Notebook; Price: PHP 45.0
```

## Example 6: Rectangle Area — Intermediate

**Purpose:** Uses input values to calculate area.

**Code:**

```python
length = float(input("Length: "))
width = float(input("Width: "))
print("Area:", length * width)
```

**Explanation:**
- `length = float(input("Length: "))` — Prompts the user and stores the typed response.
- `width = float(input("Width: "))` — Prompts the user and stores the typed response.
- `print("Area:", length * width)` — Displays information in the terminal.

**Sample output/result:**

```text
Inputs 8 and 4: Area: 32.0
```

## Example 7: Student Profile — Hard

**Purpose:** Collects and displays several student details.

**Code:**

```python
name = input("Student name: ")
course = input("Course: ")
year = input("Year level: ")
print("\nSTUDENT PROFILE")
print("Name:", name)
print("Course:", course)
print("Year:", year)
```

**Explanation:**
- `name = input("Student name: ")` — Prompts the user and stores the typed response.
- `course = input("Course: ")` — Prompts the user and stores the typed response.
- `year = input("Year level: ")` — Prompts the user and stores the typed response.
- `print("\nSTUDENT PROFILE")` — Displays information in the terminal.
- `print("Name:", name)` — Displays information in the terminal.
- `print("Course:", course)` — Displays information in the terminal.
- `print("Year:", year)` — Displays information in the terminal.

**Sample output/result:**

```text
Sample inputs Sam, BSIT, 1st Year are displayed in a profile.
```

## Example 8: Mini Order Summary — Hard

**Purpose:** Calculates the total cost of an order.

**Code:**

```python
product = input("Product: ")
quantity = int(input("Quantity: "))
price = float(input("Price each: "))
total = quantity * price
print("Product:", product)
print("Quantity:", quantity)
print("Total: PHP", total)
```

**Explanation:**
- `product = input("Product: ")` — Prompts the user and stores the typed response.
- `quantity = int(input("Quantity: "))` — Prompts the user and stores the typed response.
- `price = float(input("Price each: "))` — Prompts the user and stores the typed response.
- `total = quantity * price` — Stores a value or calculation in a variable.
- `print("Product:", product)` — Displays information in the terminal.
- `print("Quantity:", quantity)` — Displays information in the terminal.
- `print("Total: PHP", total)` — Displays information in the terminal.

**Sample output/result:**

```text
Inputs Pen, 4, 10: Total: PHP 40.0
```
