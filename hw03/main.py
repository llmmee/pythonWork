class Shape(object):
    @property
    def area(self):
        pass


class Ellipse(Shape):
    def __init__(self,a=0,b=0):
        super().__init__()
        self.a=a
        self.b=b
    @property
    def area(self):
        return self.a*self.b/2

class Square(Shape):
    def __init__(self,a=0):
        super().__init__()
        self.a=a
    @property
    def area(self):
        return self.a*self.a

class Rectangle(Shape):
    def __init__(self,a=0,b=0):
        super().__init__()
        self.a=a
        self.b=b
    @property
    def area(self):
        return self.a*self.b

class Circle(Shape):
    def __init__(self,r=0):
        super().__init__()
        self.r=r
    @property
    def area(self):
        return self.r*self.r*3.14

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
def compute_area(shapes):
    areas=[x.area for x in shapes]
    print(areas)
    return sum(areas)

total_area=compute_area(shapes)
print(total_area)
