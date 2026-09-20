""" 
Bitwise Operators
Bitwise operators are used to compare (binary) numbers: 
 -> & AND: sets each bit to 1 if both bits are 1
 -> | OR: sets each bit to 1 if one of the bits is 1
 -> ^ XOR: Sets each bit to 1 if one of the two bits is 1
 -> ~ NOT: Inverts all the bits
 -> << Zero fill left shift: let the leftmost bits fall off
 -> >> Signed right shift: let the rightmost bits fall off

"""

print(3 << 2)
print(3 << 1)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the right:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010
print(6 & 3)
""" 
The binary representation of 6 is 0110
The binary representation of 3 is 0011
Then the & operator compares the bits and returns 0010, which is 2 in decimal. 
"""



# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101
print(6 | 3)
""" 
The binary representation of 6 is 0110
The binary representation of 3 is 0011
Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
"""