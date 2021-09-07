#inside constructor using self variable

class Employee:
    def __init__(self):
        self.eno=100
        self.ename="Aabha"
        self.esalary=50000

e=Employee()
print(e.__dict__)