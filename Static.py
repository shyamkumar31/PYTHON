# Define a static variable and access that through a class.

class Python:
    
 staticVariable = 9 
print(Python.staticVariable)

Python.staticVariable = 12
print(Python.staticVariable) # Gives 12

instance = Python()
print(instance.staticVariable) # Gives 12


instance.staticVariable = 15
print(instance.staticVariable) # Gives 15
print(Python.staticVariable) #Gives 12
