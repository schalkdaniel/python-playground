'''Block comment
   Over multiple lines'''

# list
fruits = ["apple", "mango", "orange"]
print(fruits)
print(fruits[0])

# tuple
numbers = (1, 2, 3)
print(numbers)
type(numbers)

# dictionary
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)
print(alphabets["b"])

# set
vowels = {'a', 'e', 'i' , 'o', 'u'}
print(vowels)

### FLOW CONTROL:
### ====================================================

if True:
    print("True")
else:
    print("False")

a = "cat"
if a == "apple":
    print("a is an apple")
elif a == "cat":
    print("a is a cat")
else:
    print("Don't know what I am")


for alph in alphabets:
    print(alph)

for i in range(4):
    print(i)
else:
    print("DONE")


i = 0
while i < 3:
    print(i)
    i += 1

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("Done with i =", i)

i = 0
while i < 10:
    i += 1
    if ((i - 1) % 2) == 0:
        continue
    print(i)

def mySquare(num = 0):
    return num**2


import math
math.sqrt(2)

# Name of the module:
math.__name__

# Lambdas:
greetUser = lambda name : print('Hey there,', name)

