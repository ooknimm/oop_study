class CPU: 
    def execute(self): ...

class Memory: 
    def load(self, address, data): ...

class HardDrive: 
    def read(self, sector, size): ...

class Computer:
    """Facade"""
    BOOT_ADDRESS = ...
    BOOT_SECTOR = ...
    SECTOR_SIZE = ...
    def run(self):
        cpu = CPU()
        memory = Memory()
        hardDrive = HardDrive()
        memory.load(self.BOOT_ADDRESS, hardDrive.read(self.BOOT_SECTOR, self.SECTOR_SIZE))
        cpu.execute()


Computer.run()