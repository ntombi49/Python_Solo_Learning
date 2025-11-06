# Dictionaries
#key and value
# having a specific handing for whatver you want to store

# 🧠 What is a Dictionary in Python?
# A dictionary is a data structure that stores data in pairs — called key-value pairs.

student = {
    "name": "Ntombi",
    "age": 20,
    "course": "Python"
}
# # Here:

# # "name", "age" , and "course" are keys
# # "Ntombi", 20, and "Python" are values
# # So you can think of a dictionary as a mini database — it stores what something is (key) and the detail about it (value).

# # 🧩 Creating a Dictionary
# # You create it with curly braces {} and separate each key-value pair using a colon :.

person = {"name": "Liya", "age": 25, "city": "Durban"}

# # You can also start with an empty dictionary and add values later:
person = {}
person["name"] = "Liya"
person["age"] = 25
person["city"] = "Durban"

# # 🔍 Accessing Values
# # Use the key name to get its value:
# print(person["name"])  # Output: Liya
# # If you try a key that doesn’t exist, Python will give an error

# # To safely access values, use .get():

# print(person.get("hobby", "Not found"))  # Output: Not found

# # ✏️ Adding or Updating Values
# # You can update or add new key-value pairs easily:

person["age"] = 26         # Update age
person["hobby"] = "Reading"  # Add new key

# # ❌ Removing Items
# # There are several ways:

person.pop("city")      # Removes key 'city'
del person["hobby"]     # Removes key 'hobby'
person.clear()          # Removes everything

# # 🔁 Looping Through a Dictionary
# # You can loop through:
    
# # Keys
# # Values
# # Both (items)
# # Example:

student = {"name": "Thami", "age": 21, "grade": "A"}

for key in student:
    print(key)  # prints only the keys

for value in student.values():
    print(value)  # prints only the values

for key, value in student.items():
    print(f"{key}: {value}")  # prints both

# # 🧮 Useful Dictionary Methods

# # Example:
# print(student.keys())
# print(student.values())
# print(len(student))

# 🧠 Example Program

person = {"name": "Ntombi",
          "age": 19,
          "location": "Johannesburg"
          }

print(f"Name: {person["name"]}")
print(f"Age: {person['age']}")
print(f"location: {person['location']}")


# 🧩 Challenge 1
# — Create Your Profile
# Create a dictionary named my_profile with the following keys:

# "name"
# "age"
# "country"
# "hobby"
# Then print each key and its value

my_profile = {"name": "Ntombi",
              "age": 20,
              "country": "South Africa",
              "hobby": "coding",
              }

print(f"Name: {my_profile ['name']}")
print(f"Age: {my_profile ['age']}")
print(f"Country: {my_profile ['country']}")
print(f"Hobby: {my_profile ['hobby']}")

# 🧩 Challenge 2 
# — Add and Update Values

# Start with this dictionary:
# student = {"name": "Liya", "grade": "A"}
# Then:
# Add a new key "age" with any value.
# Change "grade" to "B+".
# Print the updated dictionary.

student = {"name": "Liya", "grade": "A"}

student["age"] = 20
student["grade"] = "B+"
print(student)


# 🧩 Challenge 3 
# — Remove a Key
# Use this dictionary:
# car = {"brand": "Toyota", "model": "Yaris", "year": 2020}
# Then:
# Remove "model".
# Add a new key "color" with value "Red".
# Print the final dictionary.

car = {"brand": "Toyota", "model": "Yaris", "year": 2020}

car.pop("model")
car["color"] = "Red"
print(car)



# 🧩 Challenge 4 
# — Loop Through a Dictionary
# Use this dictionary:
# person = {"name": "Thabo", "age": 22, "city": "Durban"}
# Write a loop that prints:
# name: Thabo
# age: 22
# city: Durban

person = {"name": "Thabo", "age": 22, "city": "Durban"}

for key, value in person.items():
    print(f"{key}: {value}")


# 🧩 Challenge 5 

# — Student Marks
# Make a dictionary named marks with three subjects as keys and marks as values.
# Then:
# Print the average mark.
# Print which subject has the highest mark.

value_list = []
marks = {"Maths": "63",
         "English": "72",
         "Biology": "54"
         }

for value in marks.values():
    value_list.append(int(value))
total = sum(value_list)
average = total / len(value_list)
print(average)

max_key = max(marks, key=marks.get)
max_value = marks[max_key]
print(f'The subject with high marks is {max_key} with {max_value} marks')

# 🧩 Challenge 6 — Word Counter

# Ask the user to enter a sentence.
# Count how many times each word appears and store the result in a dictionary.

# Example:
# Input: "I love love Python"
# Output: {'I': 1, 'love': 2, 'Python': 1}

sentences_dict = {}
word_count = {}
sentence = input("Enter a sentence: ")
new_sentence = sentence.lower().split(" ")

for i in new_sentence:
    sentences_dict[i] = ""

    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print(word_count)
