class Engine2D:
    def __init__(self):
        self.canvas = []
        self.color = "black"

    def add_shape(self, shape):
        self.canvas.append(shape)

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.color)
        self.canvas = []

    def set_color(self, color):
        self.color = color
