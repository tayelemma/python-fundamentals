#1. Multiple inheritance: Allows a drived class to combine attributes and behaviors from several independent base classes.

class Flayer:
    def fly(self):
        return "I can fly."

class Swimmer:
    def swim(self):
        return "I can swim"

# Inherits from both Flayer and Swimmer
class Duck(Flayer, Swimmer):
    def quack(self):
        return "Quack!"

duck_one = Duck()

print(duck_one.fly())
print(duck_one.swim())

# The Dimond Problem and Method Resolution Order (MRO)
"""
    When using multiple inheritance, a conflict can raise if two parent classes define
    a method with the exact name ( known as the dimond problem or naming collision).
    check (MRO) of a class using class_name.__mro__
"""
class A:
    def process(self):
        return "Process from A"

class B(A):
    def process(self):
        return "Process from B"

class C(A):
    def process(self):
        return "Process from C"

# Inherits from B and C
class D(B, C):
    pass

# Python checks D, then B, then C, then A
print(D.__mro__) 
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

obj = D()
print(obj.process())  # Output: Process from B (because B comes before C in definition)



#2. Multilevel Inheritance in Python
""" 
Multilevel inheritance creates an ancestry chain where features are 
passed down through successive generations: a base class is inherited 
by a child class, which in turn is inherited by a grandchild class.
"""

class Grandparent:
    def legacy(self):
        return "Wisdom of the elders."

class Parent(Grandparent):
    def career(self):
        return "Established family business."

class Child(Parent):
    def hobby(self):
        return "Coding and gaming."

# Usage
me = Child()
print(me.hobby())    # Output: Coding and gaming. (Own method)
print(me.career())   # Output: Established family business. (Inherited from Parent)
print(me.legacy())   # Output: Wisdom of the elders. (Inherited from Grandparent)

