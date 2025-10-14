# Input Output
print("Hello, world!")           # Prints plain text
name = "Ntombi"
print("My name is", name)        # Prints text and variable
print(f"My name is {name}")      # Using f-string (cleaner and modern)

name = input("What is your name? ")
print(f"Hello, {name}!")

# If you want to get a number, you must convert it using int() or float():
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print(f"You are {age} years old and {height}m tall.")

# Important: Data Types from Input

# Everything from input() is a string.

# Convert it when needed:

age = int(input("Age: "))  # integer
price = float(input("Price: "))  # decimal

#MINI CHALLANGE
#1
name = input("What is your name? ")
age = input("How old are you? ")
print(f'Hi {name}, you are {age} years old')

#2
num1 = int(input("Give any number: "))
num2 = int(input("Give a second number: "))
print(num1 + num2)

#3
fav_color = input("What is your favorite color? ")
fav_animal = input("What is your favorite animal? ")
print(f'Your favorite color is {fav_color} and your favorite animal is {fav_animal}')

#PRACTICE QUESTIONS

#1
num1 = int(input("Give any number: "))
num2 = int(input("Give any second number: "))
print('Sum:', num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1/num2)

#2
fav_movie = input("What is your favorite movie? ")
actor = input("Who was one of the actors? ")
release_year = input("When was the movie released? ")
print(f'My favorite movie is {fav_movie}, starring {actor}, released in {release_year}')

#3
temp_Fahnr = float(input("What is the temperature? "))
temp_Ce = (temp_Fahnr - 32) * 5/9
print(temp_Ce)

#4
age_in_years = int(input("Age in years: "))
age_in_months = age_in_years * 12
print(f'You are {age_in_years} years old, which is {age_in_months} months')

#5
name = input("What is your name? ")
age = input("How old are you? ")
country = input("Which country were you born in? ")
print(f'Hello, my name is {name}. I am {age} years old and I live in {country}.')

