"""
    A for loop is used for iterating over a sequence (that is either a list, a tuple, dictionary, a set, or a string )

"""

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people: 
    print(person)

# Break
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

# Continue (will skip and continue )
for person in people: 
    if person == 'Sara':
        continue
    print(f'Person = {person}')

# range
for i in range(len(people)):
    print(people[i])

num_list = [
    [1, 2, 9, 9, 5],
    [6, 7, 8, 9, 10],
    [11,12,9,14,9]
]
num_filter = []
for i in range(len(num_list)):
   for j in num_list[i]:
       if j != 9:
           num_filter.append(j)
        
print(num_filter)

# While loop

count = 0
while count <= 10:
    print(f'count: {count}')
    count += 1
