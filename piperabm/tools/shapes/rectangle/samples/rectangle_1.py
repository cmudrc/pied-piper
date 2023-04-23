from piperabm.tools.shapes import Rectangle
from piperabm.unit import Unit


rectangle = Rectangle(
    width=10,
    height=10,
    angle=Unit(45, 'degree').to_SI()
)


if __name__ == "__main__":
    print(rectangle)
    