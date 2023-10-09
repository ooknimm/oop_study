import enum

class DoughEnum(enum.Enum):
    THIN = 1
    PAN = 2
    SCREEN = 3

class SourceEnum(enum.Enum):
    TOMATO = 1
    CREAM = 2

class CheezeEnum(enum.Enum):
    MOZZARELLA = 1
    CHEDDAR = 2

class ToppingEnum(enum.Enum):
    BEEF = 1
    BELL_PEPPER = 2
    PEPPERONI = 3    

class Pizza:
    def __init__(self) -> None:
        self.size: int
        self.dough: DoughEnum
        self.source: SourceEnum
        self.cheeze: CheezeEnum
        self.topping: ToppingEnum

class PizzaBuilder:
    def __init__(self) -> None:
        self._pizza = Pizza()

    def set_size(self, size: int) -> "PizzaBuilder":
        self._pizza.size = size
        return self

    def set_dough(self, dough) -> "PizzaBuilder":
        self._pizza.dough = dough
        return self
    
    def set_source(self, source) -> "PizzaBuilder":
        self._pizza.source = source
        return self
    
    def set_cheeze(self, cheeze) -> "PizzaBuilder":
        self._pizza.cheeze = cheeze
        return self
    
    def set_topping(self, topping) -> "PizzaBuilder":
        self._pizza.topping = topping
        return self
    
    def build(self) -> Pizza:
        if not hasattr(self._pizza, "size"):
            raise
        if not hasattr(self._pizza, "dough"):
            raise
        if not hasattr(self._pizza, "source"):
            raise
        if not hasattr(self._pizza, "cheeze"):
            raise
        if not hasattr(self._pizza, "topping"):
            raise
        return self._pizza


pb = PizzaBuilder()
pizza = pb.set_size(10).set_dough(DoughEnum.THIN).set_source(SourceEnum.TOMATO).set_cheeze(CheezeEnum.MOZZARELLA).set_topping(ToppingEnum.BEEF)