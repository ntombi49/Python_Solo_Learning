# Functions Basics

# Functions Basics

# 🧠 What is a Function?
# A function is a block of code that runs only when it’s called.
# You use functions to group actions that you might need to repeat — instead of rewriting code every time.
# Think of it like this:
# A function is like a small machine — you give it input (ingredients), it does something (process), and gives you output (result).
# 
# 🧩 Basic Function Structure
# Here’s how a simple function looks in Python:

def greet():
    print("Hello, Ntombi!")

# Explanation:
# Keyword	        Meaning
# def	             Tells Python you’re defining a function
# greet	         The function name
# ()	             Parentheses — where inputs (parameters) go
# :	             Starts the function block
# print("Hello!")	  Code that runs when the function is called

# 🪄 Functions with Parameters (Inputs)
# You can make your function more flexible by adding parameters.

def greet(name):
    print(f"Hello, {name}!")
greet("Ntombi")
greet("Dimpho")

# 🎁 Functions with Return Values (Outputs)
# Sometimes you want your function to give back a result.
# You use the return keyword for that.

def add(a, b):
    total = a + b
    return total
# When you call it:

result = add(5, 3)
print(result)       #💡 return sends the value back — it doesn’t print it automatically.

# 🔁 Why Use Functions?
# Functions help you:
# Avoid repetition (write once, reuse many times)
# Organize code (break big problems into smaller ones)
# Make code readable and easy to debug
# Allow reusability (use the same logic anywhere)

# 🧮 Function Example — Putting It All Together
def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

result = calculate_average(10, 20, 30)
print(f"The average is {result}")

# ⚙️ Types of Functions in Python
# Type	             Description	                    Example
# Built-in	       Already provided by Python	       print(), len(), max()
# User-defined       Created by you	                    def greet():
# Lambda	           Small anonymous functions	     lambda x: x * 2

# 🧩 Summary Table
# Keyword	                Meaning
# def	                Define a function
# ()	               Holds parameters (inputs)
# return	           Sends a value back
# :	               Starts the function block
# pass	           Placeholder if function has no code yet

# 🌱 LEVEL 1 
# — Functions With No Inputs
# These help you get used to defining and calling functions.

# 🧩 Challenge 1: A Simple Greeting
def say_hello():
    print("Hello, welcome to Python!")

say_hello()

#🧩 Challenge 2: Print Your Favorite Hobby
def show_hobby():
    print("I love coding and reading!")

show_hobby()

# 🧩 Challenge 3: Function That Prints Today’s Motivation
def motivate():
    print("Keep going, you’re doing great!")

motivate()
# 💭 Try: Call motivate() three times.


# 🌿 LEVEL 2 — Functions With Inputs (Parameters)
# Now your functions will take in values when you call them.

# 🧩 Challenge 4: Personal Greeting
def greet(name):
    print(f"Hello, {name}! Have a great day!")
    
greet("Ntombi")
greet("Liya")

# 🧩 Challenge 5: Add Two Numbers
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)

# 🌼 LEVEL 3 — Functions That Return Values
# Now your function will give something back using return.

# 🧩 Challenge 6: Multiply Two Numbers
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

# 🌻 LEVEL 4 — Combining Logic Inside Functions
# 🧩 Challenge 8: Even or Odd Checker
def check_number(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_number(4)

# 🧩 Challenge 9: Function That Returns a Message
def get_message(name, age):
    return f"{name} is {age} years old."

info = get_message("Ntombi", 20)
print(info)

# 🧩 Challenge 10: Mini Calculator
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 2, "add"))

def profile(name, age):
    return f"My name is {name} and I am {age} years old"