# QUESTION1
  
# Initializing matrix 
listMatrix = [] 

# Taking input from user
no_of_Row = int(input("Enter the number of rows:")) 
no_of_Column = int(input("Enter the number of columns:"))
print("Enter the entries row wise:")

# Loop for row entries 
for i in range(no_of_Row):         
    a =[]
    
    # Loop for column entries 
    for j in range(no_of_Column):      
         a.append(int(input())) 
    listMatrix.append(a) 
print()
  
# Printing the matrix
print("The matrix formed is: ")
for i in range(no_of_Row): 
    for j in range(no_of_Column): 
        print(listMatrix[i][j], end = " ") 
    print()
print()

# Checking each element of matrix whether it is a prime number or not and printing the prime numbers
print("The prime numbers from the matrix are: ")
for i in range(no_of_Row): 
    for j in range(no_of_Column): 

        # If given element of matrix is greater than 1
        if( listMatrix[i][j] > 1):

            # Iterating from 2 to no_of_Row / 2  
            for p in range(2, listMatrix[i][j]):

                # If matrix[i][j] is divisible by any number between 2 and Row / 2, it is not prime 
                if(listMatrix[i][j] % p) == 0:
                    break
            else:
                # Printing the element of the matrix which is a prime number
                print(listMatrix[i][j])






        

                 











