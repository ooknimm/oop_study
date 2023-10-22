from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render(self): ...

class RasterRenderer(Renderer):
    def render(self):
        print("raster")

class VectorRenderer(Renderer):
    def render(self):
        print("vector")

class Shape(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self._renderer = renderer

    def render(self):
        return self._renderer.render()
    
class Circle(Shape): ...
    

renderer = VectorRenderer()
circle = Circle(renderer=renderer)
circle.render()