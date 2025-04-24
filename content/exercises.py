# Python exercises content
exercises = [
    {
        'title': 'Hello World',
        'problem': '''
# Exercise: Hello World

Write a program that prints "Hello, World!" and then on a new line, print your name.

For example, if your name is "Alice", the output should be:

```
Hello, World!
Alice
```''',
        'starter_code': '''# Write your solution here
print("Hello, World!")
# Print your name below
''',
        'expected_output': '''Hello, World!
YourName''',
        'solution': '''print("Hello, World!")
print("Alice")'''
    },
    {
        'title': 'Simple Calculator',
        'problem': '''
# Exercise: Simple Calculator

Create a simple calculator that:
1. Asks the user for two numbers
2. Performs addition, subtraction, multiplication, and division
3. Prints the results

Your program should:
- Handle input using the `input()` function
- Convert the input to numbers using `int()` or `float()`
- Calculate all four operations
- Format the output neatly
''',
        'starter_code': '''# Simple calculator program
# Get first number from user
num1 = float(input("Enter first number: "))

# Get second number from user
num2 = float(input("Enter second number: "))

# Calculate and display results
# Your code here
''',
        'solution': '''# Simple calculator program
# Get first number from user
num1 = float(input("Enter first number: "))

# Get second number from user
num2 = float(input("Enter second number: "))

# Calculate results
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")'''
    },
    {
        'title': 'Temperature Converter',
        'problem': '''
# Exercise: Temperature Converter

Write a program that converts temperatures between Celsius and Fahrenheit.

Your program should:
1. Ask the user for a temperature value
2. Ask the user to specify if it's in Celsius (C) or Fahrenheit (F)
3. Convert to the other unit
4. Display the result with appropriate labels

Conversion formulas:
- F = (C × 9/5) + 32
- C = (F - 32) × 5/9

Make sure your program handles user input properly and provides clear output.
''',
        'starter_code': '''# Temperature converter program
# Your code here
''',
        'hint': '''Break this down into steps:
1. Get the temperature value using input() and convert to float
2. Get the unit (C or F) using input()
3. Use if/else to determine which conversion to perform
4. Apply the appropriate formula
5. Print the result with proper formatting''',
        'solution': '''# Temperature converter program
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    # Convert Celsius to Fahrenheit
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}°C = {converted_temp:.2f}°F")
elif unit == "F":
    # Convert Fahrenheit to Celsius
    converted_temp = (temperature - 32) * 5/9
    print(f"{temperature}°F = {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")'''
    },
    {
        'title': 'List Manipulation',
        'problem': '''
# Exercise: List Manipulation

In this exercise, you'll practice working with Python lists.

Create a program that:
1. Creates a list of 5 numbers
2. Prints the original list
3. Adds two more numbers to the end of the list
4. Removes the first number from the list
5. Sorts the list in ascending order
6. Prints the final modified list
7. Prints the sum, minimum, and maximum values of the list

Use list methods like append(), remove(), sort(), and built-in functions like sum(), min(), max().
''',
        'starter_code': '''# List manipulation exercise
# Create a list of 5 numbers
numbers = [10, 5, 8, 1, 7]

# Print the original list
print("Original list:", numbers)

# Add two more numbers to the list
# Your code here

# Remove the first number from the list
# Your code here

# Sort the list
# Your code here

# Print the final modified list
# Your code here

# Print sum, min, and max
# Your code here
''',
        'expected_output': '''Original list: [10, 5, 8, 1, 7]
Modified list: [1, 5, 7, 8, 12, 15]
Sum: 48
Minimum: 1
Maximum: 15''',
        'solution': '''# List manipulation exercise
# Create a list of 5 numbers
numbers = [10, 5, 8, 1, 7]

# Print the original list
print("Original list:", numbers)

# Add two more numbers to the list
numbers.append(12)
numbers.append(15)

# Remove the first number from the list
numbers.remove(10)  # or: del numbers[0] or numbers.pop(0)

# Sort the list
numbers.sort()

# Print the final modified list
print("Modified list:", numbers)

# Print sum, min, and max
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))'''
    },
    {
        'title': 'String Manipulation',
        'problem': '''
# Exercise: String Manipulation

Write a program that:
1. Creates a string variable containing your full name
2. Prints the length of your name
3. Converts your name to uppercase and prints it
4. Converts your name to lowercase and prints it
5. Replaces any spaces with dashes and prints it
6. Creates a new string that is your name reversed
7. Checks if your name is a palindrome (reads the same forward and backward)

Use string methods like upper(), lower(), replace(), and slicing operations.
''',
        'starter_code': '''# String manipulation exercise
# Create a string with your full name
name = "Your Name" 

# Print the length of your name
# Your code here

# Convert to uppercase and print
# Your code here

# Convert to lowercase and print
# Your code here

# Replace spaces with dashes and print
# Your code here

# Create a reversed name string
# Your code here

# Check if name is a palindrome
# Your code here
''',
        'hint': '''For the reversed string, you can use slicing with a negative step: name[::-1]
For the palindrome check, compare the original string with its reversed version (ignoring case)''',
        'solution': '''# String manipulation exercise
# Create a string with your full name
name = "Your Name"  # Change this to your actual name

# Print the length of your name
print("Length of name:", len(name))

# Convert to uppercase and print
print("Uppercase:", name.upper())

# Convert to lowercase and print
print("Lowercase:", name.lower())

# Replace spaces with dashes and print
print("With dashes:", name.replace(" ", "-"))

# Create a reversed name string
reversed_name = name[::-1]
print("Reversed:", reversed_name)

# Check if name is a palindrome
if name.lower() == reversed_name.lower():
    print("Your name is a palindrome!")
else:
    print("Your name is not a palindrome.")'''
    }
]
