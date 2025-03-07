class Parent:  
    def display(self):
        print("Display inside Parent") 

    def show(self):
        print("Show inside Parent")
    
# First Child class inherits Parent
class Child1(Parent): 
    def print_message(self):
        print("Print inside Child1")    

    def show(self):
        print("Show inside Child1")
    
# Second Child class inherits Child1
class Child2(Child1): 
    def show(self):
        print("Show inside Child2")         

# Creating objects of each class
p = Parent()
p.display()

c1 = Child1()
c1.print_message()

c2 = Child2()   
c2.show()   
