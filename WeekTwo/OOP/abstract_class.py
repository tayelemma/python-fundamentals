from abc import ABC, abstractmethod

class Company(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def isAuthorizedEmployee(self,position):
        pass

class Employee(Company):
    def __init__(self, name, address, positions):
        super().__init__(name)
        self.address = address
        self.positions = positions

    def isAuthorizedEmployee(self, position):
        if self.positions == position:
            return True
        else:
            return False


employee1 = Employee(name = "Tom", address="1004 Fairfield 1 dr", positions="Manager")

print(employee1.isAuthorizedEmployee("Manager"))