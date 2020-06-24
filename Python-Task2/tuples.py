#Working with Tuples in Python

#Creation of Tuples
Tuple1 = (1,7,3,5)
print(Tuple1)

#Creating Nested Tuples
Tuple2 = (2,0,(4,6),8)
print(Tuple2)

#Joining two Tuples
joinedTuples = Tuple1 + Tuple2
print(joinedTuples)

#Slicing a list
slicingTuple = joinedTuples[1:4]
print(slicingTuple)

#Comparing Tuples
Tuple1 == Tuple2

#Deleting Tuples
del joinedTuples
print("joinedTuples deleted")

#len() Method
Length = len(Tuple2)
print("Length of Tuple2 is: ",Length)

#max() Method
Maximum = max(Tuple1)
print("Maximum from Tuple1 is: ",Maximum)

#min() Method
Minimum = min(Tuple1)
print("Minimum from Tuple1 is: ",Minimum)

#Index Method
Index = Tuple2.index(2)
print(Index)

#Count() Method
Count = Tuple1.count(7)
print("Count = ",Count)


#tuple() Method
stringTuple = tuple("abc")
print("Tuple from string 'abc' is: ",stringTuple)
