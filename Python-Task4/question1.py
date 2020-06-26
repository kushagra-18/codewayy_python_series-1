# QUESTION1
  
# Initializing matrix 
matrix = [] 

# Taking input from user
Row = int(input("Enter the number of rows:")) 
Column = int(input("Enter the number of columns:"))
print("Enter the entries row wise:")

# Loop for row entries 
for i in range(Row):         
    a =[]
    
    # Loop for column entries 
    for j in range(Column):      
         a.append(int(input())) 
    matrix.append(a) 
print()
  
# Printing the matrix
print("The matrix formed is: ")
for i in range(Row): 
    for j in range(Column): 
        print(matrix[i][j], end = " ") 
    print()
print()

# Checking each element of matrix whether it is a prime number or not and printing the prime numbers
print("The prime numbers from the matrix are: ")
for i in range(Row): 
    for j in range(Column): 

        # If given element of matrix is greater than 1
        if( matrix[i][j] > 1):

            # Iterating from 2 to Row / 2  
            for p in range(2, matrix[i][j]):

                # If matrix[i][j] is divisible by any number between 2 and Row / 2, it is not prime 
                if(matrix[i][j] % p) == 0:
                    break
            else:
                # Printing the element of the matrix which is a prime number
                print(matrix[i][j])






        

                 











