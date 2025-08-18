print("Hello, World!")

#Variables in python
a= 10
b= 20   
c = a + b
print("The sum of a and b is:", c)

d = True
print("The value of d is:", d)
e = "Python is fun!"
print("The value of e is:", e)
f = 3.14
print("The value of f is:", f)
g = None
print("The value of g is:", g)

#TypeCasting in Python
a = 10
b = 20.5
c = str(a)  # Convert integer to string
d = int(b)  # Convert float to integer
print("The value of c is:", c)
print("The value of d is:", d)
e = float(a)  # Convert integer to float
print("The value of e is:", e)
f = bool(a)  # Convert integer to boolean   
print("The value of f is:", f)
g = bool(0)  # Convert zero to boolean
print("The value of g is:", g)
h = bool("")  # Convert empty string to boolean
print("The value of h is:", h)  

#Operators in python  (can start with a variable name and underscore)

num1 = 10
num2 = 20
# Arithmetic Operators
sum_result = num1 + num2    
print("Sum:", sum_result)
diff_result = num1 - num2
print("Difference:", diff_result)
prod_result = num1 * num2
print("Product:", prod_result)
div_result = num1 / num2
print("Division:", div_result)
mod_result = num1 % num2
print("Modulus:", mod_result)
exp_result = num1 ** 2
print("Exponentiation:", exp_result)

#Assignment Operators
a = 10
b = 20
a += b  # Equivalent to a = a + b
print("After +=, a:", a)
a -= b  # Equivalent to a = a - b
print("After -=, a:", a)

#Comparison Operators
x = 10
y = 20
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to

#Logical Operators
a = True
b = False
print("a and b:", a and b)  # Logical AND
print("a or b:", a or b)    # Logical OR
print("not a:", not a)      # Logical NOT   

#Identity Operators
x = [1, 2, 3]
y = x
z = x.copy()    
print("x is y:", x is y)      # True, same object
print("x is z:", x is z)      # False, different objects    
print("x is not z:", x is not z)  # True, different objects

# String and String Methods
str1 = "Hello, World!"
str2 = "Python Programming"
print("Length of str1:", len(str1))  # Length of the string
print("Uppercase str1:", str1.upper())  # Convert to uppercase
print("Lowercase str1:", str1.lower())  # Convert to lowercase  
print(str1[0:5])  # Slicing the string
print("Concatenation:", str1 + " " + str2)  # Concatenate
print("Repetition:", str1 * 2)  # Repeat the string
print(str1.isalnum)

# User Input
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")
print(type(name))

num = input("Enter a number: ")
print("You entered:", num)
print(int(num) + 6)  # Print the type of the input

# List & List Methods
l1 = [1, 2, 3, 4, 5, "Hello"]
l2 = [6, 7, 8, 9, 10]
print(type(l1))  # Print the type of the list
print("List 1:", l1)    
print("List 2:", l2)
l1.append(6)  # Add an element to the end of the list
print("After appending 6 to List 1:", l1)
l1.extend(l2)  # Extend List 1 with List 2  
print("After extending List 1 with List 2:", l1)
l1.insert(0, 0)  # Insert 0 at the beginning of List 1

l2.sort()
print("List 2 after sorting:", l2)  # Sort List 2
l2.pop()  # Remove the last element from List 2
print("List 2 after popping the last element:", l2)
l2.copy()
print("Copy of List 2:", l2.copy())  # Create a copy of List 2
l2.remove(6)  # Remove the element 6 from List 2        
print("List 2 after removing 6:", l2)
l2.reverse()  # Reverse List 2  
print("List 2 after reversing:", l2)
l2.clear()  # Clear List 2
print("List 2 after clearing:", l2)  # Print List 2 after clearing

# Tuple & Tuple Methods
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
print(type(t1))  # Print the type of the tuple
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print(t1.index(3))  # Get the index of the element 3 in Tuple 1
print(t1.count(2))  # Count occurrences of 2 in Tuple 1
print("Concatenation of tuples:", t1 + t2)  # Concatenate Tuple 1 and Tuple 2

