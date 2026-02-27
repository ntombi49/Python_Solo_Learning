# 🧩 LEVEL 1 — The Concept of a Function

# Think of a function like a machine or recipe that does one specific job.
# You give it something (called input).
# It does something with it (called process).
# Then it gives you something back (called output).

# 💡 Example (Real Life Analogy):
# Imagine a blender:
# You put fruits inside (this is the input).
# You press the button (this is the function doing its work).
# It gives you juice (this is the output).
# So, in Python, a function works just like that:
# It takes inputs, does something, and (sometimes) gives an output.

# 🧠 In code language:
# A function has 3 main parts:

# Part	                       Meaning           	                    Example
# def     	               Tells Python you’re defining a function	    def greet():
# Function name   	        What you’ll call later to use it	          greet()
# Code inside (body)	    What the function does	                     print("Hello!")

# 🔹 Example in Python:
def greet():
    print("Hello!")
    
# # # Now, this function is defined — but it doesn’t run yet.
# # # To use the function (run it), you must call it:
greet()

# # # 🏋️‍♀️ YOUR TURN (Exercises – Level 1)
# # # Let’s test if you got this idea:

# # # 1️⃣ Create a function called say_hello that prints “Hi there!”
# # # 2️⃣ Create a function called welcome_message that prints “Welcome to my program.”
# # # 3️⃣ Call each one to make sure it works.

def say_hello():
    print("Hi there!")

def welcome_message():
    print("Welcome to my program")
    
say_hello()
welcome_message()

# A function is a reusable block of code that only runs when called.

# 🌱 Now, let’s move to LEVEL 2 – Functions with Input (Parameters)

# Right now, your functions always say the same thing — they don’t change.
# But what if you want them to work with different data?

# That’s where parameters come in.
# They’re like placeholders that receive data when the function runs.

# 💡 Example:
def greet(name):
    print(f"Hello, {name}!")
    
greet("Ntombi")
greet("Zinhle")


# 🏋️‍♀️ Your Exercises — Level 2
# 1️⃣ Create a function called greet_user that takes one argument called name,
# and prints something like "Hi, [name]! Nice to meet you!".

def greet_user(name):
    print(f'Hi, {name}! Nice to meet you!')


# 2️⃣ Create another function called favourite_food that takes one argument called food,
# and prints "I also like [food]!".

def favorite_food(food):
    print(f'I also like {food}!')

# 3️⃣ Call both functions a few times with different names and foods.
greet_user("Zinhle")
greet_user("Ntombi")
greet_user("Khati")
favorite_food("Pasta")
favorite_food("Porridge")
favorite_food("Snacks")

#  Level 3 — Returning Values 💪
# 🧠 What does “return” mean?
# So far, your functions have only been printing things (like greetings).
# But sometimes, we want a function to give back a result instead of just showing it on the screen.

# That’s what return does — it sends a value back to where the function was called.

# 🧩 Example 1: Adding two numbers
def add_numbers(a, b):
    result = a + b
    return result

sum = add_numbers(3, 5)
print(sum)

# 🧩 Example 2: Reusing the returned value
def square(number):
    return number * number

x = square(4)
y = square(10)
print(x, y)

#🧠 Mini Challenge:
# Try writing this function yourself:

# 👉 Create a function called multiply that:
# Takes two numbers as inputs
# Returns the product (multiplication result)
# Then, call the function and print the result

def multiply(a, b):
    return a * b

results = multiply(5, 5)
print(results)

# Challenge 1 — Multiply Two Numbers
# Create a function called multiply that takes two numbers and returns their product.

# Call the function with any two numbers and print the result.

def multiply(num1, num2):
    return num1 * num2

print(multiply(4, 2))

# Challenge 2 — Full Name
# Create a function called full_name that takes first_name and last_name.
# The function should return the full name as a single string.
# Call the function with your first and last name, and print it.

def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Ntombi", "Rikhotso"))

# Challenge 3 — Celsius to Fahrenheit
# Create a function called c_to_f that takes a temperature in Celsius.
# The function should return the temperature in Fahrenheit using this formula:

# Fahrenheit = (Celsius * 9/5) + 32
# Call the function with any Celsius value and print the result.

def c_to_f(temperature):
    return (temperature * 9/5) + 32

print(c_to_f(20))

#More Practice Examples:

# 🧩 Practice 1 — Square a Number
# Write a function that:

