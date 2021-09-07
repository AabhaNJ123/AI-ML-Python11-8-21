#inside instance method using self variable

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        
    def m1(self):
        self.c=30

t1=Test()
t1.m1()
t1.d=40
print(t1.__dict__)