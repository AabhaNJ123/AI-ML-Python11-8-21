class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setmarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input("Enter number of students : "))

for i in range(n):
    s=Student()
    name=input("Enter Name : ")
    s.setName(name)
    marks=int(input("Enter marks : "))
    s.setmarks(marks)
    print("hi ",s.getName())
    print("Your marks ",s.getMarks())