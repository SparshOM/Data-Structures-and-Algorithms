# WAP to implement Multiple Inheritance
class A(object):        # The base class of the class hierarchy (Base of base class)
    def _init_(self):
        self.a = 'A'
        print(self.a)
        super()._init_()

class B(object):        # The base class of the class hierarchy (Base of base class)
    def _init_(self):
        self.b = 'B'
        print(self.b)
        super()._init_()

class C(B,A):
    def _init_(self):
        self.c = 'C'
        print(self.c)
        super()._init_()
        
obj = C()
class Duck:
    def talk(self):
        print("Quack quack")

class human:
    def talk(self):
        print("Hello hi")

def call_talk(obj):
    obj.talk() 

x = Duck()
call_talk(x)
x = human()
call_talk(x)