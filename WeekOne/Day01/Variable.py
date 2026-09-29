# Variables does not need to be declared 
x=5; y="Test"
print(x,y)

# Casting used to specifiy data type
x = str(5)
print("This is string", x, "Data type:", type(x))\

y = int(3)
print("This is an int", y, "Data type: ", type(y))

z = float(3)
print("This is a float", z, "Data type = ", type(z))

# Variables are case sensitive
a = 4
A = "Sally"

print("a=", a, "=", A)

a = "Sally" #Now a is a str vlaue "Sally"
print("This is a: ", a)

# Multi word variable name
# Camel Case
myVariableName = "Every word start with capital except the first one"

# Pascal case
MyVariableName = "Every word starts with capital"

# Snack case
my_variable_name = "Every word separated by underscors"

#underscor
_myVariableName = "underscore first"


# Many Values to Multiple Variables
x, y, z = "orange", "Banana", "Cherry"

print(x); print(y); print(z)

# One value to multiple variable
n = m = o = "Orange assign to multiple variables "
print(n); print(m); print(o)


# Unpacking a collection: extracting value of list, tuple into varaibles 

fruits = ["Apple", "Banana", "Cherry"]

e, f, g = fruits

print(e); print(f); print(g)

h = 5
j = "Concat"
print(5, j)
print("word", j)
print(str(5) + " " + j)

# Global variable
 
def myfunc():
    print("Printing the h global variable inside myfunc" , h)

myfunc()

# local variable 
p = "This is global variable p."

def myLocalVariable():
    p = "This is local variable p"
    print(p)
print(p)
myLocalVariable()


# Creating global variable inside a function 
print("***********************************************")
def createGlobalVariable():
    global q 
    q = "Global"
    print(q)
    return q
var = createGlobalVariable()
print(var)
q = "Reassigning global variable q"
print(q)

# Changing a global variable inside a function
print("*****************Changing global variable inside a function *************")
k = "Global variable k"

def changingGlobalVariableK():
    global k
    k = "K Chnaged inside function"
    print(k)

print(k)
changingGlobalVariableK()
print(k)

