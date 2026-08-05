# Decorators -> A decorator is a function that adds extra functionality
#               to another function without changing its original code. 

# ------------------------------
# Function are objects in python 
# ------------------------------
# def greet():
#     print("Hello")
# print(greet)

# Output: <function greet at 0x..>

# You can assign it to another variable.

# def greet():
#     print("Hello!")
# say_hello = greet
# say_hello()
 
# Output: Hello

# -> Both variables point to the same function.
#     greet  --------\
#                     -----> Function
#     say_hello -----/
# -------------------------------------
# Functions can be passed as arguements 
# -------------------------------------
# def greet():
#     print("Hello")
# def execute(func):
#     func()
# execute(greet)

#  Output: Hello

# ------------------------------
# Functions can return functions 
# ------------------------------
# def outer():
#     def inner():
#         print("Inside Inner")
#     return inner
# my_function = outer()
# my_function()

# Output: Inside Inner 

# ------------------------------------------
# Functions can receive and return functions 
# ------------------------------------------
# def greet():
#     print("Hello")
# def decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper
# my_function = decorator(greet)
# my_function()

# Output: Start
#         Hello
#         End


# Wrapper -> The wrapper is simply another function.
# It wraps the original function
# wrapper takes 0 positional arguments, if given shows TypeError
# -----------------
# Before
# original Function
# After
# -----------------

# The @ Syntax ->
# Instead of writing 
#       greet = decorator(greet)
# Python gives us a shortcut
#       @decorator
#       def greet():
#           print("Hello")
# Python automatically converts it into
#       def greet():
#           print("Hello")
#       greet = decorator(greet)
# Both are exactly the same

# Decorators with arguments -> This works for any number of arguments
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         func(*args, **kwargs)
#         print("After")
#     return wrapper
# @decorator
# def greet(name):
#     print("Hello", name)
# greet("Aashik")

# Output:
#         Before
#         Hello Aashik
#         After

# Returning Values -> Always return the original result if the decorated function
#                     returns something.
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Calculating...")
#         result = func(*args, **kwargs)
#         print("Done")
#         return result
#     return wrapper
# @decorator
# def add(a, b):
#     return a + b
# print(add(5, 7))

# Output:
#         Calculating...
#         Done
#         12

# functools.wraps -> The function name, docstring, and other metadata are 
#                    preserved. This is considered best practice.
# from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
# print(greet.__name__)

# Output:
#         greet

# How Python Executes a Decorator?
# Imagine this code:
# @decorator
# def greet():
#     print("Hello")
# greet()
# Python internally performs these steps:
                    # Step 1:
                    # Create greet()

                    #         │
                    #         ▼

                    # Step 2:
                    # Pass greet to decorator()

                    #         │
                    #         ▼

                    # Step 3:
                    # decorator() creates wrapper()

                    #         │
                    #         ▼

                    # Step 4:
                    # greet = wrapper

                    #         │
                    #         ▼

                    # Step 5:
                    # Calling greet() actually calls wrapper()

                    #         │
                    #         ▼

                    # wrapper()
                    # ├── Before
                    # ├── Original greet()
                    # └── After
                    
                    



