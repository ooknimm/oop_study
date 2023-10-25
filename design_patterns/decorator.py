from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def add(self): ...

class BeseDecorator(Beverage):
    def __init__(self, wrappee: Beverage) -> None:
        self._wrappee = wrappee
    
    def add(self):
        self._wrappee.add()
    
class WhippingCreamDecorator(BeseDecorator):
    def add(self):
        super().add()
        print("add whippingcream")

class JavaChipDecorator(BeseDecorator):
    def add(self):
        super().add()
        print("add javachip")

class Coffee(Beverage):
    def add(self):
        print("add coffee")

c = Coffee()
c = WhippingCreamDecorator(c)
c = JavaChipDecorator(c)
c.add()

