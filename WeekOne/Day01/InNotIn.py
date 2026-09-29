# keyword "in" to check 
txt = "The best free things in life are free free free"
print("free" in txt)

counter = 0
if "free" in txt: # Does not loop; it only check if exist
    counter += 1
print("Free present in txt ", counter , " times")

print("expensive" not in txt)

# Keyword 'not in'
if "expensive" not in txt: 
    print("No, 'expensive' is Not present ")

# SLICE [start:end] and [:end] and [start: ] 
b = "Hello, world!"
print(len(b))
print(b[2:5]) # 'llo'
print(b[:5]) #  'Hello'
print(b[7:]) # world!
print(b[-6:-1]) #world -(w) included and -1(!) not included
