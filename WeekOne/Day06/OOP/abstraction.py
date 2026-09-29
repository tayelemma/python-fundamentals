""" 
    Abstract class must have atleast one abstract method. 

"""
from abc import ABC, abstractmethod

class Resturant(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def isAuthorizedToWork(self, name):
        pass

    @abstractmethod
    def work(self):
        pass

class Chef(Resturant):
    def __init__(self, name):
        self.name = name

    def isAuthorizedToWork(self, name):
        if self.name == name:
            print( f"{self.name} is authorized to work.")
    def work(self):
        print(f"{self.name} started working.")

chef_one: Chef = Chef("Mike") 

chef_one.isAuthorizedToWork("Mike")
chef_one.work()