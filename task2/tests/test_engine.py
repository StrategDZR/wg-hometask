from task2.Engine2D import Engine2D
from task2.Shape import Circle, Triangle, Rectangle


def test_engine_default_canvas():
    engine = Engine2D()
    assert len(engine.canvas) == 0, f'canvas is not empty, actual length is {len(engine.canvas)}'


def test_engine_default_color():
    engine = Engine2D()
    assert engine.color == 'black', f'default color should be black, actual color is {engine.color}'


def test_add_shape_check_length_one_object():
    engine = Engine2D()
    circle = Circle(5, 6, 12)
    engine.add_shape(circle)
    assert len(engine.canvas) == 1, f'canvas should contain 1 shape, actual size is {len(engine.canvas)}'


def test_add_shape_check_one_object_type():
    engine = Engine2D()
    circle = Circle(5, 6, 12)
    engine.add_shape(circle)
    shape = engine.canvas.pop()
    assert isinstance(shape, Circle), f'canvas should contain Circle, actual type is {shape}'


def test_add_shape_check_length_few_shapes():
    engine = Engine2D()
    circle = Circle(0, 0, 2)
    triangle = Triangle(0, 0, 2, 2, 0, 2)
    rectangle = Rectangle(5, 12, 8, 12)
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)
    assert len(engine.canvas) == 3, f'canvas should contain 3 shapes, actual size is {len(engine.canvas)}'


def test_add_shape_check_obj_types_few_shapes():
    engine = Engine2D()
    circle = Circle(0, 0, 2)
    triangle = Triangle(0, 0, 2, 2, 0, 2)
    rectangle = Rectangle(5, 12, 8, 12)
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)
    assert isinstance(engine.canvas.__getitem__(0), Circle), f'canvas should contain Circle, ' \
                                                             f'actual type is {engine.canvas.__getitem__(0)}'
    assert isinstance(engine.canvas.__getitem__(1), Triangle), f'canvas should contain Triangle, ' \
                                                               f'actual type is {engine.canvas.__getitem__(1)}'
    assert isinstance(engine.canvas.__getitem__(2), Rectangle), f'canvas should contain Rectangle, ' \
                                                                f'actual type is {engine.canvas.__getitem__(2)}'


def test_draw(capfd):
    engine = Engine2D()
    circle = Circle(0, 0, 2)
    engine.add_shape(circle)
    engine.draw()
    out, err = capfd.readouterr()
    assert out == "\nDrawing Circle: main point = (0, 0), color is black\n, with radius = 2\n"


def test_draw_few_shapes(capfd):
    engine = Engine2D()
    circle = Circle(0, 0, 2)
    rectangle = Rectangle(1, 5, 1, 1)
    engine.add_shape(circle)
    engine.add_shape(rectangle)
    engine.draw()
    out, err = capfd.readouterr()
    assert out == "\nDrawing Circle: main point = (0, 0), color is black\n, with radius = 2\n" \
                  "\nDrawing Rectangle: main point = (1, 5), color is black\n, with width = 1 and height = 1\n"


def test_draw_clearing_canvas():
    engine = Engine2D()
    circle = Circle(0, 0, 2)
    engine.add_shape(circle)
    engine.draw()
    assert len(engine.canvas) == 0


def test_draw_few_shapes_with_different_colors(capfd):
    engine = Engine2D()
    circle = Circle(0, 0, 2)
    engine.add_shape(circle)
    engine.draw()
    engine.set_color("orange")
    rectangle = Rectangle(1, 5, 1, 1)
    engine.add_shape(rectangle)
    engine.draw()
    out, err = capfd.readouterr()
    assert out == "\nDrawing Circle: main point = (0, 0), color is black\n, with radius = 2\n" \
                  "\nDrawing Rectangle: main point = (1, 5), color is orange\n, with width = 1 and height = 1\n"
