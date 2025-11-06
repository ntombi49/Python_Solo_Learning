# Does not contain any duplicates
#It removes duplicates. 

# 🟢 What is a Set?
# A set is a collection of unique items — it does not allow duplicates.
# It’s like a bag that removes any repeated items automatically.

# 🧠 Example:
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

# ⚙️ How to Create a Set
# There are two main ways:

# Using curly braces
my_set = {1, 2, 3}

# Using the set() function
my_set2 = set([1, 2, 3, 4])

# 🧰 Common Set Methods
# Method	    Description	                                   Example
# .add(x)	    Adds an item to the set	                       fruits.add("orange")
# .remove(x)	Removes an item; error if item not found	   fruits.remove("apple")
# .discard(x)	Removes an item; no error if item not found	   fruits.discard("apple")
# .pop()	    Removes and returns an arbitrary item	       item = fruits.pop()
# .clear()	    Removes all items from the set	                   fruits.clear()
# .copy()	    Returns a shallow copy of the set	           new_set = fruits.copy()
# len(set)	    Returns the number of items in the set	           len(fruits)
# in / not in	Checks membership	                           "apple" in fruits

# Set Operations
# Operation	 Symbol	   Description	                          Example
# Union	        `	         `	                                Combines all items from both sets (no duplicates)
# Intersection	&	      Items common to both sets	            A & B
# Difference	    -	      Items in first set but not in second	A - B
# SymmetricD	    ^         Items in either set but not in both	A ^ B

# 🧩 Set Challenge 1
# — Basic Set Operations
# Goal:
# Practice creating a set, adding/removing elements, and checking membership.

# Instructions:

# Create a set named friends with the names: "Liya", "Busi", "Nokx".
# Add a new friend "Dimpho" to the set.
# Remove "Busi" from the set.
# Check if "Nokx" is in the set.
# Finally, print the set and its total number of friends.

friends = {"Liya", "Busi", "Nokx"}
friends.add("Dimpho")
print(friends)
friends.remove("Busi")
print(friends)

if "Nokx" in friends:
        print("Nokx is in the set")
print(f'Total friends: {len(friends)}')


# 🧩 Challenge 2 
# — Friends from Two Groups
# You have two sets:
# Group A and Group B.
# Each contains names of friends.

# ✅ Your tasks:

# Find and print all friends (Union).
# Find and print friends who are in both groups (Intersection).
# Find and print friends who are only in Group A.
# Print how many unique friends there are in total.

Group_A = {"Kate", "Kim", "Lerato", "John"}
Group_B = {"Sim", "John", "Khati", "Zinhle"}

print(Group_A.union(Group_B))
print(Group_A & Group_B)
print(Group_A - Group_B)
print(f'Total unique friends: {len(Group_A.union(Group_B))}')