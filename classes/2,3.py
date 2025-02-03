class Shape():
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

length = int(input("lendth: "))
sqr = Square(length)
print(sqr.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  
length = int(input("length: "))
width = int(input("width: "))
rect = Rectangle(length, width)
print(rect.area())          