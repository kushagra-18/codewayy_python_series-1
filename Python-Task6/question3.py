# QUESTION3

def upperlowerCount(string): 

    # Declaring variables
    upperCount = 0
    lowerCount = 0
  
    # Iterating to count the number of lower case and upper case letters according to ASCII values
    for i in range(len(string)): 
          
        # For lower letters 
        if (ord(string[i]) >= 97 and ord(string[i]) <= 122): 
            lowerCount += 1
  
        # For upper letters 
        elif (ord(string[i]) >= 65 and ord(string[i]) <= 90): 
            upperCount += 1
  
    print('Lower case characters = %s' %lowerCount,'Upper case characters = %s' %upperCount) 
  
# Taking user input 
string1 = input("Enter a string:")

# Calling the function
upperlowerCount(string1) 
