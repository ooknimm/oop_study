import abc

# Violation of OCP
class Animal: ...

class Person(Animal): ...

class Cat(Animal): ...

class Dog(Animal): ...

class Printer:
    def hello(self, animal: Animal):
        if isinstance(animal, Person):
            print("안녕")
        elif isinstance(animal, Cat):
            print("미야옹")
        elif isinstance(animal, Dog):
            print("멍멍")


# Obey OCP
class Animal(abc.ABC):
    @abc.abstractmethod
    def hello(self): ...

class Person(Animal):
    def hello(self):
        return "안녕"

class Cat(Animal):
    def hello(self):
        return "미야옹"
        
class Dog(Animal):
    def hello(self):
        return "멍멍"
        
class Printer:
    def hello(self, animal: Animal):
        print(animal.hello())