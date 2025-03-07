# Write a program to print your name.

print ("Kashish") 

# Write a program for a Single line comment and multi-line comments.

# Read the input from the user
# Perform some operations on the input data
# Output the result
print("Multi-line commenting")

# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a = -5
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

a = 5
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a) # Program to print your name
name = "Kashish"
print(name)

# Single-line comment example:
# This is a single-line comment

# Multi-line comment example:
'''
This is a multi-line comment.
It spans multiple lines.
'''

print("Multi-line commenting")

# Define variables for different Data Types and print them
a = -5
b = 0  
c = 5  
d = "Hello"  

print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)
print("Value of d:", d)

# Demonstrating local and global variables
a = 5  

def f():
    print("Inside f():", a) 

def g():
    a_local = 2  
    print("Inside g():", a_local) 

def h():
    global a  
    a = 4
    print("Inside h():", a)

print("Global:", a)
f()
print("Global:", a)
g()
print("Global:", a)
h()
print("Global:", a)

# Uses global keyword to modify global 'a'
def h():
    global a
    a = 4      
    print('Inside h() : ', a)  

print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
