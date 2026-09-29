"""
Membership Operators
Membership operators are used to test if a sequence is presented in an object:
Also, checks if a value exists in a sequence
-> in
-> not in

"""

fruits = ["apple", "banana", "cherry"]
# Check if banana is present in a list
print("banana" in fruits) #True
# Check if pineapple not in fruits
print("pineapple" not in fruits) # True

""" 
    Membership in Strings

"""

string = "Hello, World!"
print("**********************************")
print("string: 'Hello, World!' ")
print("is 'W' in the string", "W" in string) #True
print("is w in the string: ", "w" in string) # False case sensitive 
print("is z not in the stirng: ", "z" not in string)