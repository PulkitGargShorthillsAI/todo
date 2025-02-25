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
    print("Truthy")
else:
    print("Falsey")