
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
