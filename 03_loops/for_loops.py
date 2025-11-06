# For Loops

# For Loops
# A for loop is used when you want to repeat something a fixed number of times or iterate over a collection (like a list, string, or range of numbers).
#You know how much you want a 

# 1️⃣ Basic for loop with numbers
for i in range(5):
    print(i)     #it ends before 5, which is 4 (python)
    

# 2️⃣ For loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3️⃣ For loop over a string
letters = "Python"
for letter in letters:
    print(letter)
    
# 4️⃣ Using break and continue in a for loop
for i in range(1, 6):
    if i == 3:
        continue  # skip number 3
    if i == 5:
        break  # stop the loop
    print(i)

#Challenge 1

for i in range(1, 11):
    
    if i == 5:
        print("Skipping number 5...")
        continue
    if i == 8:
        print("Stopping at 8...")
        break
    else:
        print(i)
    
# Challenge 2
total = 0

for number in range(1, 21):
    if number %2 == 0:
        total = total + number
print(f'The sum of even numbers from 1 to 20 is {total}')
        
#cHALLANGE 3

character = "*"
for i in character:
    print(i)
    print(i * 2)
    print(i * 3)
    print(i * 4)
    print(i * 5)
    
for i in range(1, 6):
    print("*" * i)
    
#Challenge 4

fruit = input("What is your favorite fruit? ")

for letter in fruit:
    if letter == "a":
        continue
    print(letter) 
    
# cHALLENGE 5

sentence = input("Type any sentence of choice: ")
vowels = ["a", "e", "i", "o", "u"]
count = 0

for i in sentence:
    for v in vowels:
        if i.lower() == v:
            count = count + 1
print(f'Number of vowels: {count}')
             
             #Another way to do it
sentence = input("Type any sentence of choice: ")
vowels = "aeiou"
count = 0

for char in sentence.lower():
    if char in vowels:
        count = count + 1
print(f'Number of vowels: {count}')

# Challenge 6

num = int(input("Enter any number: "))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
    
# Challenge 7
total = 0

for i in range(1, 51):
    if i %2 != 0:
        total = total + i
print(f'The total sum is {total}')

# Challenge 8

word = input("Enter any word: ")
reversed_word = word[::-1]

for i in reversed_word:
    print(i)

# Challenge 9

for i in range(1, 31):
    if i % 3 == 0:
        print(i)
    
# Challenge 10

word = input("Enter a word: ")
vowels = 'aeiou'
count = 0

for char in word.lower():
    if char in vowels:
        count += 1
print(count)

# Challenge 11

numbers = []

for i in range(5):
    num = int(input("Enter 5 numbers: "))
    numbers.append(num)
print(max(numbers))


# Challenge 12

num = int(input("Enter a number: "))

for i in range(num, -1, -1):
    print(i)
    
    #using a while loop:
    
while num >0:
    print(num)
    num -= 1

1

for i in range(1, 31):
    if i % 3 == 0:
        print(i)
        
# 2

name = input("What is your name? ")
num = int(input("Enter a number: "))

for i in range(num):
    print(name)
    
# 3
word = input("Enter any word: ")

for i in word:
    print(i * word)
    
#5

for i in range(1, 11):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
