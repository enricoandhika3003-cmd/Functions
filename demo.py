name = str(input("Enter your name: "))

def greetings(name):
    print("Hello, I'm", name, "!")

greetings(name)

def factorials(n):
    if n == 1:
        return n
    else:
        return n*factorials(n-1)

num = int(input("Enter a random number: "))

if num < 0:
    print("There are no factorials for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of", num, "is", factorials(num), ".")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

numA = int(input("Enter value of A: "))
numB = int(input("Enter value of B: "))

print("Sum of A and B is ", addition(numA, numB))
print("Difference of A and B is ", subtraction(numA, numB))
print("Product of A and B is ", multiplication(numA, numB))
print("Quotient of A and B is ", division(numA, numB))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

length = int(input("How many fibonacci terms? "))

for i in range(length):
    print(fibonacci(i), end=", ")