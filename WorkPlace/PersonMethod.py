class Person:
    def __init__(self):
        self.name="Aabha"
        self.dob=self.Dob()

    def display(self):
        print("Name",self.name)
        self.dob.display()

    class Dob:
        def __init__(self):
            self.dd=13
            self.mm=9
            self.yy=2005

        def display(self):
            print("DOB = {}/{}/{}",format(self.dd,self.mm,self.yy))
p=Person()
p.display()