# If Statements

# 🟢 1. The if Statement
# Used when you want to run some code only if a condition is true.
age = 18

if age >= 18:
    print("You are an adult.")
# 🧩 Explanation:
# if checks a condition (age >= 18)
# If the condition is True, it runs the indented code.
# If it’s False, it skips that part.

# 🟡 2. The else Statement
# Used when you want to do something else if the condition is false.
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor")
    
# 🧮 Example 3 — Odd or Even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ⚙️ 3. Conditions can use any comparison
# | Operator | Meaning             | Example  |
# | -------- | ------------------- | -------- |
# | `==`     | equal to            | `x == 5` |
# | `!=`     | not equal to        | `x != 5` |
# | `>`      | greater than        | `x > 5`  |
# | `<`      | less than           | `x < 5`  |
# | `>=`     | greater or equal to | `x >= 5` |
# | `<=`     | less or equal to    | `x <= 5` |


# 🧩 Example 4 — Grade Checker
grade = int(input("Enter your mark: "))

if grade >= 50:
    print("You passed!")
else:
    print("You failed.")
    
    
#PRACTICE QUESTIONS

#1
number = int(input("Enter a number: "))
if number %2 == 0:
    print("Even")
else:
    print("Odd")
    
#2
exam_score = int(input("Enter your score: "))
if exam_score >= 50:
    print("You have passed! ")
    
else:
    print("You failed")
    
#3
age = int(input("How old are you? "))
if age >= 18:
    print("You can vote")
else:
    print("You are too young to vote")

#4
temp_C = int(input("What is the temperature? "))
if temp_C >= 30:
    print("It's hot today") 
else:
    print("The weather is nice.")   
    
#5
password = input("Enter the password: ")
if password.lower() == "Python123".lower():
    print("Access granted")
else:
    print("Access denied")
    
