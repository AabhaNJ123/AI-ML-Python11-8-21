class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def talk(self):
        print("Hello I am ",self.name)
        print("My marks ",self.marks)

s1=Student("Aabha",16)
s2=Student("Aarya",13)
s2.talk()
