#static methods

class Maths:

    @staticmethod
    def add(x,y):
        print("The sum     : ",x+y)

    @staticmethod
    def product(x,y):
        print("The product : ",x*y)

    @staticmethod
    def avg(x,y):
        print("The average : ",(x+y)/2)

Maths.add(10,20)
Maths.product(10,20)
Maths.avg(10,20)