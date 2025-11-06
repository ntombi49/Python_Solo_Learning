#You cant add
# you can't change anything

# 🧠 What Is a Tuple?
# A tuple is a collection of ordered and unchangeable items — meaning once you create it, you can’t modify (add, remove, or change) its elements.
# Tuples are written with round brackets ( ).

# 🧩 Example
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# 📘 Why Use Tuples?
# They are faster than lists.
# They are immutable (can’t be changed), which makes them safe for data that shouldn’t be modified.
# Can be used as dictionary keys (lists cannot).

# 🧱 Tuple Syntax and Access
# Operation	     Example	       Description
# Create tuple	  t = (1, 2, 3)	   Defines a tuple
# Access  item	  t[0]	           Returns first element
# Negative index  t[-1]	           Returns last element
# Slice	          t[1:3]	       Returns elements from index 1 to 2
# Length	      len(t)	       Number of items
# Count	          t.count(2)	   Counts occurrences
# Index	          t.index(3)	   Finds index of a value

# 🧮 Tuple Packing & Unpacking
# You can assign multiple values at once.

person = ("Ntombi", 20, "South Africa")
name, age, country = person

print(name)
print(age)
print(country)

# 🧊 Tuples Inside Tuples
# You can even store tuples inside other tuples:

nested = (("a", 1), ("b", 2), ("c", 3))
print(nested[1])       # ('b', 2)
print(nested[1][0])    # 'b'

# 🔁 Looping Through a Tuple
colors = ("red", "blue", "green")
for color in colors:
    print(color)
    
#🧩 Challenge Ideas
# Create a tuple of your 5 favorite foods and print them one by one.

foods = ("apple", "Burger", "chips", "carrots", "spinach")
for food in foods:
    print(food)

# Unpack a tuple of 3 values into variables and print them.

values = ("Hello", "Ntombi", "Centurion")
greeting, name, location = values

print(greeting)
print(name)
print(location)

# Find how many times "apple" appears in a tuple.

count = 0
fruits = ("apples", "banana", "apples", "orange")

for fruit in fruits:
    if fruit == "apples":
        count += 1
print(f'apples appears {count} in this tuple')

# Combine two tuples together.
fruits = ("apples", "banana", "apples", "orange")
foods = ("apple", "Burger", "chips", "carrots", "spinach")

combined = fruits + foods
print(combined)

# Create a tuple of numbers and find the smallest and largest.

numbers = (1, 4, 7, 5, 10, 15)
print(min(numbers))
print(max(numbers))
