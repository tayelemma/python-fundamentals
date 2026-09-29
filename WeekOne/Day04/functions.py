# A function 

def sayHello(name):
    print(f"Hello {name}")

sayHello('Jhon Doe')

#Default
def sayHelloTwo(name='Sam'):
    print(f'Hello {name}')
sayHelloTwo()
sayHelloTwo('Tom')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(4,6)
print(f'Total = {num}')


# A lambda function is a small anonymous function 

get_sum = lambda num1, num2 : num1 + num2
print( "The sum is: ", getSum(10, 3))
