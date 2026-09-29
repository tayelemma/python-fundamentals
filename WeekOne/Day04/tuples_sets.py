# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members

fruits = ('Apple', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) # Tuple constractor

print(fruits, fruits2)

# Single value with/without traling comma
color = ('Green') # without a trailing comma
print("Without a traling comma: ", type(color)) #<class 'str'>

car = ('Toyota',) #with traling comma
print("With the trailing comma: ", type(car)) #<class 'tuple'>

# Delete tuple
# del car

print(car)
print(len(car))


"""
A Set is a collection which is unordered and unindexed. NO duplicate members.
"""
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Everytime it print different order
print("Prints different order each time: ", fruits_set)

# Check if in set
print('Apple' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove form set
fruits_set.remove('Mango')
print(fruits_set)

# Clear: 'Set is still defined and empty
fruits_set.clear()
print(fruits_set) 

# Delete: remove 'Set' and is not defined
# del fruits_set
# print(fruits_set)