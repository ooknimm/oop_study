# Violation of SRP
class Video:
    def __init__(self, running_time):
        self.running_time = running_time
        self.format = format

    def play(self): ...
    
    def move(self): ...



# Obey SRP
class Video:
    def __init__(self, running_time, format):
        self.running_time = running_time
        self.format = format

class Player:
    def __init__(self, video):
        self.video = video
        
    def play(self): ...
    
    def move(self): ...