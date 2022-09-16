

class Car:
    #__init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def printname(self):
        print(self.year + self.color)

x = Car("66", "Blue ")
x.printname()


