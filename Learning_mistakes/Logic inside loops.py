# 📘 What to learn next:
# How loops run from start to finish

# Where to place return (after loop, not inside)

# When to use break, continue, and when NOT to


# ✅ 🔥 MINI LESSON: 
# Logic Inside Loops (Your Most Important Fix)

# 1️⃣ How loops run (very important)
# A loop repeats every line inside it for each item.

# for num in [1, 2, 3, 4]:
#     print(num)
    
# 2️⃣ Why “return” inside a loop is dangerous
# You often do this:

# for x in items:
#     return x   # ❌ loop stops immediately

# This means the loop only runs one time.

# ❗ RULE:
# Only put return AFTER the loop unless you want to stop early.

# def add_all(nums):
#     total = 0
#     for n in nums:
#         total += n
#     return total      # ✅ OUTSIDE the loop

# 3️⃣ When to use break
# break stops the loop, but the function continues.

# Use it when you want to stop because you found what you needed.
# for n in nums:
#     if n == 10:
#         break
    
# When to use:

# find first match
# stop searching
# stop when condition is met

# When not to use:

# when you need to process the whole list
# when you need to count ALL items
# when the question requires whole-loop work

# 4️⃣ When to use continue
# continue skips the current iteration and moves to the next one.

# Example:
# for n in nums:
#     if n < 0:
#         continue      # skip negative numbers
#     print(n)

# When to use:

# skip certain items
# ignore invalid data
# skip vowels, skip odd numbers, etc.

# When not to use:

# if you still need to use the item in calculations
# if it makes you miss important items

# 5️⃣ When NOT to use return, break, continue
# Avoid them when the goal is:

# processing the whole list or string
# counting items
# summing all numbers
# building a result step-by-step
# checking ALL items

#----------------Practice Questions ----------------------------

# Beginner Level
# 1. Count how many even numbers are in a list

def count_even(numbers):
    
    count = 0
    
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

print(count_even([1, 4, 5, 20, 32, 6]))

# 1.1 Write a function count_odd(numbers) that counts all odd numbers in a list.

def count_odd(numbers):
    
    count = 0
    
    for number in numbers:
        if number % 2 == 0:
            continue
        count += 1
        
    return count
print(count_odd([1, 4, 5, 20, 32, 6]))

# 1.2 Write a function count_multiples_of_three(numbers) that counts how many numbers in a list are divisible by 3.

def count_multiples_of_three(numbers):
    
    count = 0
    
    for number in numbers:
        if number % 3 == 0:
            count += 1
            
    return count

print(count_multiples_of_three([3, 4, 6, 7, 9, 10]))
        

# 2. Find the total of all numbers in a list


def sum_list(numbers):
    
    total = sum(numbers)
    
    return total

print(sum([5, 10, 20, 30]))

# 3. Count how many vowels are in a string

def count_vowels(string):
    
    count = 0
    vowels = "aeiou"
    
    for char in string:
        if char.lower() in vowels:
                count += 1
                
    return count

print(count_vowels("Banana"))


# 4. Print each character in a string, except vowels (use continue)

def exclude_vowels(string):
    
    vowels = "aeiou"
    
    for char in string:
        if char.lower() in vowels:
            continue
        
        print(char)

print(exclude_vowels("Banana"))

# 5. Print only the first 3 consonants in a string
#(Stop completely after printing 3 of them — use break)

def first_three_consonants(string):
    
    vowels = "aeiou"
    
    for char in string:
        if char.lower() in vowels:
            continue
        
        print(char[:2])

print(first_three_consonants("Campuses"))
        