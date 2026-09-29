# The following will return true
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

"""
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
"""
print(bool(False), bool(None), bool(0),
bool(""),
bool(()),
bool([]),
bool({}))

# Function can return a boolean value
def myFunction() :
  return True

print(myFunction())

def myFun():
  return True

if myFun():
  print('YES')
else:
  print('NO')

#   Check if an object is an integer or not:
x = 200
print(isinstance(x, int))