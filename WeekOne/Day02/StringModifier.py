"""
Modify String
"""
a = "Hello, World!"
print(a.upper())
print(a.lower())

a = " Hello, World! " # white space form befinning or end will be removed by strip()
print(a.strip())

a = "This is the text to split the word into two places at the word. This is also the word that he is tring to change"
print(a.split("word"))

print(a.replace("is", "was"))

#f-String 
age = 40
txt = f"My name is Taye, I am {age} years old."
print(txt)

# Modifier : and .2f to add a fixed decimal
price = 59
txt = f"The price is {price:.1f}"
print(txt)

# placeholder 
txt = f"The price is {20 * 59:.6f} dollars"
print(txt)

# escape characters
txt = "We are the so-colled \"Vikings\" from the north. "
print(txt, "######")

# \n
txt = "I'm inserting a new line \nafter this."
print(txt)

# \r carriage return 
txt = "This is the carriage return \rcheck"
print(txt)

# \t
txt = "I'm inserting a tab \tafter this text on the same line."
print(txt)

# \b backspace
backsp = "This is backspace \bafter this text."
print(backsp)

# \f Form Feed
formFeed = "This is to check form feed \fwhat is this."
print(formFeed)


# formFeed = formFeed.encode()
# formFeed = formFeed.casefold()
formFeed = formFeed.center(1)

print(formFeed)

tran = "aliminate"
myDict = {97: 65}
print(tran.translate({97: 65})) # ascii code 97(a) into 65(A)

makeTran = "Hello Sam"
myTable = makeTran.maketrans("S", "P")
print(myTable) # This will give you the ascii dict {83: 80}
print(makeTran.translate(myTable)) # This will give you "Hello Pam"

# lit  = ("one", "two", "three")
# ta = dict({"name": "taye", "age": 40, "education": "CS"})
# ta = list(("a", "b", "c", "d"))
# ta = tuple(("one", 1, "sew", [1,2,3]))
# print(ta)