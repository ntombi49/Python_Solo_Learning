# # 🧩 Lesson: Comparison Operators
# # Comparison operators are used to compare two values — they return either True or False.

# # Think of them as questions you ask Python, like:

# # “Is this number bigger than that number?”
# # “Are these two things equal?”

# # 🔹 Python’s Comparison Operators
# # | Operator | Meaning                  | Example  | Output |
# # | :------: | :----------------------- | :------- | :----: |
# # |   `==`   | Equal to                 | `5 == 5` | ✅ True |
# # |   `!=`   | Not equal to             | `5 != 3` | ✅ True |
# # |    `>`   | Greater than             | `10 > 8` | ✅ True |
# # |    `<`   | Less than                | `2 < 5`  | ✅ True |
# # |   `>=`   | Greater than or equal to | `5 >= 5` | ✅ True |
# # |   `<=`   | Less than or equal to    | `4 <= 6` | ✅ True |

# # 💻 Example 1: Checking equality
# age = 18
# print(age == 18)  # True
# print(age != 21)  # True

# # 💻 Example 2: Comparing numbers
# x = 10
# y = 5

# print(x > y)   # True
# print(x < y)   # False
# print(x >= 10) # True
# print(y <= 5)  # True

# # 💻 Example 3: Using with strings
# # You can also compare text (strings).

# name = "Ntombi"
# print(name == "Ntombi")   # True
# print(name != "John")     # True


# 📝 Remember: string comparisons are case-sensitive
# 👉 "Hello" ≠ "hello"

#MINI CHALLANGE

#1
print(10 == 20)

#2
age = int(20)
print(age > 18)

#3
name = input("Enter name: ")
print(name.lower() == "Ntombi")

#4
print(10 != 5)

#5
print(7 <= 10)
