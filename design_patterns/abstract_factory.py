import abc

# Product
class Button: ...

class ButtonA(Button): ...

class ButtonB(Button): ...

class Checkbox: ...

class CheckboxA(Checkbox): ...

class CheckboxB(Checkbox): ...


# Factory
class Theme(abc.ABC):
    @abc.abstractmethod
    def create_button(self) -> Button: 
        return Button()
    
    @abc.abstractmethod
    def create_checkbox(self) -> Checkbox:
        return Checkbox()

class ThemeA(Theme):
    def create_button(self) -> Button:
        return ButtonA()
    
    def create_checkbox(self) -> Checkbox:
        return CheckboxA()
    
class ThemeB(Theme):
    def create_button(self) -> Button:
        return ButtonB()
    
    def create_checkbox(self) -> Checkbox:
        return CheckboxB()