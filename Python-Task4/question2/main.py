# Main file

# importing the files which contains user defined functions
import list_functions
import string_functions
import operator_functions

# Declaring an empty list 
list = []

# Taking input from the user
listSize = int(input("Enter the number of elements: "))
for index in range (0, listSize):
        element = float(input("Enter the list element"))
        list.append(element)

# Using list_functions
square = list_functions.calculateSquare(list[0])
print("Square of first element of list is ",square)

listMaximum = list_functions.findMaximum(list, listSize)
print("Maximum element of list is ",listMaximum)

listMinimum = list_functions.findMinimum(list, listSize)
print("Minimum element of list is ",listMinimum)

listSum = list_functions.findSum(list, listSize)
print("Sum of elements of list is ",listSum)

print()

# Taking input from the user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Using string_functions
stringLength1 = string_functions.findLength(string1)
stringLength2 = string_functions.findLength(string2)
print("Length of first string: ",stringLength1)
print("Length of second string: ",stringLength2)

midChar = string_functions.findMiddle(string1, stringLength1)
print("Middle character of first string: ",midChar)

no_of_Vowels = string_functions.countVowels(string1)
print("Number of vowels in first string: ",no_of_Vowels)

no_of_Words = string_functions.countWords(string2, stringLength2)
print("Number of words in second string: ",no_of_Words)

# Taking input from the user
value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))

# Using operator_functions
operator_functions.operatorAnd(value1, value2)

operator_functions.operatorOr(value1, value2)

operator_functions.operatorNot(value1)





