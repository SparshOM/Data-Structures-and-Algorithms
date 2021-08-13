# wap to make a class inside a class (nested class)
class Person:
    def _init_(self):
        self.name = input("Enter your name ")
        # self.dob = self.DOB()
        #self.dob => class 
    def display(self):
        print(self.name)
    
    # inner class
    class DOB:
        def _init_(self):
            self.dd = int(input("Enter day "))
            self.mm = int(input("Enter month "))
            self.yy = int(input("Enter year "))
        def display(self):
            print("Dob = {}/{}/{}".format(self.dd,self.mm,self.yy))
            

x = Person().DOB()
x.display()
print(x.yy)
# x = p.dob
# x.display()