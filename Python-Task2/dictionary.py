#Working with Dictionary in Python

#Colors name is written in 'key' and color code is in 'values'

#Creating a Dictionary 
Colors = {"red" : "#FF0000", "white" : "#FFFFFF", "blue" : "#0000FF", "green" : "#008000", "black" : "#000000"}
print(Colors)

#The keys() function will retirn the key of a colors, i.e color name
print(Colors.keys())

#The items() fucntion will return the dictionary with both keys and values which is called an item
print(Colors.items())

#The values() function will return the list of values i.e code
print(Colors.values())

#Changing the code of blue, key to #00FF00
Colors["blue"] = "#00FF00"
print(Colors)

#Looping through dictionary, printing all key name one by on
for index in Colors:
  print(index)

#Looping through dictionary, printing all the values one by on
for x in Colors.values():
  print(index)

#Looping through dictionary, printing all the keys and values one by on
for x, y in Colors.items():
  print(x, y)

#Adding new items
Colors["Purple"] = "#800080"
print(Colors)