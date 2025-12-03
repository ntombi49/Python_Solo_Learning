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
    count = 0
    
    for char in string:
        if char.lower() in vowels:
            continue
        
        print(char)
        count += 1
        
        if count == 3:
            break
            
        
print(first_three_consonants("Banana"))


# Print characters until you hit the first vowel.
#Stop completely when you see one.

def before_first_vowel(string):
    
    vowels = "aeiou"
    
    for char in string:
        if char.lower() in vowels:
            break
            
        print(char)
    
print(before_first_vowel("Strong"))

# 🔥 LEVEL 1 — Loop Logic (Warm-up)
# 1️⃣ Count how many uppercase letters are in a string

# Example:
# "HeLLo" → 3

def count_uppercases(string):
    
    uppercase = 0
    
    for letter in string:
        if letter == letter.upper():
            uppercase += 1
            
    return uppercase

print(count_uppercases("HeLLo"))

# 2️⃣ Count how many items in a list are greater than 10

# Example:
# [3, 12, 20, 5] → 2

def count_items(numbers):
    
    items = 0
    
    for number in numbers:
        if number > 10:
            items += 1
            
    return items

print(count_items([3, 12, 20, 5]))


# 3️⃣ Create a new list with only odd numbers

# Example:
# [1, 2, 3, 4, 5] → [1, 3, 5]

def new_list(numbers):
    
    new_list = []
    
    for number in numbers:
        if number % 2 != 0:
            new_list.append(number)
            
    return new_list

print(new_list([1, 2, 3, 4, 5]))
            
            

# 4️⃣ Count how many words in a sentence start with 's'

# Case-insensitive.

def count_words(sentence):
    
    words = 0
    
    for word in sentence.lower():
        if word[0] == "s":
            words += 1
            
    return words

print(count_words("Such a strong lady Shaun."))
            

# 5️⃣ Print only characters at even positions

# Example:
# "Python" → P t o (indexes 0,2,4)

def char_even(word):
    
    for letter in word.lower():
        if letter.index() % 2 == 0:
            print(letter)
            
print(count_words("Python"))



# 🔥 LEVEL 2 — Loop Logic (Trickier)
# 6️⃣ Print numbers from a list until you reach a negative number

# Stop immediately when you hit a negative.

def negative_number(numbers):
    
    for number in numbers:
        if number < 0:
            break
        
        print(number)

print(negative_number([1, 5, 6, -4, 7, 15]))


# 7️⃣ Count how many characters appear before the first space

# Example:
# "Hello World" → 5

def count_char(characters):
    
    char = 0
    
    for letter in characters:
        char += 1
        if letter == " ":
            break
        
    return char

print(count_char("Hello World"))


# 8️⃣ Find the first number in a list that is divisible by 7

# Return that number.

def divisible_by_seven(numbers):
    
    for number in numbers:
        if number % 7 == 0:
            break
        
    return number

print(divisible_by_seven([1, 3, 9, 14, 21, 30]))


# 9️⃣ Reverse a string manually using a loop (no slicing)

# Example:
# "cat" → "tac"

# def reverse_string(string):
    
#     for letter in string:
        


# 🔟 Build a new string but skip double letters

# Example:
# "baallooon" → "balon"

def new_string(word):
    
    new_string = ""
    
    for letter in word:
        if letter in new_string:
            continue
        new_string += letter
        
    return new_string

print(new_string("ballooon"))

# 🔥 LEVEL 3 — Loop Logic (Challenge Mode)
# 1️⃣1️⃣ Find the longest word in a sentence

# Example:
# "I love programming" → "programming"

def longest_word(sentence):
    
    sentence_list = sentence.split()
        
    return max(sentence_list)
            
print(longest_word("I love programming"))


# 1️⃣2️⃣ Count how many times a number changes (compare to previous number)

# Example:
# [1, 1, 2, 2, 3, 1]
# Changes at: 1→2, 2→3, 3→1 → 3 changes




# 1️⃣3️⃣ Create a new list with only increasing numbers

# Keep a number only if it is larger than the previous kept number.

# Example:
# Input: [3, 1, 2, 5, 4, 7]
# Output: [3, 5, 7]

# 1️⃣4️⃣ Count consecutive duplicates

# Example:
# [1,1,2,3,3,3] → duplicates = 4 (two 1s → 1, three 3s → 2 extra)

# 1️⃣5️⃣ Check if a string is symmetrical

# Left half == right half
# Example:
# "abba" → True
# "abcd" → False