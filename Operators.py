# Arithmetic Operations
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Undefined")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
arithmetic_operations(num1, num2)

# Increment and Decrement Operators
def increment_decrement():
    a = 0
    a += 1
    a = a + 1
    print("Incremented value:", a)

    print("Incremented for loop:")
    for i in range(5):
        print(i)
    
    print("Decremented for loop:")
    for i in range(4, -1, -1):
        print(i)

increment_decrement()

# Check if Two Numbers are Equal
def check_equality(a, b):
    if a == b:
        print("Both numbers are equal")
    else:
        print("Both numbers are not equal")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
check_equality(a, b)

# Relational Operators
def relational_operators(a, b):
    print(a, "<", b, ":", a < b)
    print(a, "<=", b, ":", a <= b)
    print(a, ">", b, ":", a > b)
    print(a, ">=", b, ":", a >= b)
    print(a, "==", b, ":", a == b)
    print(a, "!=", b, ":", a != b)

relational_operators(4, 5)

# Find the Smaller and Larger Number
def find_larger_smaller(a, b):
    print("Larger number:", a if a > b else b)
    print("Smaller number:", a if a < b else b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
find_larger_smaller(a, b)
