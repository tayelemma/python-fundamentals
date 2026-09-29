"""
 composition: "own a" relationship
            : The composed object directly owns its components, which cannot exist independently.
"""

class Car:
    def __init__(self,make, model, wheel_size, horse_power):
       self.make = make
       self.model = model
       # This is composition: creating object inside class car 
       # It has 'own a' relationship
       self.engine = Engine(horse_power) 
       self.wheel = [ Wheel(wheel_size) for wheel in range(4)] # list comprehension

    def display_car(self): 
        return f"{self.make}  {self.model} has {self.engine.horse_power} horse power and {self.wheel[0]} in wheel"

class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


car1 = Car(make="ford", model="Mustang", horse_power=500, wheel_size=18)
print(car1.display_car())
