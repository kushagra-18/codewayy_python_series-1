# Main file

# importing the files which contains user defined functions
import list_functions
import string_functions
import operator_functions

#Declaring an empty list 
list = []

#Taking input from the user
size = int(input("Enter the number of elements: "))
for index in range (0, size):
        element = float(input("Enter the list element"))
        list.append(element)

# Using list_functions
square = list_functions.calculateSquare(list[0])
print("Square of first element of list is ",square)

maximum = list_functions.findMaximum(list, size)
print("Maximum element of list is ",maximum)

minimum = list_functions.findMinimum(list, size)
print("Minimum element of list is ",minimum)

sum = list_functions.findSum(list, size)
print("Sum of elements of list is ",sum)

print()

#Taking input from the user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Using string_functions
length1 = string_functions.findLength(string1)
length2 = string_functions.findLength(string2)
print("Length of first string: ",length1)
print("Length of second string: ",length2)

midChar = string_functions.findMiddle(string1, length1)
print("Middle character of first string: ",midChar)

vowels = string_functions.countVowels(string1)
print("Number of vowels in first string: ",vowels)

words = string_functions.countWords(string2, length2)
print("Number of words in second string: ",words)

#Taking input from the user
value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))

# Using operator_functions
operator_functions.operatorAnd(value1, value2)
operator_functions.operatorOr(value1, value2)
operator_functions.operatorNot(value1)





