"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List- is a collection which is ordered and changeable. Allows duplicate members.
Tuple- is a collection which is ordered and unchangeable. Allows duplicate members.
Set- is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary- is a collection which is ordered** and changeable. No duplicate members.

"""

fruits = ["apple", "orange", "banana"]

for fruit in fruits:
    print(fruit)

append = fruits.append("pineapple")
print("After Pineapple added: ", fruits)

count = fruits.count("apple")
print(f"There are {count} fruits.")

index = fruits.index("pineapple")
print(f"Index of pineapple is {index}")

fruits.insert(3, "Kiwi") # Insert allow us to insert at specific index...
print(f"After kiwi added: {fruits}")

fruits.sort(reverse=True)
print( "Reverse sorted: ", fruits)

"""
Sort depends on the ISCI and upper -> lower 
"""
copy_fruits = []
for fruit in fruits: 
    copy_fruits.append(fruit.lower())
copy_fruits.sort()
print("Alphabetically sorted: ", copy_fruits)


"""
Allow duplicates: 
"""
cars = ["Ford", "Ford", "Chevy", "Chevy", "BMW", "Audi"]
print(cars)

"""
 Changeable:
"""

properties = ["single family", "town house", "multi family", "condo", "business"]
print(f"Properties before change: {properties}")


properties[4] = "resturant"
print(f"Properties after index 4 change: {properties}")


print( "Length of property list: ", len(properties))


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:6])
print(fruits[-4:-1])

#Change a range of item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""
List Comprehension:
newlist = [expression 'for' item in iterable if condition == True]
"""

# Without List Comprehension: 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With List Comprehension: 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x.upper() for x in fruits] # Change all in upper()
print(newlist)

newlist = [x for x in fruits if x != "apple"] #Only accept item that are not "apple"
print(newlist)


#Using range() function 
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 4]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
