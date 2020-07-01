# Question2

# Delcaring and defining the function that removes empty tuples from a list
def removeEmptyTuples(myList):
    # Declaring empty list
    newList = []

    # Iterating to remove empty tuples
    for i in myList:
        if i != ():
            newList.append(i)

    # Assigning the newList values to myList
    myList = newList
    print("List after removing empty tuples is:",myList)
    

# Declaring empty list
myList = []

# Taking user input
line = input("Enter the list of tuples:\n")
while(line != "end"):
    myList.append(tuple(line.split()))
    line = input()
print("List entered is:",myList)

# Calling of the function
removeEmptyTuples(myList)
