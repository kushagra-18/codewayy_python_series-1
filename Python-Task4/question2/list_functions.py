# Declaring and defining the functions

# Function to calculate the square of a number
def calculateSquare(number ):
    square = number * number
    return(square )

# Function to find the maximum number from a list
def findMaximum(list, length):
    Maximum = list[0]
    for i in range(1, length):
        if(list[i] > Maximum):
            Maximum = list[i]
    return(Maximum)

# Function to find the mimimum number from a list
def findMinimum(list, length):
    Minimum = list[0]
    for i in range(1, length):
        if(list[i] < Minimum):
            Minimum = list[i]
    return(Minimum)

# Function to find the sum of the list
def findSum(list, length):
    Sum = 0
    for i in range(1, length):
        Sum += list[i]
    return(Sum)
