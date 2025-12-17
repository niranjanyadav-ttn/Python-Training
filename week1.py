# Data Types
# 1. Task: Convert the following values to the specified types and print the results
# Convert 3.75 to an integer and print the value?
float_value = 3.75
int_value = int(float_value)
print("Converted float to integer:", int_value)

# Convert "123" to a float and print the value
string_value = "123"
float_value = float(string_value)
print("Converted string to Float:", float_value)

# Convert 0 to a boolean and print the value
zero_value = 0
boolean_value = bool(zero_value)
print("Zero to Boolean:", boolean_value)

# Convert False to a string and print the value
bool_value = False
string_value = str(bool_value)
print("Boolean to String:", string_value)

# 2. Convert all characters in the string to uppercase. x = "hello"
x = "hello"
x = x.upper()
print("Converted to upper case:", x)

# 3. Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer.
x = 5
y = 3.14
z = x + y
print("Data type of z:", type(z))
z_integer = int(z)
print("z as integer:", z_integer)

# 4. Given the string s = 'hello', perform the following operations:
# Convert the string to uppercase.
# Replace 'e' with 'a'.
# Check if the string starts with 'he'.
# Check if the string ends with 'lo'.
s = 'hello'
upper_s = s.upper()
print("S in uppercase :", upper_s)

replaced_s = s.replace('e', 'a')
print("After replacing 'e' with 'a':", replaced_s)

starts_with_he = s.startswith('he')
print("Starts with 'he':", starts_with_he)

ends_with_lo = s.endswith('lo')
print("Ends with 'lo':", ends_with_lo)

# Input and print
#Task 1: Write a program that asks the user for their name and then prints a greeting message using their name.
name = input("Enter your name: ")
print("Hello, " + name + " Welcome!")

# Task 2: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_res = num1 + num2
multiply_res = num1 * num2
division_res = num1 / num2

print(f"{num1} + {num2} = {sum_res}")
print(f"{num1} * {num2} = {multiply_res}")
print(f"{num1} / {num2} = {division_res}")

# Task 3: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
names = input("Enter names separated by commas: ")
names_list = names.split(',')
print("List of names:", names_list)

# Task 4: Ask the user to enter their age and check if they are eligible to vote based on their age.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

#5. For value = 3.14159, Using f-string print output for only up to 2 decimal places.
value = 3.14159
print(f"Value with 2 decimal places: {value:.2f}")

# Built-In Data Structures
# 1. Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]
maximum = max(nums)
minimum = min(nums)
print("Maximum value:", maximum)
print("Minimum value:", minimum)

# 2. Given two lists below, merge the values from both lists to one and print
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged_list = a + b
print("Merged list:", merged_list) 

# 3. From a list, print the number of times the value 3 appears in the list:
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
count = a.count(3)
print("Number 3 appears:", count, "times")

# 4. From below list, Sort the list and print
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
a.sort()
print("Sorted list:", a)

# 5. Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print("Updated set:", numbers)

# 6. Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Updated set:", numbers)

# 7. Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1.intersection(set2)
print("Intersection:", intersection)

# 8. Given a tuple, count and print the number of occurrences of the element 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')
count = fruits.count('apple')
print("'apple' appears:", count, "times")

# 9. Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)

# 10. Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
age = person["age"]
print("Age:", age)

# age = person.get("age")
# print("Age:", age)

# 11. Add new key,  gender to dictionary and assign “M” to it and print
person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print("Updated dictionary:", person)

# 12. Remove the key "city" from the above Dict and print
person = {"name": "Alice", "age": 30, "city": "New York"}
del person["city"]
print("Updated dictionary:", person)

# person.pop("city")
# print("Updated dictionary:", person)

# 13. Given two dictionaries, merge them into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print("Merged:", dict1)

# merged_dict = dict1 | dict2

# Control Flow
# For loop
# Write a program that takes the input from the user and checks if a number is even or odd.
count = int(input("How many numbers do you want to check? "))
for i in range(count):
    number = int(input(f"Enter number {i+1}: "))
    
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
strings = ["civic", "hello"]
for string in strings:
    rev_str = ""
    for char in string:
        rev_str = char + rev_str

    if string == rev_str:
        print(f"'{string}' reversed is '{rev_str}' - It is a PALINDROME")
    else:
        print(f"'{string}' reversed is '{rev_str}' - It is NOT a palindrome")

# Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
n = int(input("How many Fibonacci numbers do you want? "))
a = 0
b = 1
print(f"First {n} Fibonacci numbers:")

for i in range(n):
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
print()

# From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.
# Expected output : [4, 5]
numbers = [1, 2, 3, 4, 5]
target = 9
result = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            result = [numbers[i], numbers[j]]
            break
print(f"Sum pair indexes are : {result}")

# Use set for faster lookup (alternate)
# seen = set()
# for num in numbers:
#     diff = target - num
#     if diff in seen:
#         print(f"Expected output: [{diff}, {num}]")
#         break
#     seen.add(num)

# While loop
# Print all even numbers between 1 and 20 using a while loop.
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
print()

# Break
# Find the first occurrence of a number in a list and stop further searching. 
numbers = [10, 20, 30, 40, 50]
key = 30
for i in range(len(numbers)):
    if numbers[i] == key:
        print(f"Found {key} at index {i}")
        break

# Continue
# Using continue statement, print only the odd numbers from 1 to 10.
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

# Pass
# What will be the output 
# for i in range(5):
#     if i == 3:
#         pass  
#     print(i)

# output: 
# 0
# 1
# 2
# 3
# 4

# Match
# Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.
# Get day from user
day = input("Enter a day of the week: ").strip().lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print(f"{day.capitalize()} is a Weekday")
    case "saturday" | "sunday":
        print(f"{day.capitalize()} is a Weekend")
    case _:
        print("Invalid input! Please enter a valid day.")


#1. Define a function calculate_area that calculates the area of a rectangle and return the result.
#  If no width is provided, it defaults to 10.
def calculate_area(length, width=10):
    area = length * width
    return area

result1 = calculate_area(5, 8)
print(f"Area (5 x 8): {result1}")

result2 = calculate_area(5)
print(f"Area (5 x 10): {result2}")

# 2.  Write a recursive function to compute the factorial of a non-negative integer.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")

# 3. Write a function that takes one parameter as a string and reverse it and return.
def reverse_string(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text

print(reverse_string("hello"))

# 4. Write a Python function that takes two parameters as lists and to sum all the numbers in a list. 
# a = [8, 2, 3, 0, 7], b =  [3, -2, 5, 1] and return a value.
def sum_two_lists(list1, list2):
    total = sum(list1) + sum(list2)
    return total

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
result = sum_two_lists(a, b)
print(f"List a: {a}")
print(f"List b: {b}")
print(f"Total sum: {result}")

# 5. Write a Python function that takes a list and returns a new list with distinct and sorted elements
# from the first list. a = [4,1,2,3,3,1,3,4,5,1,7] Output = [1,2,3,4,5,7]
def get_distinct_sorted(list1):
    distinct_sorted = sorted(set(list1))
    return distinct_sorted

a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
result = get_distinct_sorted(a)
print(f"Original list: {a}")
print(f"Output: {result}")

# Given a list of numeric strings, convert them into integers. Using List Comprehensions
# strings = ["1", "2", "3", "4", "5"] #Expected output : [1, 2, 3, 4, 5]
strings = ["1", "2", "3", "4", "5"]
integers = [int(num) for num in strings]
print(f"Converted to integers: {integers}")

# Extract all integers from a list that are greater than 10. Using List Comprehensions
# numbers = [1, 5, 13, 4, 16, 7] #Expected output :[13, 16]
numbers = [1, 5, 13, 4, 16, 7]
result = [num for num in numbers if num > 10]
print(f"Expected output: {result}")

# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
# #Expected output :[1, 4, 9, 16, 25]
squares = [num**2 for num in range(1, 6)]
print(f"Expected output: {squares}")

# Convert a 2D list into a 1D list.Using List Comprehensions
# matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
# #Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened = [num for row in matrix for num in row]
print(f"Expected output: {flattened}")

# Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
# Expected output : {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(f"Expected output: {result}")

# Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
# Expected output : {'Alice': 85, 'Charlie': 90}
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
filtered_scores = {name: score for name, score in scores.items() if score > 80}
print(f"Expected output: {filtered_scores}")
