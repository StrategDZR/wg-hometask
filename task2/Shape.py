class Shape:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color):
        print(f"\nDrawing {self.__class__.__name__}: main point = ({self.x}, {self.y}), color is {color}")


class Circle(Shape):
    radius: int

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, color):
        super().draw(color)
        print(f", with radius = {self.radius}")


class Triangle(Shape):
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, x, y, x1, y1, x2, y2):
        super().__init__(x, y)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, color):
        super().draw(color)
        print(f", with second point = ({self.x1}, {self.y1}) and third point = ({self.x2}, {self.y2})")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self, color):
        super().draw(color)
        print(f", with width = {self.width} and height = {self.height}")
