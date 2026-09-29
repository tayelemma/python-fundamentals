# Comparison Operators (=, !=, >, <, >=, <=) used to compare values

# Simple if
x = 50
y = 50

if x > y:
    print(f'Yes, {x} is greater than {y}')

# if/else
if x > y: 
    print(f'Yes, {x} is greater than {y}')
else:
    print(f'No, {y} is greater than {x}')

# elif
if x > y: 
    print(f'Yes, {x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'No, {y} is greater than {x}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operator ( and , or , not)
x = 3
y = 5
if x > 2 and x <= 10:
    print(f' {x} is greater than 2 and less than or equal to 10')


# Membership Operators
num_list = [1,3,5,7, 9, 11]
if 2 in num_list: 
    print(f'{2} is in the list')
else:
    print(f'{2} is not in the list')

if 2 not in num_list:
    print(f'{2} is not in the list')