"""
Advantages: 
  Code will be self documented
  Drop down options will be adjusted to the given type anotaion value
  Error hint: runtime error
"""
# Variable Anotaion
number: int = 100
text: str = "Hello World"
lists: list = [0, 1, 2, 5, 7, 7] # Ordered
tpl: tuple = (1,2)
dic: dict = {'name': "Tim", "ownCar": True}
sets : set = {'one', 'two', 'three'}


# Functions Anotaion
def myFunction(name: str, age: int) -> dict:
    return {"name": name, "age": age}

person = myFunction('Teo', 20)
print(type(person))

print(person['name'])
print(person.keys())
print(person.values())
person['address'] = '222 W. Irving Park st.'
print(person)

# Class Anotaion: 
class Car:
    def __init__(self, make : str, model : str, year : str):
        self.make = make
        self.model = model
        self.year = year

    def displayCar(self) -> dict: 
        return {
            "Make": self.make,
            "Model": self.model,
            "Year": self.year
        }

carOne: Car = Car('Toyota','RAV4', '2026')
print(carOne.displayCar())

# CLI input 
value = input("Enter your name: ")
age = input("Please enter your age: ")


print(f' Hi, my name is {value} and I"m {age}')
    