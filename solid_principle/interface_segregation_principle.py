import abc

# Violation of ISP
class MultiFunctioPrinterInterface(abc.ABC):
    @abc.abstractmethod
    def scan(self): ...

    @abc.abstractmethod
    def print(self): ...

    @abc.abstractmethod
    def copy(self): ...


# Obey ISP
class PrinterInterface(abc.ABC):
    @abc.abstractmethod
    def print(self): ...

class ScannerInteface(abc.ABC):
    @abc.abstractmethod
    def scan(self): ...

class CopierInteface(abc.ABC):
    @abc.abstractmethod
    def copy(self): ...

class MultiFunctioPrinter(PrinterInterface, ScannerInteface, CopierInteface):
    def print(self): ...

    def copy(self): ...

    def scan(self): ...

