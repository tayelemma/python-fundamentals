# Python has functions for creating, reading, updating, and deleting files. 
myFile = open('myfile.txt', 'w')

print("File name:", myFile.name)
print("Is Closed: ", myFile.closed)
print("Mode: ", myFile.mode)

# Write to a file
myFile.write("I love python.")
myFile.write("I also love JavaScript.")
myFile.close()

# After closed to add a txt, mode has to be 'a' append
# mode 'w' write will override the existing file
# Append to a file
myFile = open('myfile.txt', 'a')
myFile.write(" I like using both python and javascript for my project.")
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
file_to_read = myFile.read()
print(file_to_read)