# While Loops

# We’ll start simple with “while” loops (which repeat code while a condition is true).

count = 1
while count <= 5:     #keep looping as long as count is less than or equal to 5.
    print(count)
    count += 1        #Increases the value each time, so the loop doesn't go on forever
    
# 🔁 What a while loop is
# A while loop repeats a block of code as long as a condition is True.    
# Basic shape:
    
    # while condition:
        # code to repeat
# Think of it like:
# “Keep doing this while the question is yes.”

# 🧭 Step-by-step example (the classic counter)
# Code:

count = 1
while count <= 5:
    print(count)
    count += 1
# Let’s follow each line iteration by iteration:
# Initial state before loop starts:
# count = 1

# Loop check 1
# Condition count <= 5? → 1 <= 5 → True

# Execute body:
# print(count) → prints 1
# count += 1 → count becomes 2

# Loop check 3
# 3 <= 5 → True → print 3, count → 4

# Loop check 4
# 4 <= 5 → True → print 4, count → 5

# Loop check 5
# 5 <= 5 → True → print 5, count → 6

# Loop check 6
# 6 <= 5 → False → loop stops, program continues after the loop.

# ⚠️ Common mistake: infinite loop

# If the condition never becomes False, the loop will run forever.
# Bad example:

i = 1
while i <= 3:
    print(i)
    # forgot to change i -> infinite loop!

# Fix: update the loop variable inside:

i = 1
while i <= 3:
    print(i)
    i += 1
    
# 🛠 Useful tools inside loops
# BREAK
# Exit the loop immediately.

n = 1
while True:
    print(n)
    if n == 3:
        break   # stop loop
    n += 1

# continue
# Skip the rest of the loop body and go to the next iteration.

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue   # skip printing 3
    print(i)
    
# -------------------Understanding again ------------------------------

# 1) What a while loop is (in one sentence)

# A while loop repeats a block of code over and over as long as a condition is True.
# Think: “Keep doing this while the question is yes.”

# 2 Anatomy of a while loop

while condition:     #This is an expression that evaluates to True or False
    body_line_1      #This is the body, they run everytime the conditions is True 
    body_line_2      #when the condition becomes False, the loop stops and execution continues after the loop
    ...
# code here runs after loop ends

# Walk through examples. 

count = 1              #initial state
while count <= 5:       # 1 - True, 2 - True, 3- True, 4 -True, 5- True
    print(count)        # 
    count = count + 1   # count increases everytime so that it checks the next condition
print("Done")

#infinite loops
i = 1
while i <= 3:
    print(i)

# 6) Common loop patterns & why we use them

# Pattern A — Input validation (ask until valid)
answer = ""
while answer.lower() not in ("yes", "no"):
    answer = input("Type yes or no: ")
print("You typed:", answer)

# Pattern B — Sentinel loop (stop when special word entered)
text = ""
while text != "quit":
    text = input("Type something (or 'quit' to stop): ")
    print("You typed:", text)
    
# Pattern C — Accumulate until stop (sum numbers)
total = 0
num = None
while True:
    num = int(input("Enter a number ('0' to stop: )"))
    if num  == 0:
        break
    total = total + num
    print("Total is: ", total)
    
# 7) Truthiness: what can be used as a condition

# Comparison expressions → x < 5, name == "Ntombi" evaluate to True/False.
# You can use values directly: while some_list: repeats while some_list is not empty (non-empty containers are True, empty ones False).
# None, 0, "", [], {} evaluate to False.

# 8) Small annotated examples with state traced
# Example: Countdown from 3

n = 3
while n > 0:
    print ("n = ", n)
    n = n - 1
print("Blast off!")

# Example: Keep asking password, limit tries (shows break)

correct = "hey"
tries = 0

while tries < 3:
    password = input("Password: ")
    if password == correct:
        print("Welcome")
        break
    tries = tries + 1
    
else:
    print("Too many attempts")
    
#9) Debugging tips (what to check when loop behaves wrong)
# Is the loop condition correct? (typos, wrong operators)
# Are you updating the variables used in the condition inside the loop?
# Are you accidentally using strings where numbers are needed? (use int() / float())
# Print internal state (e.g., print("count =", count)) to watch how variables change.
# If Python prints the same thing forever, Ctrl+C to stop, then inspect the code.

# 10) Short practice — I’ll show solution for one step-by-step
# You said you had trouble — let’s do Practice #2 (Sum until zero) together, step-by-step.
# Goal: keep asking numbers, add them to total, stop when user types 0, then print total.