# Takes a number as input
# Returns the square of that number

def square(number):
    return number * number

print(square(4))

# 🧩 Practice 2 — Add Three Numbers
# Write a function that:

# Takes three numbers
# Returns their sum

def add_three(num1, num2, num3):
    return num1 + num2 + num3

numbers = add_three(2, 4, 6)
print(numbers)

# 🧩 Practice 3 — Even or Odd
# Write a function that:

# Takes a number
# Returns "Even" if the number is even, or "Odd" if it’s odd

def check_even_odd(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_even_odd(5))

# 🧩 Practice 4 — Area of a Rectangle
# Write a function that:

# Takes length and width as inputs
# Returns the area (length × width)

def area(lenght, width):
    return lenght * width

print(area(5, 10))

# # 🧩 Practice 5 — Greeting Generator
# # Write a function that:

# Takes a name and a time_of_day (like “morning” or “evening”)
# Returns a message like:
# "Good morning, Ntombi!"

def greet(name, time_of_day):
    
    return f'Good {time_of_day}, {name}!'

print(greet("Ntombi", "evening"))

#-------------------------------------------------------------------------------------

# 🧩 LEVEL 2: Intermediate Functions

# 🧠 1. Using Loops Inside a Function
# We can make a function that loops through numbers and performs actions.

def print_even_numbers(limit):
    for num in range(1, limit + 1): #start at 1 and stop just before limit + 1. Meaning stop at limit
        if num % 2 == 0:
            print(num)

# print(even_numbers(10))
print_even_numbers(10)
# 🧠 2. Function Returning a List
# A function doesn’t have to just print — it can also return data.

def get_squares(numbers):
    squares = []
    for n in numbers:
        squares.append(n ** 2)
    return squares

print(get_squares([1, 2, 3, 4]))

# 🧠 3. Function with If-Else Logic
# You can use conditions inside your function to make decisions.

def check_temperature(temp):
    if temp > 30:
        return "It's hot outside."
    elif temp >= 15:
        return "It's warm."
    else:
        return "It's cold."

print(check_temperature(10))

# 🧠 4. Combining Everything
# You can mix input, logic, and calculations.


def average_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 50:
        return f"Average: {average} — Passed"
    else:
        return f"Average: {average} — Failed"

print(average_marks([60, 55, 70, 80]))

#Practice Questions. 

# 🧩 Challenge 1: Multiply and Add

# Write a function called multiply_and_add that:
# Takes three numbers: a, b, and c.
# Multiplies a and b, then adds c.
# Returns the final result

def multiply_and_add(a, b, c):
    return a * b + c

print(multiply_and_add(2, 3, 4))

# 🧮 Challenge 2: Find the Largest Number
# Write a function called find_largest that:

# Takes three numbers as input.
# Returns the largest of the three.

def find_largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
print(find_largest(5, 9, 3))

def find_largest(numbers):
    num_list = []
    for num in numbers:
        num_list.append(num)
        
    for num in num_list:
        if num > num_list:
            return num

print(find_largest(5, 9, 3))

✏️ Challenge 3: Count Vowels
Write a function called count_vowels that:

Takes a string as input.
Returns how many vowels (a, e, i, o, u) are in it.

def count_vowels(string):
    count = 0
    vowels = "aeiou"
    
    for i in string.lower():
        for v in vowels:
            if i == v:
                count += 1
    return count

print(count_vowels("Ntombi"))
    

# 💰 Challenge 4: Calculate Discount
# Write a function called apply_discount that:

# Takes price and discount_percentage as inputs.
# Returns the final price after applying the discount.

def apply_discount(price, discount_percentage):
    
    dp_decimal = discount_percentage / 100
    discount_amount = price * dp_decimal
    final_price = price - discount_amount
    
    return final_price

print(apply_discount(100, 20))

# 🕒 Challenge 5: Age Category
# Write a function called age_category that:

# Takes an age as input.
# Returns:

# "Child" if age < 13
# "Teenager" if age is between 13–19
# "Adult" if age >= 20

def age_category(age):
    
    if age < 13:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:
        return "Adult"
    
print(age_category(16))


# #More Practice Questions. 

# 1️⃣ Reverse a String
# Write a function that takes a word and returns it reversed.

def reverse_string(word):
    
    return word[::-1]

print(reverse_string("Ntombi"))


# 2️⃣ Check for a Palindrome
# A palindrome is a word that reads the same backward (like "madam").


