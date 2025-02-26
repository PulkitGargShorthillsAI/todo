# Break, Continue, Pass
for i in range(5):
    if i == 3:
        break  # Stops the loop
    print(i)
print()

for i in range(5):
    if i == 2:
        continue  # Skips iteration
    print(i)
print()

for i in range(5):
    if i == 2:
        pass  # Placeholder, does nothing
    print(i)
print()

# Functions
def greet():
    print("Hello, World!")

greet()
print()

# Parameters and Arguments
def add(a, b):
    return a + b

print(add(3, 5))
print()

# Default Parameters and Keyword Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")
print()

# Return Statement
def square(n):
    return n * n

print(square(4))
print()

# Methods vs Functions
string = "hello"
print(string.upper())  # Method
print(len(string))  # Function
print()

# Docstrings
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print(multiply(3, 4))
print()

# *args and **kwargs
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))
print()

def greet_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_all(Alice="Hello", Bob="Hi")
print()

# Scope
x = 10  # Global variable

def example():
    x = 5  # Local variable
    print(x)

example()
print(x)
print()

# Scope Rules
x = 10

def outer():
    x = 5
    def inner():
        print(x)  # Refers to x inside outer()
    inner()

outer()
print()

# Global Keyword
global_var = 10

def modify_global():
    global global_var
    global_var = 20

modify_global()
print(global_var)
print()

# Nonlocal Keyword
def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)

outer()


def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 
print()

# Why Do We Need Scope?
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
