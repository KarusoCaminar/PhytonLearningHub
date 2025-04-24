# Python tutorials content
tutorials = [
    {
        'title': 'Introduction to Python',
        'content': """
# Welcome to Python!

Python is a high-level, interpreted programming language known for its simplicity and readability. It's an excellent language for beginners due to its clean syntax and powerful capabilities.

## Why Learn Python?

- **Easy to Learn**: Simple, readable syntax
- **Versatile**: Used in web development, data science, AI, automation, and more
- **Popular**: One of the most widely used programming languages
- **Powerful**: Extensive libraries and frameworks for various tasks

## What You'll Learn

In this course, you'll start with the basics and gradually build up to more complex programming concepts. By the end, you'll have a solid foundation in Python programming.

Let's begin with a simple example:
        """,
        'example': '''# Your first Python program
print("Hello, World!")
print("Welcome to Python Learning Hub!")''',
        'starter_code': '''# Try printing your own message
print("Hello, World!")
# Add another print statement below
'''
    },
    {
        'title': 'Variables and Data Types',
        'content': """
# Variables and Data Types

In Python, you don't need to declare variable types explicitly. The interpreter infers the type based on the assigned value.

## Basic Data Types

- **Integers**: Whole numbers like `5`, `-10`, `42`
- **Floats**: Decimal numbers like `3.14`, `-0.001`, `2.0`
- **Strings**: Text enclosed in quotes like `"hello"`, `'Python'`
- **Booleans**: `True` or `False` values

## Variable Assignment

Variables are assigned using the `=` operator:
        """,
        'example': '''# Variable examples
age = 25              # Integer
pi = 3.14159          # Float
name = "Alice"        # String
is_student = True     # Boolean

# Printing variables
print(name)
print("Age:", age)
print("Pi value:", pi)
print("Is student?", is_student)''',
        'starter_code': '''# Try creating your own variables
name = "Your Name"
age = 0  # Replace with a number

# Print your variables
print("My name is", name)
print("I am", age, "years old")

# Try creating a float and a boolean variable below
'''
    },
    {
        'title': 'Basic Operators',
        'content': """
# Basic Operators in Python

Python supports various operators for performing operations on variables and values.

## Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division (returns float)
- `//` Floor Division (returns integer)
- `**` Exponentiation (power)
- `%` Modulus (remainder)

## Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

## Logical Operators

- `and` Logical AND
- `or` Logical OR
- `not` Logical NOT
        """,
        'example': '''# Arithmetic operators
x = 10
y = 3

print("Addition:", x + y)        # 13
print("Subtraction:", x - y)     # 7
print("Multiplication:", x * y)  # 30
print("Division:", x / y)        # 3.3333...
print("Floor Division:", x // y) # 3
print("Exponent:", x ** y)       # 1000
print("Modulus:", x % y)         # 1

# Comparison operators
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x > y:", x > y)    # True
print("x < y:", x < y)    # False

# Logical operators
a = True
b = False
print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False''',
        'starter_code': '''# Try using different operators
x = 15
y = 4

# Calculate and print the following:
# 1. x plus y
# 2. x minus y
# 3. x multiplied by y
# 4. x divided by y
# 5. x to the power of y
# 6. The remainder when x is divided by y

# Write your code below
'''
    },
    {
        'title': 'Strings and String Methods',
        'content': """
# Working with Strings

Strings in Python are sequences of characters enclosed in quotes. Python provides many built-in methods to manipulate strings.

## Creating Strings

```python
single_quoted = 'Hello'
double_quoted = "World"
triple_quoted = '''This is a
multi-line string'''
```

## String Operations and Methods

Strings in Python can be concatenated, indexed, and sliced. Python also provides many useful string methods.
        """,
        'example': '''# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation

# Accessing characters (indexing)
print("First character:", first_name[0])  # J
print("Last character:", last_name[-1])   # e

# String methods
message = "hello, world!"
print(message.upper())          # HELLO, WORLD!
print(message.capitalize())     # Hello, world!
print(message.replace("world", "Python"))  # hello, Python!
print(len(message))             # 13 (length of string)''',
        'starter_code': '''# Try some string operations
your_string = "Python is amazing"

# Print the length of your string
print("Length:", len(your_string))

# Print your string in uppercase
print("Uppercase:", your_string.upper())

# Try other string methods like .lower(), .replace(), .split()
# Write your code below
'''
    }
]