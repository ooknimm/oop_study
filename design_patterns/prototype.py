import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def clone(self) -> "Shape": ...

class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)
    
rectangle = Rectangle(1, 5)

new_rectangle = rectangle.clone()