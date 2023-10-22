from abc import ABC, abstractmethod
from typing import List

class Graphic(ABC):
    @abstractmethod
    def move(self): ...

class Shape(Graphic):
    def move(self):
        print("move")

class Group(Graphic):
    def __init__(self) -> None:
        self._children: List[Graphic] = []

    def add (self, child: Graphic) -> None:
        self._children.append(child)

    def remove(self, child: Graphic) -> None:
        self._children.remove(child)

    def move(self):
        for child in self._children:
            child.move()