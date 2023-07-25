class InvalidSideLengthError(Exception):
    def __init__(self, side_name, side_length):
        self.side_name = side_name
        self.side_length = side_length

    def __str__(self):
        return f"Invalid {self.side_name} length: {self.side_length}. Side length should be greater than 0."


class Rectangle:
    def __init__(self, width, height):
        if width <= 0:
            raise InvalidSideLengthError("width", width)
        if height <= 0:
            raise InvalidSideLengthError("height", height)

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


try:
    rectangle1 = Rectangle(4, 5)
    print("Rectangle 1 area:", rectangle1.area())

    rectangle2 = Rectangle(-2, 3)
    print("Rectangle 2 area:", rectangle2.area())  # Этот код не выполнится из-за исключения

except InvalidSideLengthError as e:
    print("Error:", e)
