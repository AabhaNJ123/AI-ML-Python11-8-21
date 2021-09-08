#static variable

class Test:
    x=10

    def __init__(self):
        self.y=30

t1=Test()
t2=Test()
print("t1 : ",t1.x, t1.y)
print("t2 : ",t2.x, t2.y)
Test.x=888
t1.y=999
print("t1 : ",t1.x, t1.y)
print("t2 : ",t2.x, t2.y)