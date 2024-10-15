from TransportFile import Transport
import random

class Bus(Transport):
    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / self.speed

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
        else:
            self.arrivalTime -= random.randint(0,5)

    def showInfoBus(self):
        print(self.model, self.speed, self.arrivalTime)

class Trolleybus(Transport):

    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / self.speed

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
        else:
            self.arrivalTime -= random.randint(0,5)

    def showInfoTrolleybus(self):
        print(self.model, self.speed, self.arrivalTime)
class Tram(Transport):

    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / self.speed

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
        else:
            self.arrivalTime -= random.randint(0,5)

    def showInfoTram(self):
        print(self.model, self.speed, self.arrivalTime)



obj = Bus('Nissan', 60, 600, 6)
obj1 = Trolleybus('Ford', 20, 600, 6)
obj2 = Tram('Tram', 45, 600,6)

obj.time()
obj1.time()
obj2.time()

obj.showInfoBus()
obj1.showInfoTrolleybus()
obj2.showInfoTram()
