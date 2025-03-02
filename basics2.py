#String Indexing
str = "Hello world!!"
print(str[0])
print(str[-2])


#Immutability
# str[0] = 'h' # will give error as strings are immutable 


#Built in methods
print(len(str))
print(max([1,2,3,4,5,6,7]))
print(all([1,2,3,4,5,6,7]))


#Booleans
print()
print(10 > 9)
print(10 == 9)
print(10 < 9) 

#Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)


# Lists slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])
print(a[0::2])
print(a[-1::-2])


# Matrix
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   

print("3rd column =", column)


print()

import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
print(A)

A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
print(A)

print()


#List Methods
l = [1,2,3,4,5,6]
print(len(l))
l.append(9)
l.append('apple')
print(l)
l.reverse()
print(l)
l.pop(1)
print(l)
l.remove('apple')
print(l,'\n')


# List unpacking
a, b, c = [1, 2, 3]
print(a, b, c,'\n')


# None 
x = None
if x:
  print("Do you think None is True? \n")
elif x is False:
  print ("Do you think None is False? \n")
else:
  print("None is not True, or False, None is just None... \n") 


# Dictionaries
person = {"name": "Alice", "age": 25}
print(person["name"],'\n')


# Dictionaries keys and methods
person = {"name": "Alice", "age": 25}
print(person.keys())
x = person.items()
print(x,'\n')


# tuples
tuple_example = (1, 2, 3)
print(tuple_example[0],'\n')
# tuple_example[0] = 1 # will throw error because tuple are immutable


# sets
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers,'\n') 