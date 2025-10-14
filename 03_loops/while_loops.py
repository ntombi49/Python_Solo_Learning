# While Loops

# We’ll start simple with “while” loops (which repeat code while a condition is true).

count = 1
while count <= 5:     #keep looping as long as count is less than or equal to 5.
    print(count)
    count += 1        #Increases the value each time, so the loop doesn't go on forever
    
# 🔁 What a while loop is
# A while loop repeats a block of code as long as a condition is True.    
# Basic shape:
    
    while condition:
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
    
