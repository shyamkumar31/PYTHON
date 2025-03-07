# Print "Bright IT Career" 10 times
for i in range(10):
    print("Bright IT Career")

# Print numbers from 1 to 20 using a while loop
i = 1
while i <= 20:
    print(i)
    i += 1

# Equal and Not Equal Operator
a = 5
b = 10
print("a == b:", a == b)
print("a != b:", a != b)

# Print Even and Odd Numbers
for n in range(1, 11):
    if n % 2 == 0:
        print("Even:", n)
    else:
        print("Odd:", n)

# Find the Largest Number Among Three
x = 40
y = 50
z = 90
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print("Largest number is:", largest)

# Print Even Numbers Between 10 and 20 using while loop
n = 10
while n <= 20:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()

# Print Numbers 1 to 10 Using a do-while Concept
n = 1
while True:
    print(n, end=" ")
    n += 1
    if n > 10:
        break
print()

# Check If a Number is an Armstrong Number
num = int(input("Enter a number: "))
temp = num
total = 0
while temp > 0:
    digit = temp - (temp // 10) * 10  # Extract last digit
    total += digit * digit * digit
    temp = temp // 10
if num == total:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Check If a Number is Prime
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")

# Check If a Number is a Palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp - (temp // 10) * 10  # Extract last digit
    rev = rev * 10 + digit
    temp = temp // 10
if num == rev:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")

# Check If a Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
