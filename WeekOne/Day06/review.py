# Reversing word in python
text = "This is python course"

splitText = text.split()
print("Splited Word: ", splitText)

value = " ".join(splitText[::-1])
print("Reverse Word: ", value)
