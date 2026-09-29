x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)# 15/4 = 3 times remender 3
print(x ** y)
print(x // y) # return 7 floor
print(4/2) # return float 2.0

ternary = 4

x = "WEEKEND" if ternary > 5 else "Workday"

print(x)
"""
Ternary Operator elif
Assign:
- "Fri" if num is 5
- "Sat" if num is 6
- "Sun" if num is 7
- otherwise assign "weekday":"""

num = 6

y = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(y)

#Comparison operators return True or False based on the comparison:
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)