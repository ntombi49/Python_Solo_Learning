# Lists

# # 🧠 Let’s start with Lists

# # Lists are used to store multiple items in a single variable.
# # A list is a collection that allows you to store multiple values in one variable.
# # You can think of it like a shopping basket — you can keep many items inside, and you can add, remove, or change them anytime.

# # Example:

# fruits = ["apple", "banana", "mango"]
# print(fruits)
# print(fruits[1])  # prints 'banana'

# # mix data tye
# mixed = ["Ntombi", 18, 3.5, True]


# # 💡 2. Accessing Items (Indexing)
# # Each item in a list has a position number (index), starting from 0.

# # Example:

# fruits = ["apple", "banana", "mango"]
# print(fruits[0])  # prints 'apple'
# print(fruits[1])  # prints 'banana'
# print(fruits[2])  # prints 'mango'

# # You can also use negative indexing:

# print(fruits[-1])  # prints 'mango' (last item)
# print(fruits[-2])  # prints 'banana'

# # ✏️ 3. Changing Items
# # Lists are mutable — that means you can modify them.

# # Example:

# fruits[1] = "orange"
# print(fruits)  # ['apple', 'orange', 'mango']

# # 🧺 4. Adding Items
# # You can add new items in different ways:

# fruits.append("grape")     # adds at the end
# fruits.insert(1, "pear")   # adds at position 1
# print(fruits)

# # ❌ 5. Removing Items
# fruits.remove("apple")  # removes by name
# fruits.pop()            # removes last item
# fruits.pop(0)           # removes item at position 0
# del fruits[1]           # also removes by position
# print(fruits)

# # 🧹 6. Other Useful List Operations
# # 📏 Find length:
# print(len(fruits))  # how many items in 

# # ➕ Combine two lists:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = list1 + list2
# print(combined)

# # 🔁 Loop through a list:
# for fruit in fruits:
#     print(fruit)
    
    
# #  🧮 Sum and sort:
# numbers = [5, 2, 9, 1]
# print(sum(numbers))  # adds all numbers
# numbers.sort()       # sorts in order
# print(numbers)

# # 🎯 7. Common Mistakes
# ❌ Using round brackets () instead of square brackets [].
# ✅ Correct: mylist = [1, 2, 3] 

# ❌ Forgetting commas between items.
# ✅ Correct: mylist = ["a", "b", "c"]






#Practice Problems

1
foods = ['food1', 'food2', 'food3', 'food4', 'food5']
print(foods[0])
print(foods[4])

# #2
# foods.append('food6')
# print(foods)

#3
foods.remove('food1')
print(foods)

# #4
# for food in foods:
#     print(food)
    
# #5
# numbers = [10, 20, 30, 40]
# print(sum(numbers))

# average = sum(numbers) / len(numbers)
# print(average)

#Challenge 1

# colors = input("Enter 3 colors: ")
# color_list = colors.split(",")
# print(color_list)
# print(color_list[0].strip())
# print(color_list[2].strip())

#Using loops.

# 🧩 List Practice Challenges
# Challenge 1 — Favorite Colors
# Ask the user to enter 3 colors and store them in a list.
# Then print:
# The full list
# The first and last color

# colors = []
# count = 0

# for i in range(3):
#     color = input(f'Enter first color {i + 1}: ')
#     colors.append(color)
    
# print(colors)
# print(colors[0])
# print(colors[2])

# Challenge 2 — Shopping List
# Create a list with at least 5 grocery items.
# Then:
# Remove one item.
# Add two new ones.
# Print the updated list.

# grocery = ["Maize", 'noodles', 'water', 'Fish Oil', 'banana']
# grocery.remove('water')
# grocery.append('potatos')
# grocery.append('rice')
# print(grocery)


# Challenge 3 — Numbers Average
# Ask the user to enter 5 numbers (using a loop).
# Store them in a list and print:
# The list
# The sum
# The average

# count = 0
# number_list = []
# while True:
#     numbers = int(input(f'Enter number {count + 1}: ' ))
#     number_list.append(numbers)
#     count = count + 1

#     if count == 5:
#         break
# print(number_list)
# total = sum(number_list)
# print(f'Sum: {total}')
# average = total / len(number_list)
# print(f'Average: {average}')
     
#      #Using A FOOR lOOP
# number_list = []
# for i in range(5):
#     numbers = int(input(f'Enter numbers {i + 1} : '))
#     number_list.append(numbers)   
# print(number_list)

# total = sum(number_list)
# print(f'Sum: {total}')
# print(f'Average: {total / len(number_list)}')

# Challenge 4 — Even Numbers
# Make a list from 1 to 20.
# Then print only the even numbers using a for loop.
number_list = []
for number in range(1, 21):
    # print(number)
    if number % 2 == 0:
        number_list.append(number)
print(number_list)

# Challenge 5 — Word Lengths
# Ask the user to type 3 words.
# Store them in a list, then print each word and how many letters it has.
# 📝 Example:

word_list = []
count = 0
while True:
    words = input("Enter a word: ")
    word_list.append(words)
    count = count + 1
    if count == 3:
        break
print(f'{word_list[0]} has {len(word_list[0])} letters')
print(f'{word_list[1]} has {len(word_list[1])} letters')
print(f'{word_list[2]} has {len(word_list[2])} letters')

#Challenge 6

# Goal:
# Ask the user to enter 5 words.
# After they finish, print which word is the longest and how many letters it has.

words_list = []
for i in range(5):
    words = input(f'Enter word {i + 1}: ')
    words_list.append(words)
# print(words_list)
# print(max(words_list))
# print(len(max(words_list)))
print(f'The longest word is {print(max(words_list))} and it has {print(len(max(words_list)))} letters')

              #Using a while loop
words_list = []
count = 0

while True:
    words = input(f'Enter word {count + 1}: ')
    words_list.append(words)
    count += 1
  
    if count == 5:
        break
max_value = max(words_list, key=len) 
max_length = len(max_value)
print(f'The longest word is {max_value} and it has {max_length} letters')

#Challenge 7

count = 0

for i in range(5):
    num = input(f'Enter number {i + 1}: ')
    num_list = list(num)
    count += 1

    if count == 5:
        break
    
print(f'The smallest number is {min(num_list)}')