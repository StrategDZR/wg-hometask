from task2.Shape import Circle, Triangle, Rectangle


def test_circle():
    circle = Circle(0, 1, 2)
    assert circle.x == 0
    assert circle.y == 1
    assert circle.radius == 2
    assert isinstance(circle, Circle)


def test_circle_big_values():
    circle = Circle(12343243423434234, -2342342342342342355646546546456456, 0)
    assert circle.x == 12343243423434234
    assert circle.y == -2342342342342342355646546546456456
    assert circle.radius == 0


def test_circle_incorrect_values():
    circle = Circle(2.243, "three", True)
    assert circle.x == 2.243
    assert circle.y == "three"
    assert circle.radius


def test_circle_color(capfd):
    circle = Circle(0, 1, 2)
    circle.draw("white")
    out, err = capfd.readouterr()
    assert out == "\nDrawing Circle: main point = (0, 1), color is white\n, with radius = 2\n"


def test_triangle():
    triangle = Triangle(0, 1, 2, 3, 4, 5)
    assert triangle.x == 0
    assert triangle.y == 1
    assert triangle.x1 == 2
    assert triangle.y1 == 3
    assert triangle.x2 == 4
    assert triangle.y2 == 5
    assert isinstance(triangle, Triangle)


def test_triangle_incorrect_values():
    triangle = Triangle(0, '1', "two", False, 4.42, 5)
    assert triangle.x == 0
    assert triangle.y == '1'
    assert triangle.x1 == "two"
    assert not triangle.y1
    assert triangle.x2 == 4.42
    assert triangle.y2 == 5


def test_triangle_color(capfd):
    triangle = Triangle(0, 1, 2, 3, 4, 5)
    triangle.draw("purple")
    out, err = capfd.readouterr()
    assert out == "\nDrawing Triangle: main point = (0, 1), color is purple\n" \
                  ", with second point = (2, 3) and third point = (4, 5)\n"


def test_rectangle():
    rectangle = Rectangle(0, 1, 2, 3)
    assert rectangle.x == 0
    assert rectangle.y == 1
    assert rectangle.width == 2
    assert rectangle.height == 3
    assert isinstance(rectangle, Rectangle)


def test_rectangle_incorrect_values():
    rectangle = Rectangle(0, True, list, "3")
    assert rectangle.x == 0
    assert rectangle.y
    assert rectangle.width == list
    assert rectangle.height == "3"


def test_rectangle_color(capfd):
    rectangle = Rectangle(0, 1, 2, 3)
    rectangle.draw("yellow")
    out, err = capfd.readouterr()
    assert out == "\nDrawing Rectangle: main point = (0, 1), color is yellow\n" \
                  ", with width = 2 and height = 3\n"
