# Question4

# Declarinf and defining the function
def countOccurance(string):
    for i in string:
        string1 = string.lower()
    print("Occurences:",(string1.count("at")))
        

# Taking user input
string1 = input("Enter a String:")

# Calling of the function
countOccurance(string1)
