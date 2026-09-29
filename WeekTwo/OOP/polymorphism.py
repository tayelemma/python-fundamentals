"""
1. Built-in Function Polymorphism: a single Python function can accept different data types
   and automatically adapt its execution logic on what you pass in.
   eg. len("Python")
       len([1,2,3,4])
       len({"a": 1, "b": 2})
2. Operator Polymorphism (Operator Overloading): The same operator symbol can perform completely 
   distinct actions depending on the data types of it's operands
   eg. 5 + 10
       "hello" + "world"
       [1,2] + [3,4]
3. Class Polymorphism (Method Overriding)
-> Runtime Polymorphism: different classes can expose the exact same method name. 
   When a child class provides a specialized implementaion of a method already defined in it's 
   parent class
4. Duck Typing: Priortize object behavior over it's explicit class inheritance
   Two classes do not need to share a common parent class to be used polymorphically;
   They just need to share the same method signiture

"""

# 1. Built-in Function Polymorphism
print(len("Python") )
print(len([1,2,3,4]))
print(len({"a": 1, "b": 2}))

# 2. Operator Polymorphism (Operator Overloading)
print(5 + 10)
print("Hello" + "World")
print([1,2,3] + [3,4,5])

# 3. Class Polymorphism (Method Overriding)

class Animal: 
    def make_sound(self): 
        pass

class Dog(Animal): #inheritance
    def make_sound(self):
        return "Woof!"

class Cat(Animal): #inheritance
    def make_sound(self):
        return "Meow!"

# A unified interface to process different objects
def play_sound(animal_object):
    print(animal_object.make_sound())

play_sound(Dog()) #Woof!
play_sound(Cat()) #Meow!

# 4. Duck Typing: does not care about inheritance
# If it walks like a duck and quacks like a duck, it's a duck.
class Car: 
    def start(self):
        return "Engine roaring!"
    
class ElectricScooter:
    def start(self):
        return "Beep. System ready."

# Function only check if the method exist
def ignite_vehicle(vehicle):
    print(vehicle.start())

ignite_vehicle(Car())
ignite_vehicle(ElectricScooter())
