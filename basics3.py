# control flow statements
for i in range(0,20):
    if(i == 2):
        continue
    elif(i == 12):
        break
    else:
        print(i)
print()

# Conditional logic
age = 18
if age >= 18:
    print("You can vote \n")
else:
    print("You cannot vote \n")


a = 2
b = 330
print("A \n") if a > b else print("B \n") 


# Truthy and Falsy
if "":
    print("Truthy \n")
else:
    print("Falsey \n")


# Ternary operator
x = 18 if 13 > 14 else 16
print(x)

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status,'\n')  


# Short Circuiting
def check():
    print("Function called")
    return True

print(True or check())  # Short-circuits, function not called
print()

# Logical operators
x, y = True, False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False

print()

# is vs ==
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)  # Output: True (same values)
print(x is y)  # Output: False (different objects)
print(x is z)  # Output: True (same object)
print()

# for loop
for num in [1, 2, 3]:
    print(num)
print()

# iterables
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print()

# range
for i in range(3):
    print(i) 
print()



# enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print()


# while loops
count = 0
while count < 3:
    print(count)
    count += 1