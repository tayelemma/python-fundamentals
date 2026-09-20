"""
Identity Operators:
Identity operators are used to compare the objects, 
not if they are equal, but if they are actually the same object, 
with the same memory location:
 -> is
 -> is not


 Difference Between 'is' and '=='
'is' - Checks if both variables point to the same object in memory
 '==' - Checks if the values of both variables are equal

"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True smae memory location
print(x is y) #False different memory location
print(x == y) #True equality check

print(x is not y) #Ture different memory location 


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) #Ture
print(x is y) #False