total = 0
num = None

while True:
    num = int(input("Enter number or '0' to stop: "))
    if num == 0:
        break
    total = total + num
print('Total:', total)

2
pswd = "Hey"
count = 0
while count < 3:
    password = input("Enter password: ")
    if password == pswd:
        print("Welcome")
        break
    count = count + 1
else:
    print("Too Many Attemps. ")
    
#An example
#  🧠 Example: Skip wrong numbers and stop at 0
#  We’ll write a program that keeps asking the user for a number:
 
#  If the number is negative → skip it using continue
 
#  If the number is 0 → stop completely using break
 
#  Otherwise → print the square of the number

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num < 0:
        print("Skipping negative number...")
        continue  # skips the rest of this loop and goes back to start

    if num == 0:
        print("Program stopped.")
        break  # completely exits the loop
    
    print("Square:", num ** 2)

# Practice

secrete = 7
guess = None

while True:
    guess = int(input("Enter number: "))
    if guess < 0:
        print("Negative numbers not allowed!")
        continue
    
    if guess == secrete:
        print("You got it!")
        break
    
    else:
        print("Try again!")

# Practice
user = "Ntombi"
pswd= "Python123" 
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if password == pswd and username == user:
        print("Login successful!")
        break
    else:
        print("Incorrect credentials, try again!")
        attempts = attempts + 1
else:
    print("Too many failed attempts. Access denied!")
    
# Practice 2

correct_pin = 4321
attempts = 0

while attempts < 3:
    pin = int(input("Enter PIN: "))
    
    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN, try again.")
        attempts = attempts + 1
else:
    print("Card blocked. Contact your bank.")
    
# Practice 3
while True:
    score = 0
    
    cof = input("What is the capital of France? ")
    if cof.lower() == "paris":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect.")
         
    sum = int(input("What is 5 + 3? "))
    if sum == 8:
        print("correct!")
        score = score + 1
    else:
        print("Incorrect.")

    language = input("What programming language are we learning? ")
    if language.lower() == "python":
        print("correct!")
        score = score + 1
    else:
        print("Incorrect.")
        
    print(f'You got {score} out of 3!')

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye")
        break
    
    
# Challenge 2

correct_pin = 4321
attempts = 0
starting_balance = 1000

while attempts < 3:
    pin = int(input("Enter PIN: "))
    if pin == correct_pin:
        print("Access granted!")
        
        action = input("Do you want to Withdraw, Deposit or Check balance: ")
        
        if action.lower() == "withdraw":
            withdraw_amount = float(input("How much: "))
            if withdraw_amount <= starting_balance:
                starting_balance = starting_balance - withdraw_amount
                print(f'New balance: R{starting_balance}')
            else:
                print("Insufficient funds!")
            
        elif action.lower() == "deposit":
            deposit_amount = float(input("How much: "))
            starting_balance = starting_balance + deposit_amount
            print(f'New balance: R{starting_balance}')
        
        elif action.lower() == "check balance":
            print(f'Your balance is R{starting_balance}')
        else:
            print("Invalid option")
            break
    else:
        print("Invalid PIN")
        attempts = attempts + 1
else:
    print("Card blocked. Contact your bank")  
    
#Challenge 3

secret_number = 6
attempts = 0

while attempts < 3:
    guess = int(input("Enter your guess number: "))
    if guess == secret_number:
        print("Correct! You guessed it!")
        break
    
    elif guess == 0:
        print("Game over!")
        break
    else:
        print("Try again!")
        attempts = attempts + 1
        
else:
    print("You've reach maximun number of attempts!")

# 6    
password = "python123"
      
while True:
    pswd = input("Enter password: ")
    if pswd == password:
        print("Access granted")
        break
    else:
        print("Try again!")

# 7. Sum Until Zero

# Keep asking for numbers and add them together until the user enters 0.
# Then show the total.
number = 0
while True:
    num = int(input("Enter numbers: "))
    number = number + num
    if num == 0:
        break
print(f'Total = {number}')

# 8. Guess the Secret Number
# Pick a secret number between 1 and 10 and keep asking the user until they guess right.
    
secret = 5

while True:
    guess = input("Enter secret number: ")
    if guess == secret:
        print("You guessed right!")
else:
        print("Wrong")
        
        
#Pass
#On to the next one
#in a function, it says go to next functions