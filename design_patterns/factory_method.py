import abc

# Product
class Vehicle(abc.ABC):
    @abc.abstractmethod
    def run(self): ...

class Motorcyle(Vehicle):
    def run(self): ...

class Bicycle(Vehicle):
    def run(self): ...


# Creator
class AbstractDeliveryService(abc.ABC):
    ...
    def deliver(self): 
        ...
        vehicle = self.create_vehicle()
        vehicle.run()
        ...

    @abc.abstractmethod
    def create_vehicle(self) -> Vehicle:
        return Vehicle()

class MotorcyleDeliveryService(AbstractDeliveryService):
    def create_vehicle(self) -> Vehicle:
        return Motorcyle()

class BicycleDeliveryService(AbstractDeliveryService):
    def create_vehicle(self) -> Vehicle:
        return Bicycle()