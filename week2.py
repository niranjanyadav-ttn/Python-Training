from functools import reduce
import time
import csv
from datetime import datetime, timedelta
import os

# Given a list let's see how to double each element of the given list. Using map() 
# a = [1, 2, 3, 4] Expected Output: [2, 4, 6, 8]
a = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, a))
print(f"Output is: {result}")

# Use filter() and lambda to extract all even numbers from a list of integers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Expected Output: [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Output is : {result}")

# Use reduce() and lambda to find the longest word in a list of strings.
# from functools import reduce
# words = ["apple", "banana", "cherry", "date"] Expected Output: 'banana'
words = ["apple", "banana", "cherry", "date"]
result = reduce(lambda x, y: x if len(x) >= len(y) else y, words)
print(f"Expected Output: '{result}'")

# Use map() to square each number in the list and round the result to one decimal place.
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59] Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
result = list(map(lambda x: round(x**2, 1), my_floats))
print(f"Expected Output: '{result}'")

# Use filter() to select names with 7 or fewer characters from the list.
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# #Expected Output: ['olumide', 'josiah', 'omoseun']
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
result = list(filter(lambda name: len(name) <= 7, my_names))
print(f"Expected Output: {result}")

# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(f"Expected Output: {result}")

# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
# Input : numbers = [1, 2, 3, 4, 5] # Expected Output : True
numbers = [1, 2, 3, 4, 5]
result = all(num > 0 for num in numbers)
print(f"Expected Output: {result}")

# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
# Input: numbers = [1, 3, 5, 7, 8] Expected Output: True
numbers = [1, 3, 5, 7, 8]
result = any(num % 2 == 0 for num in numbers)
print(f"Expected Output: {result}")

# Determine if any number in a list is divisible by 5 an print.
numbers = [12, 23, 34, 45, 56]
result = any(num % 5 == 0 for num in numbers)
print(f"Any divisible by 5? {result}")
if result:
    divisible_by_5 = [num for num in numbers if num % 5 == 0]
    print(f"Numbers divisible by 5: {divisible_by_5}")

# Using below list and enumerate(), print index followed by value. 
# Input: fruits = ["apple", "banana", "cherry"]
# Output: 
# 0 apple
# 1 banana
# 2 cherry
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Using below dict and enumerate, print key followed by value
# Input: person = {"name": "Alice", "age": 30, "city": "New York"}
# Output:
# name: Alice
# age: 30
# city: New York
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples
# where each tuple contains the index and the corresponding fruit, but only for even indices.
# Output:[(2, 'banana'), (4, 'date')]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
result = [(index, fruit) for index, fruit in enumerate(fruits, start=1) if index % 2 == 0]
print(f"Output: {result}")

# Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
max_value = max(numbers)
min_value = min(numbers) 
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Given a set of numbers, find the maximum and minimum values.
# setn = {5, 10, 3, 15, 2, 20}
setn = {5, 10, 3, 15, 2, 20}
max_value = max(setn)
min_value = min(setn)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Write a Python function that takes a list of strings as input and returns
# a tuple containing the shortest and longest word from the list, in that order.
# If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
# Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
# Output: ('kiwi', 'grapefruit')
def find_shortest_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = find_shortest_longest(words)
print(f"Longest and shortest words are: {result}")

# Exception Handling
# Write a Python program that attempts to divide two numbers a = 10  b = 0
# and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error
a = 10
b = 0
try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Apply exception handling to below code and handle an exception if the index is out of range. 
# my_list = [1, 2, 3] print(my_list[5])
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index is out of range!")

# Correct this below code with appropriate exception handlings. And finally print “Execution completed”
# def safe_divide(a,b):
#       result = a / b
#       print(f"Result: {result}")
# safe_divide(1,0)
# safe_divide(1,”a”)
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Both a and b must be numbers!")
    finally:
        print("Execution completed")
safe_divide(1, 0)
safe_divide(1, "a")

# Decorater
# Write a function that appends 1 to 1000 numbers to a list and add a decorator
# to that function to calculate the start and end time. Calculate the total time taken and print.
def time_calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
    
        total_time = end_time - start_time
        print(f"Total time taken: {total_time:.6f} seconds")
        
        return result
    return wrapper

# Apply decorator to the function
@time_calculator
def append_numbers():
    my_list = []
    for i in range(1, 1001):
        my_list.append(i)
    return my_list

result = append_numbers()

# Create a parameterised decorator retry that retries a function a specified number of times.
# 	@retry(3)
#          def may_fail(name):
#                 print(f"Hello, {name}!")
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if attempt == times:
                        raise
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Alice")

# Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#     def square_root(x):
#     	return x ** 0.5
def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError(f"Argument must be positive. Got: {x}")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

try:
    result = square_root(0)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")

# Create a decorator cache that caches the result of a function based on its arguments.
# 	@cache
#       	def expensive_computation(x):
#     		print("Performing computation...")
#     		return x * x
# 	expensive_computation(5)
# 	expensive_computation(5)
# Write a cache decorator for it to check if the calculation is already performed then return the result.
def cache(func):
    cached_results = {}
    def wrapper(x):
        if x in cached_results:
            print(f"Returning cached result for {x}")
            return cached_results[x]
        else:
            print(f"Computing result for {x}...")
            result = func(x)
            cached_results[x] = result  # Store in cache
            return result
    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

expensive_computation(5)
expensive_computation(5)

# Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, 
# if a different user then responds “Access denied”.
#  	 def delete_user(user, user_id):
#     		print(f"User {user_id} deleted by {user['name']}")
# 	user1 = {'name': 'Alice', 'permissions': ['admin']}
# 	user2 = {'name': John, 'permissions': ['dev']}
# 	user3 = {'name': 'Kurt', 'permissions': ['test’']}
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print(f"Access denied for {user['name']}")
            return None
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103)

# Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10  numbers 
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
def fibonacci_generator():
    a, b = 0, 1
    
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

for i in range(10):
    print(next(fib))

# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
#   Input n=3
# Output:
# 3
# 6
# 9
# 12
# 15
# …
def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n

gen = infinite_multiples(3)

for i in range(10):
    print(next(gen))

# Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
# word = “hello”
# times = 5
def repeat_word(word, times):
    for i in range(times):
        yield word

word = "hello"
times = 5

gen = repeat_word(word, times)

for w in gen:
    print(w)

# Write a Python program to read the entire content of a file named sample.txt and display it.
# Read and display content of sample.txt
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

#  Write a Python program to count the number of words in a file named words.txt
try:
    with open('words.txt', 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        
    print(f"Total number of words in 'words.txt': {word_count}")
    
except FileNotFoundError:
    print("Error: words.txt file not found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Create a program to write the string “Hello, Python!” into a file named output.txt.
# Write string to output.txt
with open('output.txt', 'w') as file:
    file.write("Hello, Python!")

print("String written to output.txt successfully!")

# Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries
# 	data = [
#     ["Name", "Roll Number", "Marks"],
#     ["Alice", "101", "85"],
#     ["Bob", "102", "90"],
#     ["Charlie", "103", "88"]
# ]
data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("students.csv created successfully!")

# From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
def read_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_file_generator('large_file.txt'):
    print(line)

# Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)
print(person1.age)

# Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name,
#  and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print(f"Insufficient balance! Available: ₹{self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")
    
    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")
        return self.balance

account1 = BankAccount("ACC001", "Vijay Kumar", 5000)
account1.check_balance() 
account1.deposit(3000) 
account1.withdraw(2000) 
account1.check_balance()

#  Create a class Book with a class method from_string() that creates a Book instance from a string.
#   And print both attributes of the class
#  book = Book.from_string("Python Programming, John Doe")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @classmethod
    def from_string(cls, book_string):
        title, author = book_string.split(', ')
        return cls(title, author)

book = Book.from_string("Python Programming, John Doe")
print(f"Title: {book.title}")
print(f"Author: {book.author}")

#  Create a base class Animal with a method sound(). Create subclasses 
#  Dog and Cat that overrides the sound() method and call those methods.
# Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("This animal makes a sound")


# Subclass Dog
class Dog(Animal):
    def sound(self):
        print(f"{self.name} says: Woof! Woof!")


# Subclass Cat
class Cat(Animal):
    def sound(self):
        print(f"{self.name} says: Meow! Meow!")

dog = Dog("Doggy")
cat = Cat("Jangli billi")

dog.sound()
cat.sound()

# Write a code to perform multiple inheritance.
# Parent class 1
class Father:
    def __init__(self):
        self.father_name = "Rajesh"
    
    def gardening(self):
        print(f"{self.father_name} loves gardening")

# Parent class 2
class Mother:
    def __init__(self):
        self.mother_name = "Priya"
    
    def cooking(self):
        print(f"{self.mother_name} is good at cooking")

# Child class inheriting from both parents
class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Amit"
    
    def display_family(self):
        print(f"Child: {self.child_name}")
        print(f"Father: {self.father_name}")
        print(f"Mother: {self.mother_name}")

child = Child()
child.display_family()
child.gardening()
child.cooking()

# Using datetime, ​​add a week and 12 hours to a date. 
# Given date: March 22, 2020, at 10:00 AM. print original date time and new date time.
original_date = datetime(2020, 3, 22, 10, 0, 0)

print("Original Date and Time:")
print(original_date.strftime("%B %d, %Y at %I:%M %p"))

new_date = original_date + timedelta(weeks=1, hours=12)

print("\nNew Date and Time:")
print(new_date.strftime("%B %d, %Y at %I:%M %p"))

# Code to get the dates of yesterday, today, and tomorrow.
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%B %d, %Y"))
print("Today:    ", today.strftime("%B %d, %Y"))
print("Tomorrow: ", tomorrow.strftime("%B %d, %Y"))

# Write a code snippet using os module, to get the current working directory and print and create a folder “test”.
# List all the files and folders in the current working directory and remove the directory “test” that was created.
# Get the current working directory
current_dir = os.getcwd()
print("Current Working Directory:")
print(current_dir)
print()

# Create a folder named "test"
os.mkdir('test')
print("Folder 'test' created successfully!")
print()

# List all files and folders in current directory
print("Files and folders in current directory:")
items = os.listdir()
for item in items:
    print(item)
print()

# Remove the "test" directory
os.rmdir('test')
print("Folder 'test' removed successfully!")

# Write a Python program to rename a file from old_name.txt to new_name.txt.
os.rename('old_name.txt', 'new_name.txt')

print("File renamed successfully!")

# Create a file and Write a Python program to get the size of a file named example.txt 
with open('example.txt', 'w') as file:
    file.write("Hello, this is example.txt file.\n")
    file.write("This file contains some sample text.\n")
    file.write("Python file handling is easy!\n")
    file.write("We are learning to get file size.\n")
    file.write("This is the last line of the file.")

file_size = os.path.getsize('example.txt')
print(f"File size: {file_size} bytes")

# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00
date_string = "Feb 25 2020 4:20PM"

date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(date_object)

# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
original_date = datetime(2025, 2, 25)

new_date = original_date - timedelta(days=7)
print(f"New date: {new_date.strftime('%Y-%m-%d')}")

# Format the date 2020-02-25 as "Tuesday 25 February 2020"
date = datetime(2020, 2, 25)

formatted_date = date.strftime("%A %d %B %Y")
print(formatted_date)
