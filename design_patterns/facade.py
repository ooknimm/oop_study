class CPU: 
    def execute(self): ...

class Memory: 
    def load(self, address, data): ...

class HardDrive: 
    def read(self, sector, size): ...

class Computer:
    """Facade"""
    BOOT_ADDRESS = 1020301
    BOOT_SECTOR = 12938
    SECTOR_SIZE = 1024
    def run(self):
        cpu = CPU()
        memory = Memory()
        hardDrive = HardDrive()
        memory.load(self.BOOT_ADDRESS, hardDrive.read(self.BOOT_SECTOR, self.SECTOR_SIZE))
        cpu.execute()


Computer.run()