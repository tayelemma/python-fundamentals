from user import User

class Customer(User):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = 0 # adding additional property

    # Overriding method 
    def greeting(self):
        print(f"Hi my name is {self.first_name} {self.last_name} and I'm {self.age} years old. I have {self.balance} in my account.")

    # define a method 
    def set_balance(self, balance):
        self.balance = balance


# Instance 
# customer_one = Customer("Tom", "Brady", 58)
# customer_one.greeting()

# customer_two = Customer("Alex", "William", 22)
# customer_two.set_balance(50000)
# customer_two.greeting()

        