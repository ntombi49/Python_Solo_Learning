# 🧠 Lesson: nested if (Control Flow → 2_nested_if.py)
# 💡 What it means:
# A nested if is an if statement inside another if.
# It helps you make multiple levels of decisions.

# Think of it like saying:
# “If this is true, then check another thing.”

# 🧩 Example 1 — Age and License Check
age = int(input("Enter your age: "))

if age >= 18:
    has_license = input("Do you have a driver’s license? (yes/no): ")
    if has_license == "yes":
        print("You can drive!")
    else:
        print("You need a license to drive.")
else:
    print("You’re too young to drive.")
# 🧠 How it works:
# First, we check if the person is 18 or older.
# Only if that’s true, we go inside the next if to check for a license.
# If the first condition is false, the inner part is skipped completely.

# 🧩 Example 2 — Grade System
grade = int(input("Enter your mark: "))

if grade >= 50:
    if grade >= 75:
        print("Distinction!")
    else:
        print("Pass")
else:
    print("Fail")   
# 🧠 Explanation:    
# First, the program checks if you passed.    
# If yes, it then checks if you got a distinction.

# 🧩 Example 3 — Login System with Role
username = input("Enter username: ")
password = input("Enter password: ")

if username == "Ntombi":
    if password == "Python123":
        print("Welcome back, admin!")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")
    
# ⚙️ Tips
# Keep indentation consistent (4 spaces per level).
# Don’t over-nest too deeply — it can get confusing.
# You can mix nested if with else and elif later on.

#PRACTICE QUESTIONS
#1
age = int(input("Enter your age: "))

if age >= 18:
    highSchool = input("Have you finished High School? (yes/no) ")
    if highSchool == "yes":
        print("You can apply for college.")
    else: print("Finish high school first.")
else: print("You're not old enough to apply.")

#2
score = int(input("Enter your score: "))

if score >= 50:
    if score >= 75:
        print("Excellent!")
    else:
        print("You passed.")
else:
    print("You failed")
    
#3
username = input("Enter username: ")
password = input("Enter password: ")
if username == "Ntombi":
    if password.lower() == "Ntombi@123".lower():
        print("Welcome, Ntombi!")
    else:
        print("Incorrect password.")
        
else:
    print("User not found.")
 
#4
temp_C = int(input("Enter the temperature: "))
if temp_C < 15:
    jacket = input("Do you have a Jacket? (yes/no) ")
    if jacket.lower == "yes".lower():
        print("You're ready for the cold!")
    else:
        print("You should wear a jacket.")
else:
    print("Nice weather today!")
    
#5
pincode = input("Enter the pin code: ")

if pincode == "2025":
    check_balance = input("Withdraw / Check balance ")
    if check_balance.lower() == "withdraw":
        print("Processing your withdrawal...")
    elif check_balance.lower() == "Check balance":
        print("Your balance is R1000.")
    else:
        print("Invalid option")
else:
    print("Access Denied")


    
    
