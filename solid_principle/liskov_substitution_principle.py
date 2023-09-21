from abc import ABC, abstractmethod

class WebException(Exception): ...

class ServerException(WebException): ...

#########################################

class Product:
    def __init__(self):
        self.count_of_bug = 0

class WebProduct(Product): ...

class ServerProduct(Product): ...

#########################################

class Programmer(ABC):
    def __init__(self, payment):
        self._payment = payment

    @abstractmethod
    def work(self): ...

class Backend(Programmer): 
    def work(self):
        print("backend work")
    
    def create_server_app(self) -> ServerProduct:
        print("create server app")
        return ServerProduct()

class Frontend(Programmer): 
    def work(self):
        print("frontend work")

    def create_html(self) -> WebProduct:
        print("create html")
        return WebProduct()

class Fullstack(Backend, Frontend): 
    def work(self):
        print("fullstack work")

    def create_web_service(self) -> Product:
        print("create web service")
        self.create_html()
        self.create_server_app()
        return Product()
    
#########################################

class WebProgramming:
    def do_project(self, worker: Fullstack) -> Product:
        # Preconditions
        if worker.payment > 100:
            raise WebException()

        try:
            worker.work()
        except Exception:
            raise WebException()

        product = worker.create_web_service()

        # Postconditions
        if product.count_of_bug > 5:
            raise WebException()
        return product

class ServerProgramming(WebProgramming):
    def do_project(self, worker: Backend) -> ServerProduct:
        ##### Preconditions cannot be strengthened in the subtype 
        # if worker.payment > 80:
        #   return None
        #####
        if worker.payment > 150: # it works.
            raise ServerException()
        
        try:
            worker.work()
        except Exception:
            raise ServerException()
        product = worker.create_server_app()

        ##### Postconditions cannot be weakened in the subtype 
        # if product.count_of_bug > 10:
        #     raise ServerException()
        #####
        if product.count_of_bug > 1:
            raise ServerException()
        return product

#########################################

frontend = Frontend(payment=100)
backend = Backend(payment=100)
fullstack = Fullstack(payment=100)
server = WebProgramming()
try:
    product: Product = server.do_project(fullstack) # it works.
except WebException:
    print("WebException")

server = ServerProgramming() # it can substitues to sub class.
try:
    product: Product = server.do_project(fullstack) # it works too.
except WebException:
    print("WebException")


################################
# Invariant cannot be weakened in the subtype.

class Animal:
    def __init__(self, age: int):
        self._age = age
    
    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0
        else:
            self._age = value

class Human(Animal):
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        ##### Invariant cannot be weakened in the subtype
        # self._age = value
        #####
        if value < 0:
            self._age = 0
        else:
            self._age = value