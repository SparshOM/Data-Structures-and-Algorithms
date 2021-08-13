# WAP to implement diff types of methods in Python OOP
"""
# types of methon in Python
    1. Instance Method => Object specific methods 
    2. Class methods => Whole class implementation
    3. Static methods => Do not change for class or objects
"""
class Student:
    def _init_(self,name = 'None',age = 0,number = 0):
        self.name = name
        self.age = age
        self.number = number
    def display(self):          # Instance Method
        print("Hi, my name is",self.name)
        print("My age is",self.age)
        print("My marks are",self.number)

s1 = Student('Tanishka',20,80)
s2 = Student('palak',38,90)
s2.display()
[9:48 pm, 10/08/2021] Tkohlu__00: class Bird():
    wings = 2       # Class level variable
    @classmethod
    def fly(cls,name):
        print(name,'flies with',cls.wings,'wings')
Bird.fly("Sparrow")
Bird.fly("Pigeon")
[9:48 pm, 10/08/2021] Tkohlu__00: class myClass():
    n = 0
    def _init_(self):
        myClass.n = myClass.n + 1
    @staticmethod
    def noObjects():
        print("This is the",myClass.n,'object')

obj1 = myClass()
obj2 = myClass()
obj3 = myClass()
myClass.noObjects()