# Set & Set Methods (it does not allow duplicate elements, it is unordered)
s1 = {1, 2, 3, 4, 5}
s2 = {1,2,3, 6, 7, 8, 9, 10}
s1.pop()
print(s1.pop())  # Remove and return an arbitrary element from Set 1
s1.add(6)  # Add an element to Set 1
print("Set 1 after adding 6:", s1)
s1.update(s2)  # Update Set 1 with elements from Set 2
print("Set 1 after updating with Set 2:", s1)
s1.remove(2)  # Remove the element 2 from Set 1
print("Set 1 after removing 2:", s1)
s1.union(s2)  # Union of Set 1 and Set 2
print("Union of Set 1 and Set 2:", s1.union(s2))
s1.intersection(s2)  # Intersection of Set 1 and Set 2
print("Intersection of Set 1 and Set 2:", s1.intersection(s2))

# Dictionary & Dictionary Methods
D1 = {"name": "Alice", "age": 25, "city": "New York"}
D2 = {"name": "Bob", "age": 30, "city": "Los Angeles"}
print(type(D1))  # Print the type of the dictionary
print("Dictionary 1:", D1)
print("Dictionary 2:", D2)
D1["age"] = 26  # Update the age in Dictionary 
print("Dictionary 1 after updating age:", D1)
D1["country"] = "USA"  # Add a new key-value pair to Dictionary
print("Dictionary 1 after adding country:", D1)
D1.pop("city")  # Remove the key "city" from Dictionary 1
print("Dictionary 1 after removing city:", D1)
print(D1.keys())  # Print the keys of Dictionary 1
print(D1.values())  # Print the values of Dictionary 1
print(D1.items())  # Print the items (key-value pairs) of Dictionary 1

# Conditional Statements
a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Match-Case Statement -- Python 3.10+(Switch Case)
day = "Monday"
match day:
    case "Monday":
        print("It's the start of the week!")
    case "Tuesday":
        print("It's Tuesday, keep going!")
    case "Wednesday":
        print("We're halfway through the week!")
    case "Thursday":
        print("Almost there, it's Thursday!")
    case "Friday":
        print("It's Friday, the weekend is near!")
    case "Saturday":
        print("It's Saturday, enjoy your weekend!")
    case "Sunday":
        print("It's Sunday, relax and recharge!")
    case _:
        print("Not a valid day of the week!")

# write a python program  to print table of a number which is from 1 to 10
num = int(input("Enter a num to print it's table:  "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   
    print("----")  # Print a separator line

# looping in python
# For Loop
for i in range(1, 10):
    print(i)  # Print numbers from 1 to 9

# While Loop
j = 1
while j < 10:
    print(j)  # Print numbers from 1 to 9
    j += 1  # Increment j by 1

# Break and Continue Statements
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i is 5
    print(i)  # Print numbers from 1 to 4 
    if i % 2 == 0:
            print("Skipping even number:", i)
            continue  # Skip the rest of the loop for even numbers  
    print(i)  # Print numbers from 1 to 9 
    print("Continuing the loop at i =", i)

# Nested Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")  # Print the values of i and j
    print("----")  

# Functions in Python
def greet(name, ending):
    """Function to greet a person by name."""
    print(f"Hello" + name)
    print(f"Goodbye" + ending)
print("This is a function to greet a person by name.")
greet(" Alice", " Bob")

def letter_gen(name, date):
    st = f"hi this is {name} and today is {date}"
    print(st)
letter_gen("Alice", "18th August 2025")

def avg(a, b, c):
    """Function to calculate the average of three numbers."""
    return (a + b + c) / 3
print("The average of 10, 20, and 30 is:", avg(10, 20, 30))

 # Exception Handling in Python
try:
    a = int (input("Enter a number: "))
    print( a + 3)
except ValueError as e:
    print("Invalid input! Please enter a valid number.")
    print("Error details:", e)


# File-I/O in Python
s = "I am a good a boi"
with open("output.txt", "w") as file:
    file.write(s)  # Write the string to the file
fp = open("output.txt", "w")
fp.write(s)  # Write the string to the file
fp.close()  # Close the file

with open("output.txt", "r") as file:
    content = file.read()  # Read the content of the file
    print("Content of the file:", content)  # Print the content of the file
with open("output.txt", "a") as file:
    file.write("\nAppending this line to the file.")  # Append a line to the file

# # OOP in Python

class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")

Harry = Employee("Rohan", 30, "Software Engineer")
print("Employee Information:")
Harry.display_info()  # Display the information of the employee
