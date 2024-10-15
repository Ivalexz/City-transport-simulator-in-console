import Transport

class Bus(Transport):
    def __init__(self, model, speed):
        super().__init__(model, speed)

    def showInfo(self):
        print(self.model, self.speed)

class Trolleybus(Transport):
    def __init__(self, model, speed):
        super().__init__(model, speed)

    def showInfor(self):
        print(self.model, self.speed)

class Tram(Transport):
    def __init__(self, model, speed):
        super().__init__(model, speed)

    def showInfo(self):
        print(self.model, self.speed)
