# Composition
"""
 Building something by combining 
 Composition it's a 'has' relation. 
"""

class Chef:
    def cook_food(self, dish):
        print(f"Chef cooks {dish}")

class Waiter:
    def __init__(self, name, chef):
        self.name = name
        self.chef = chef

    def take_order(self, dish):
        print(f"{self.name} takes order: {dish}")
        self.chef.cook_food(dish)

amit: Chef = Chef()
waiter_raj: Waiter = Waiter("Raj", amit)

waiter_raj.take_order("Chicken fried rice")