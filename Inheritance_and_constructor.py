# Inheritance and constructor
class Father:
    def _init_(self,property = 0):
        self.property = 80000
    def display2(self):
        print("Fathers property is",self.property)

class Child(Father):
    def _init_(self,property=0,property1=0):
        super()._init_(property)
        self.property1 = 20000
    def display1(self):
        print("Child property is",self.property1)

s = Child()
s.display1()
s.display2()