#Function are defined here

#Name function
def funcName(firstName, lastName):
    fullName = firstName +" "+ lastName
    return (fullName)


#Fucntion for calculating total marks
def funcMarks(listMarks):
    totalMarks = sum(listMarks)
    return (totalMarks)
    

#Function for Percentage
def funcPercentage(no_of_Subj, totalMarks):
    Percentage = totalMarks/no_of_Subj
    return (Percentage)
   

#Function for grades
def funcGrade(Percentage):
     if(int(Percentage) >= 95):
        return('A')
     elif(int(Percentage) >= 85 and int(Percentage) <= 95):
        return('B')
     elif(int(Percentage) >= 75 and int(Percentage) <= 85):
        return('C')
     elif(int(Percentage) >= 65 and int(Percentage) <= 75):
        return('D')
     else:
        return("FAILED")


#Master function which calls all the functions 
def masterFunc(fullName, totalMarks, Percentage, Grade):
    print("The name of student is ",fullName)
    print("The total marks obtained is: ",totalMarks)
    print("Your Percentage is: ",Percentage)
    print("Your Grade is: ",Grade)


#Declaring an empty list for marks
listMarks = []
    
#Taking input from the user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

no_of_Subj = int(input("Enter the number of subjects:"))
for index in range (0,no_of_Subj):
        subjMark = float(input("Enter the marks of subject"))
        listMarks.append(subjMark)

#calling funcName
fullName = funcName( firstName, lastName)
#calling funcMarks
totalMarks = funcMarks(listMarks)
#calling funcPercentage
Percentage = funcPercentage(no_of_Subj, totalMarks)
#calling funcGrage
Grade = funcGrade(Percentage)
#Calling master function
masterFunc(fullName, totalMarks, Percentage, Grade)




