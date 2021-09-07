class Student:

    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("Student Name : {}\nRoll no : {}\nMarks : {}\n".format(self.name,self.rollno,self.marks))

s1=Student("Aabha",41,94)
s1.display()
s2=Student("Aarya",34,87)
s2.display()