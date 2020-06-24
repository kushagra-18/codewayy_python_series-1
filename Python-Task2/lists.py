#Working with lists in Python

#Creation of list
myList = [3, 9, 81,27]
print(myList)

#Creating Nested List
myList2 = [25, [45, 10]]
print(myList2)

#Joining two lists
List = myList + myList2
print(List)

#Slicing a list
slicingList = List[1:5]
print(slicingList)

#Index Method
Index = List.index(25)
print(Index)

#Append Method
myList.append(6)
print(myList)

#Extend Method
myList2.extend(myList)
print(myList2)

#Insert Method
myList.insert(3, 15)
print(myList)

#Pop Method
Element = myList2.pop(2)
print("Deleted element: ",Element)

#Remove Method
List.remove(27)
print(List)

#Clear Method
List.clear
print("List cleared")

#Count Method
Count = myList.count(9)
print("Count = ",Count)

#Reverse Method
myList.reverse();
print("Reversed list is: ",myList)

#Sort Method
myList.sort()
print("Sorted list is: ",myList)
