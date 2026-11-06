# Grade 8 Python Program: Lists, List Methods, Loops, and Control Statements
# Reference: More About Python

# 1. Lists in Python and Accessing Items (Indexing & Slicing)
hobbies = [
    "reading",
    "cooking",
    "hiking",
    "painting",
]  # Creating a list
print("Original Hobbies List:", hobbies)
print("First hobby (Index 0):", hobbies[0])  
print("Last hobby (Index -1):", hobbies[-1])  
print("First two hobbies (Slicing):", hobbies[:2])  

# 2. List Methods (.append())
hobbies.append("gardening")  # Adds a new item to the end of the list
print("Updated Hobbies List after append:", hobbies)

# 3. Counter-Controlled Loop (for loop) with else block
print("\n--- Iterating through Hobbies using a for loop ---")
for hobby in hobbies:  
  print(f"I enjoy {hobby}.")
else:
  print("Loop completed: All hobbies displayed successfully!")  

# 4. Condition-Controlled Loop (while loop)
print("\n--- Countdown using a while loop ---")
count = 3
while count > 0:  
  print(f"Countdown: {count}")
  count -= 1  # Updating the condition variable
print("Liftoff!")

# 5. Control Statements (continue and break)
print("\n--- Demonstrating continue and break statements ---")
for i in range(6):  
  if i == 2:
    continue  # Skip the rest of the loop when i is 2
  if i == 5:
    break  # Terminate the loop completely when i reaches 5
  print("Current number:", i)
