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
txt = f"The price is {price:.2f}"
print(txt)

# placeholder 
txt = f"The price is {20 * 59} dollars"
print(txt)