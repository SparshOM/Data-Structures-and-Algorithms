# WAP to make a class student and take their numbers age and name and then print it with stmt

class Student:
    def _init_(self):
        self.name = input("Enter your name ")
        self.age = input("Enter your age ")
        self.number = input("Enter your number ")
    def display(self):
        print("Hi, my name is",self.name)
        print("My age is",self.age)
        print("My marks are",self.number)

s1 = Student()
s1.display()
# to study "Types of Methods"