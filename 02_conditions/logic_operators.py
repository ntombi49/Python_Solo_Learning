# Logical operators help your program make smarter decisions by checking more than one condition at once.
# There are three main ones:

# | Operator | Example           | Meaning                   |
# | -------- | ----------------- | ------------------------- |
# | `and`    | `x > 0 and y > 0` | True if *both* are true   |
# | `or`     | `x > 0 or y > 0`  | True if *any one* is true |
# | `not`    | `not x > 0`       | Reverses the result       |


# 🧠 Examples
# 1️⃣ Using and
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club.")
else:
    print("Access denied.")
# ✅ Both must be True for the condition to pass.

# 2️⃣ Using or
raining = True
has_umbrella = False

if raining or not has_umbrella:
    print("You won’t get wet.")
else:
    print("You might get soaked!")
# ✅ At least one of the conditions must be True.

# 3️⃣ Using not
hungry = False

if not hungry:
    print("You are full.")
else:
    print("Time to eat!")
# ✅ not flips True ↔ False.

#Practice Questions
#1
age = int(input("How old are you? "))
id_card = input("Do you have an ID card (yes/no)")

if age >= 18 and id_card == "yes":
    print("Access granted")
else:
    print("Access denied")

#2
is_raining = input("Is it raining? (yes/no) ")
has_umbrella = input("Do you have an umbrella (yes/no)? ")


if is_raining == "yes" and has_umbrella == "no":
    print("You might get wet.")
else:
    print("You are safe")

#3
weekend = input("Is it Saturday or Sunday? ")

if weekend == "Saturday" or weekend == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")
    
#4
hungry = input("Are you hungry? (yes/no)")
if hungry == "no":
    print("You're full!.")
else:
    print("Time to eat!")
    
#5
age = int(input("How old are you? "))
score = int(input("Enter your score: "))

if age >= 18 and score >= 50:
        print("Eligible")
else:
    print("Not eligible")

#MORE PRACTICE QUESTIONS

#1
age = int(input("How old are you? "))
student_card = input("Do you have a student card? ")
if age < 18 or student_card == "yes":
    print("You get a discount.")
else:
    print("No discount available.")
    
#2
temp_C = int(input("What is the temperature? "))
is_raining = input("Is it raining? (yes/no) ")

if temp_C < 20 or is_raining == "yes":
    print("Better wear a jacket.")
else:
    print("You don't need a jacket")

#3
member = input("Are you a member (yes/no) ")
overdue_books = input("Do you have overdue books? (yes/no)")

if member == "yes" and  overdue_books == "no":
    print("You can borrow books")
else:
    print("Cannot borrow books.")
    
#4
average_mark = int(input("Enter your average mark: "))
att_perc  = int(input("Enter attendence percentage: "))

if average_mark >= 75 and att_perc >= 80:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
    
#5
username = input("Enter username: ")
password = input("Enter password: ")

if username == 'admin' and password == '1234':
    print("Login successful!")
else:
    print("Invalid username or password")
    
    
