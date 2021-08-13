# from teachers import Teacher

# t = Teacher()
# t.setId(10)
# t.setname('Tkohli')
# t.setsalary(10000)

# print("ID =",t.getId())
# print("name =",t.getname())
# print("salary =",t.getsalary())# making a class Teacher and the making multiple objects
class Teacher:
    def setId(self,id):
        self.id = id
    def getId(self):
        return self.id
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setsalary(self,salary):
        self.salary = salary
    def getsalary(self):
        return self.salary
from teachers import Teacher
class Students(Teacher):
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks # from teachers import Teacher

# t = Teacher()
# t.setId(10)
# t.setname('Tkohli')
# t.setsalary(10000)

# print("ID =",t.getId())
# print("name =",t.getname())
# print("salary =",t.getsalary())

from student import Students

t = Students()
t.setId(10)
t.setname('Tkohli')
t.setmarks(80)

print("ID =",t.getId())
print("name =",t.getname())
print("marks =",t.getmarks())
from student import Students

t = Students()
t.setId(10)
t.setname('Tkohli')
t.setmarks(80)

print("ID =",t.getId())
print("name =",t.getname())
print("marks =",t.getmarks())