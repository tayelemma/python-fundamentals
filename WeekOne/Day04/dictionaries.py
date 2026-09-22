"""
    A Dictionary is a collection which is unordered, changeable and indexed. No duplicate 
"""#
# dict constractor
name_dict = dict({"first_name": "Brat", "last_name": "Traversy"})
print(name_dict)

person = dict(first_name='Sara', last_name = "Williams")
print(person)

# Get Value
print(person.get('last_name'))

# Add
person['phone'] = '555-555-5555'
print(person)

# Get items
print(person.items())

# Copy dict
person_copy = person.copy()
person_copy['City'] = 'Boston'
print("Copy:", person_copy)
print("Original: ", person)

# Get length
print(len(person_copy))

# Remove 
del(person_copy['last_name'])
person_copy.pop('phone')
print("After last_name and phone removed: ", person_copy)

# Clear
person_copy.clear()
print("After it cleared: ", person_copy)

car_dict = {"Make": "Toyota", "Model": "RAV4", "Year": 2026}
print(type(car_dict))
print(car_dict)

# Update
car_dict.update({"Make": "Lexus"})
print(car_dict)

# update to insert
car_dict.update({"Color": "Silver"})
print(car_dict)

# Keys
print(car_dict.keys())

# Values 
print(car_dict.values())

"""
 List of dict
"""
employe = [
    {"first_name": "Martha", "last_name": "Kudoba", 'position': 'Developer'},
    {"first_name": "Teo", "last_name": "David", "position": "product manager"}
]
print(employe[0])