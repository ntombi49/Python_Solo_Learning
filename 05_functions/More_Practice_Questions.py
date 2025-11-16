# 1️⃣ Count how many times a letter appears in a word

# Example:
# count_letter("banana", "a") → 3

def count_letter(word, letter):
    count = 0
    
    for i in word:
        if letter == i:
            count += 1
            
    return count
print(count_letter("banana", "a"))

# 2️⃣ Return the last item in a list

# Example:
# last_item([10, 20, 30]) → 30

def last_item(items):
    
    return items[-1]

print(last_item([10, 20, 30]))


# 3️⃣ Check if a number is positive, negative, or zero

# Return "positive", "negative", or "zero"

def check_number(number):
    
    if number < 0:
        return "Negative"
    elif number == 0:
        return "Zero"
    else:
        return "Positive"
    
print(check_number(-3))

# 4️⃣ Return the first three characters of a string

# If the string is shorter than 3, return the whole thing.

def first_three_char(string):
    
    return string[:3]
    
print(first_three_char("Ntombi"))

# 5️⃣ Multiply all numbers in a list

# Example:
# multiply_list([2, 3, 4]) → 24

def multiply(numbers):
    
    results = 1
    for num in numbers:
        results *= num
        
    return results

print(multiply([2, 3, 4]))


# ⭐ INTERMEDIATE CHALLENGES (Level 2)

# These will stretch your thinking but are still very doable.

# 6️⃣ Return only the unique items from a list

# Example:
# unique_items([1,1,2,3,3]) → [1,2,3]

def unique_items(items):
    
    # results = []
    items_set = set(items)
    
    return list(items_set)

print(unique_items([1,1,2,3,3]))
            

# 7️⃣ Check if two strings are anagrams

# (Anagrams = same letters, different order)
# Example:
# "listen" → "silent"

def anagrams(word1, word2):
    
    word1_sorted = sorted(word1.lower())
    word2_sorted = sorted(word2.lower())
    
    if word1_sorted == word2_sorted:
        return True
    else:
        return False
            
print(anagrams("silent", "listen"))


# 8️⃣ Return the second largest number in a list

# Example:
# # second_largest([10, 20, 30, 5]) → 20

def second_largest(list):
    
    for number in list:
        if number == max(number):
            continue
        
    return max(number)

print(second_largest([10, 20, 30, 5]))

# 9️⃣ Remove duplicates from a string

# Example:
# "mississippi" → "misp"

def remove_duplicates(string):
    
    string_set = set(string)
    
    return string_set

print(remove_duplicates("mississippi"))

# 🔟 Count how many even and odd numbers exist in a list

# Return a tuple like:
# (even_count, odd_count)

def count_even_odd(numbers):
    
    even_count = 0
    odd_count = 0
    
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
            
    return even_count, odd_count

print(count_even_odd([2, 5, 7, 10, 22, 33, 52, 4]))