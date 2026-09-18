import sys

# Module importing is done using the import statement. The sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
print(sys.version)

print("Hello, World!")


# Indentation indicate a block of code
if 5 > 2:
 print("Yes, 5 is greater than 2")

#  The number of space s used for indentation is up to you as a programmer, but it must be at least one. You must use the same number of spaces in the same block of code, otherwise Python will give you an error.
if 5 > 2:
    print("Yes, 5 is greater than 2")
if 5 > 2:
        print("Yes, 5 is greater than 2")
        print("Yes, 5 is greater than 2")


# Variables are containers for storing data values.
# In Python, variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 5
# x = "Sally"
print("This is the Value of x with out conversion: " ,x)
print("This is the Type of x before conversion: " , type(x))
x = str(x)
print("This is the Type of x after conversion: " , type(x))
y = "John"
z = len(x + y)  # len() function returns the length of a string
print("This is the Value of x: " ,x)
print("This is the Value of y: " ,y)
print("This is the Value of z: " ,z)

print("Statement"); print("separated by semicolons"); print("are the followings")


# Print by default ends with a new line

# Print without a new line
print("Hello World", end=" ")
print("I will print on the same line")

print("Mixing number ", 35 , "and the next word")