# Declaring and defining the functions


# Function for and operator
def operatorAnd(a, b):
    if a > 10 and b > 10: 
        print("Both the numbers are greater than 10") 
    else: 
        print("Both the numbers are smaller than 10")


# Function for or operator
def operatorOr(a, b):
    if a > 10 or b > 10: 
        print("Atleast one number is greater than 10") 
    else: 
        print("Both the numbers are smaller than 10")


# Function for or operator
def operatorNot(a):
    print(not(a > 5 and a < 10))

