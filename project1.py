#Create a class Calculator with methods add(), subtract(), multiply(), and divide(). Create an object and perform all operations.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

c = Calculator()
print("Addition:", c.add(25, 12))
print("Subtraction:", c.subtract(45, 47))
print("Multiplication:", c.multiply(5, 22))
print("Division:", c.divide(5, 8))
