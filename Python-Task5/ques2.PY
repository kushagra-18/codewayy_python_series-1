# QUESTION2

# USING MATH FUNCTIONS

# IMPORTING MATH MODULE
import math
print("using math functions\n")
# Calculating power
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
calPower = math.pow(number1, number2)
print("Power:",calPower)

# Using ceil function
number1 = float(input("Enter a number: "))
calCeil = math.ceil(number1)
print("Ceil value:",calCeil)

# Using factorial function
number3 = int(input("Enter a number: "))
calFactorial = math.factorial(number3)
print("Factorial:",calFactorial)

# Using sqrt function
number4 = int(input("Enter a number: "))
calSquareroot = math.sqrt(number4)
print("Square root:",calSquareroot)


# Using sin function
valTheta = int(input("Enter the theta value: "))
calSin = math.sin(valTheta)
print("Sin(x):",calSin)


# USING SORT FUNCTION

# Declaring and defining functions
# Function for List
def sortList(myList):
    # Sorting the List
    myList.sort()
    print("Sorted List is:",myList)

# Fucntion of tuple
def sortTuple(tupleList):
    # Sorting a tuple
    sortedTuple = sorted(tupleList)
    print("Sorted tuple is:",sortedTuple)

# Function for set
def sortSet(Set1):
     # Sorting a set
     sortedSet = sorted(Set1)
     print("Sorted set is:",sortedSet)

print("using sort function\n")
# Working with lists
# Declaring an empty list
myList = []

# Taking user inputs
listSize = int(input("Enter the size of list: "))
for index in range(listSize):
    listElement = int(input("Enter list element:"))
    myList.append(listElement)
print("List entered is:", myList)

# calling the function
sortList(myList)
print()

# Working with tuples
# Declaring an empty tuple
tupleList = []

# Taking user inputs
line = input("Enter the list of tuples:\n")
while(line != ""):
    tupleList.append(tuple(line.split()))
    line = input()
print("Entered Tuple is:",tupleList)

# calling the function
sortTuple(tupleList)
print()

# Working with sets
# Declaring an empty set
Set1 = set()

# Taking user inputs
setSize = int(input("Enter the size of set:"))
for index in range(setSize):
    setElement = int(input("Enter set element:"))
    Set1.add(setElement)
print("Entered Set is:",Set1)

# calling the function
sortSet(Set1)
print()

