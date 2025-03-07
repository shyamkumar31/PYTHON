class Super:
    def __init__(self, var1, var2, var3): 
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    
    def displayPublicMembers(self):
        print("Public Data Member:", self.var1)
    
    def _displayProtectedMembers(self):
        print("Protected Data Member:", self._var2)
    
    def __displayPrivateMembers(self):
        print("Private Data Member:", self.__var3)
    
    def accessPrivateMembers(self):
        self.__displayPrivateMembers()

class Sub(Super):
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)
    
    def accessProtectedMembers(self):
        self._displayProtectedMembers()

obj = Sub("KG", 5, "KG !")

obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

print("Object is accessing protected member:", obj._var2)

print("Accessing private member using name mangling:", obj._Super__var3)
