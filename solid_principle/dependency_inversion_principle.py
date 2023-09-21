import abc


# Violation of DIP
class NomalTire: ...

class Car:
    def __init__(self) -> None:
        self.tire: NomalTire


# Obey DIP
class Tire(abc.ABC): ...

class NomalTire(Tire): ...

class SnowTire(Tire): ...

class Car:
    def __init__(self) -> None:
        self.tire: Tire