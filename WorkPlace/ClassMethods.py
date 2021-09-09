#class methods

class Animals:
    legs=4
    @classmethod
    def Walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
Animals.Walk("Dog")
Animals.Walk("Cat")
