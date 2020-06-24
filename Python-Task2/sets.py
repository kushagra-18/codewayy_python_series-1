#Working with Sets in Python

#Intialising sets
colorSet = {"Purple", "Red", "White", "Orange"}
print(colorSet)

#Accesing sets through loops
for index in colorSet:
    print(index)
    
#Adding item using add fucntion
colorSet.add("Green")
print(colorSet)

#Adding multiple items using update fucntion
colorSet.update(["Green","Blue"])
print(colorSet)

#getting the length
print(len(colorSet))

#Removing items using discard fucntion
colorSet.discard("Blue")
print(colorSet)

#deleting using pop
Element = colorSet.pop()
print(Element)
print(colorSet)

#Using the union function to return the union of two sets
colorSet2 = {"Pink"}
mainSet = colorSet.union(colorSet2)
print(mainSet)

#Using the difference function to return the union of two sets
mainSet2 = mainSet.union(colorSet)
print(mainSet2)
