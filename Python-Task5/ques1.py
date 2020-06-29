# QUESTION1

# USING TRY EXCEPT AND RAISE

try:    
    studentName = input("Enter your name: ")
    studentAge = int(input("Enter the age: "))    
    
    if(studentAge<18):    
        raise ValueError   
    else:    
        print("Hello",studentName)
        print("You are elegible for the course.")    

except ValueError:    
    print("Hey",studentName)
    print("Your age is ",studentAge)
    print("You are not elegible for the course.")   