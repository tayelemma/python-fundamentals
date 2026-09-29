import random
# Built-in Data Types
"""
    Text Type: str
    Numeric Types: int,float, complex
    Sequence Types: list, tuple, range
    Mapping Type: dict
    Set Types: set, frozenset
    Boolean Type: bool
    Binary Types: bytes, bytearray, memoryview
    None Type: NoneType
"""
x = "Hello World"
print("Str Data Type", type(x))

x = 20 
print("int Data Type", type(x))

x = 20.5 
print("float Data Type", type(x))

x = 20j
print("complex Data Type", type(x))

# List
x = [2, 4, 5, "One", "Two"]
print("list Data type", type(x), x)

#Tuple
x = ("one", 2, "three", ["four", "five"], bool(4))
print("Tuple Data Type", type(x), x)

# Dictionary
x = {"name": "Taye", "age": 40}
print("Dictionary Data Type: ", type(x), x)

# Set
x = {"apple", 1} # Tuple and list is not allowed
print("set Data Types: ", type(x), x)

#frozenset
x = frozenset({"apple", "banana", "cherry"})
print("Frozenset Data Type: ", type(x), x) #frozenset({'cherry', 'apple', 'banana'})

x = True
print("Bool data type: ", type(x), x)

#bytes
x = b"Hello"
print("bytes data type: ", type(x), x) # b'Hello'

#bytearray
x = bytearray(5)
print("bytearray data type: ", type(x), x) #bytearray(b'\x00\x00\x00\x00\x00')

#memoryview 
x = memoryview(bytes(5))
print("memoryview data type: ", type(x), x) #<memory at 0x0000015B176A5480>

# b = memoryview(complex(1j)) Not permited bytes-like object is required
# print(b)

# v= memoryview(float(1.0))
# print(v)

# u = memoryview(int(1))
# print(u)

x = None
print("NoneType data Type", type(x), x) # None


# Three types of numeric types
"""
    int
    float
    complex
"""
p = 1 #int any whole +ve or -ve whole number
q = 2.8e10 #float can be scientific numbers an "e"
z = 1j #complex

s = 3+5j
print("Complex number", type(s), s)

# Type conversion 
a = 1
b = 2.8
c = 1j

w = float(a)
print("Int convert into flaot: ", w)

i = int(b)
print("Float convert into int: ", b)

j = complex(a)
print("int convert into complex: ", j)

# Display random number 1 to 9
print(random.randrange(1,10))

mc = range(3, 10)
mc = list(mc)
print(mc)

a = """Multiple line 
string. is like this
also the third line"""
print(a)

d = "Hello, World!"
print(d[0])

# String is an Array
# Loop thourgh string

count = 0
for i in d:
    if i == "l":
        count +=1
print(count)
