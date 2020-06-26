# Declaring and defining the functions


# Function to find the middle character of a string
def findMiddle(string, length):
  Middle = ''
  if length % 2 != 0:
    Middle = string[length // 2]
  else:
    Middle = string[(length-1)//2] + string[length//2]
  return(Middle)


# Function to count the number of vowels in a string
def countVowels(string):
    vowels=0
    for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    return(vowels)


# Function to find the length of a string
def findLength(string):
    length=0
    for i in string:
      length += 1
    return(length)


# Function to count the number of words in a string
def countWords(string, length):
    words = 1
    for i in range(length):
        if(string[i] == ' ' or string == '\n' or string == '\t'):
            words = words + 1
    return(words)
