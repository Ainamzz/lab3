import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, another):
        return math.sqrt((self.x - another.x) ** 2 + (self.y - another.y) ** 2)

x1, y1 = map(int, input("Input first values:").split())
x2, y2 = map(int, input("Input second values:").split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
p1.show()
p2.show()
print(p1.dist(p2))