def is_palindrome(word):
    
    if word[::-1] == word:
        return "True"
    else:
        return "False"
    
print(is_palindrome("madam"))
print(is_palindrome("python"))

# 3️⃣ Calculate Factorial
# Create a function that finds the factorial of a number (e.g. 5! = 5×4×3×2×1 = 120).

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(5))

    
# 4️⃣ Count Even and Odd Numbers
# Given a list of numbers, return how many are even and how many are odd.

def count_even_odd(numbers):
    
    even = 0
    odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        
    return f'Even: {even}, Odd: {odd}'
    
print(count_even_odd([1, 2, 3, 4, 5, 6])) 

# 5️⃣ Find the Longest Word
# Write a function that takes a list of words and returns the longest one.

def longest_word(words):
    
    long_word = ""
    
    for word in words:
        if len(word) >= len(long_word):
            long_word = word
    return long_word
            # return word
        
print(longest_word(["Ntombi", "Python", "Developer", "AI"]))

#More Practice Questions. 
# 🧩 Functions Practice Challenges — Set 3

# 1️⃣ square_list(numbers)
# Write a function that takes a list of numbers and returns a new list with each number squared.
# 🧠 Example:
# [1, 2, 3, 4] → [1, 4, 9, 16]

def square(numbers):
    # list = []
    new_list = []
    
    # for num in numbers:
        # list.append(num)
    
    for i in list:
        new_list.append(i*i)
        
    return new_list
    
print(square([1, 2, 3, 4]))


# 2️⃣ find_min_max(numbers)

# Return both the smallest and largest number from a list.
# 🧠 Example:
# [5, 3, 8, 2, 10] → (2, 10)

def find_max_min(numbers):
    # num_list = []
    
    # for i in numbers:
        # num_list.append(i)
    
    return f'{min(numbers)}, {max(numbers)}'

print(find_max_min([5, 3, 8, 2, 10]))


# 3️⃣ remove_vowels(word)

# Return a version of the string without vowels.
# 🧠 Example:
# "Ntombi" → "Ntm b"

def remove_vowels(word):
    vowels = "aeiou"
    result = ""
    # word_list = []
    
    for letter in word:
        if letter.lower() not in vowels:
            results += letter
            
    return result

print(remove_vowels("Ntombi"))

# 4️⃣ sum_even_numbers(numbers)

# Return the sum of all even numbers in a list.
# 🧠 Example:
# [1, 2, 3, 4, 5, 6] → 12

def sum_even_numbers(numbers):
    count = 0
    
    for num in numbers:
        if numbers % 2 == 0:
            count += num
        
    return count

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))

# 5️⃣ count_words(sentence)

# Count and return the number of words in a given sentence.
# 🧠 Example:
# "I love Python coding" → 4

def count_words(sentence):
    
    words = sentence.split()
    count = 0
    
    for word in words:
        count += 1
        
    return count
    
print(count_words("I love Python coding"))


# 6️⃣ find_common_items(list1, list2)

# Return the common elements between two lists.
# 🧠 Example:
# [1, 2, 3] and [2, 3, 4] → [2, 3]

def find_common_items(list1, list2):
    
    common = [] 
    for i in list1:
        for v in list2:
            if i == v:
                common.append(i)
    return common
            
print(find_common_items([1, 2, 3], [2, 3, 4]))



# 7️⃣ is_prime(number)

# Return True if the number is prime, otherwise False.
# 🧠 Example:
# is_prime(7) → True

def is_prime(number):
    
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True
    
print(is_prime(4))
    

# 8️⃣ calculate_grade(marks)
# Given a percentage, return a grade:

# 80–100 → “A”
# 70–79 → “B”
# 60–69 → “C”
# 50–59 → “D”
# below 50 → “F”

def calculate_grade(marks):
    
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
    
print(calculate_grade(67))

# 9️⃣ reverse_list(items)
# Reverse the order of items in a list without using .reverse() or slicing.
# 🧠 Example:
# [1, 2, 3] → [3, 2, 1]

def reverse_list(items):
    
    new_items = [items[-1], items[-2], items[0]]
    
    return new_items

print(reverse_list([1, 2, 3]))


# 🔟 sum_digits(number)
# Take an integer and return the sum of its digits.
# 🧠 Example:
# 1234 → 10

def sum_digits(number):
    
    list = []
    list.append(number)
    

print(sum_digits(1234))
