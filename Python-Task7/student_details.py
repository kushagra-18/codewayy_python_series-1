# Question1

# importing math
import math

#yo

# creating a class Student
class Student :
    # class variables
    no_of_Students = -1
    no_of_Subj = 3

    # constructor function for initializing values
    def __init__(self, firstName, lastName, studCollege, studBranch, subjMark1, subjMark2, subjMark3) :
        self.firstName = firstName
        self.lastName = lastName
        self.studCollege = studCollege
        self.studBranch = studBranch
        self.subjMark1 = subjMark1
        self.subjMark2 = subjMark2
        self.subjMark3 = subjMark3

        # keeping the count of number of students
        Student.no_of_Students += 1

    # function to display full name
    def dispFullname(self) :
        fullName = self.firstName +" "+ self.lastName
        print("Name of student: ",fullName)

    # function to display college name and branch
    def dispCollegeBranch(self):
        print("College: ",self.studCollege)
        print("Branch: ",self.studBranch)

    # function to print total marks obtained
    def dispTotalMarks(self):
        studTotal = self.subjMark1 + self.subjMark2 + self.subjMark3
        print("Total marks obtained: ",studTotal)
        return studTotal

    # function to print the percentage of student
    def calPercentage(self, totalMarks):
        Percentage = math.ceil((totalMarks / (Student.no_of_Subj)))
        print("Percentage: ",Percentage)
        return (Percentage)

    # function to calculate grade of the student
    def calGrade(self, Percentage):
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


# function to display all the required details
def displayDetails(student,n):
    print("Student ",n)
    student.dispFullname()
    student.dispCollegeBranch()
    totalMarks = student.dispTotalMarks()
    Percentage = student.calPercentage(totalMarks)
    studGrade = student.calGrade(Percentage)
    print("Grade: ",studGrade)
    print()

# function to take user input
def inputDetails(studList):
    print("Enter details for student:")  
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    studCollege = input("Enter college name: ")
    studBranch = input("Enter branch: ")
    subjMark1 = int(input("Enter marks for subject 1: "))
    subjMark2 = int(input("Enter marks for subject 2: "))
    subjMark3 = int(input("Enter marks for subject 3: "))
    print()

    # creating object
    studObj= Student(firstName, lastName, studCollege, studBranch, subjMark1, subjMark2, subjMark3 ) 

    # adding the created object to the list
    studList.append(studObj) 


# Create a list to add Students 
studList =[] 

# an object of Student class 
studObj = Student('', '', '', '', 0, 0, 0)
num = int(input("Enter no. of students:"))

# calling inputDetails()
for i in range(0, num):
    inputDetails(studList)
    
# finding total no. of students
print("Number of students: ",Student.no_of_Students)

print("Details:")

# printing the details by calling the displayDetails()
for i in range(studList.__len__()):
    displayDetails(studList[i], i+1)


