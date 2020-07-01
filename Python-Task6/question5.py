# QUESTION5

# Declaring and defining a function
def countWords(string):
   wordCount = 1
   for i in range(len(string)):
        if(string[i] == ' ' or string == '\n' or string == '\t'):
            wordCount += 1
   return wordCount

# Taking user input
string = input("Enter a string :")

# Calling of the function
totalWords = countWords(string)
print("Total Number of Words in our input string is: ", totalWords)
