## TASK2

### QUESTION ANSWERS

a)Why is list used?

A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]. Lists are great to use when you want to work with many related values. They enable you to keep data together that belongs together, condense your code, and perform the same methods and operations on multiple values at once. When thinking about Python lists and other data structures that are types of collections, it is useful to consider all the different collections you have on your computer: your assortment of files, your song playlists, your browser bookmarks, your emails, the collection of videos you can access on a streaming service, and more. 


b)How do lists and sets differ?

Lists are:-
 (1)Indexable - in that they have their elements in a known order which can be accessed by an integer index

 (2)Slicable - in that you can extract a group of consecutive elements based on start index and end index.

 (3)Non unique - they can contain multiple elements which are the same instances and multiple element which are different instances of an object but which are defined to be equal.

 (4)Heterogeneous - they don’t need to contain objects of the same type.

 (5)Non-hashable - Objects in a list don’t need to be hashable, so mutable Objects can be stored in a list (including other lists).

Sets are:-
 (1)Non indexable - you can not use an index to extract the nth element in the set.

 (2)Non-sliceable - since there are no indexes, there are no slices.

 (3)Unique - sets can not contain duplicates of an instance (a duplicate is defined as an object where the == operator is true - two different instances a & b of the same class cannot be stored in a set if a == b)

 (4)Heterogeneous - they don’t need to contain objects of the same type.

 (5)Hashable - Custom instances in a class must have a defined hash.


c)Application of dictionaries with a real world example.

A Python dictionary is a mapping of unique keys to values. Dictionaries are mutable, which means they can be changed. The values that the keys point to can be any Python value. Dictionaries are unordered, so the order that the keys are added doesn't necessarily reflect what order they may be reported back.
Dictionaries are useful for speedy lookup and for storing unique keys with their respective values. When you want a mapping from keys to values, use a dictionary. For example, when you want a telephone book which maps names to phone numbers: {'John Smith': '555-1212'}. Note the keys in dictionaries are unordered. (If you iterough a dictionary (telephone book), the keys (names) may show up in any order).
Say you are building a map of objects on a game field - so each object has an (x,y) co-ordinate. Instead of a big list which is mostly empty showing each of the objects - you have a dictionary with the key being a tuple of the (x,y) co-ordinate, and the value being the object at that location. 
