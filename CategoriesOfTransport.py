from TransportFile import Transport
import random

class Bus(Transport):
    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / (self.speed * 3.6)

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)
        else:
            self.arrivalTime -= random.randint(0,5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)

    def showInfoBus(self):
        print(self.model, self.speed, self.arrivalTime)

class Trolleybus(Transport):

    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self): 

        self.arrivalTime = (self.pathLength * self.numberOfStops) / (self.speed * 3.6)

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)
        else:
            self.arrivalTime -= random.randint(0,5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)

    def showInfoTrolleybus(self):
        print(self.model, self.speed, self.arrivalTime)
class Tram(Transport):

    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / (self.speed * 3.6)

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)
        else:
            self.arrivalTime -= random.randint(0,5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)

    def showInfoTram(self):
        print(self.model, self.speed, self.arrivalTime)



obj = Bus('Nissan', 35, 600, 6)
obj1 = Trolleybus('Ford', 20, 600, 8)
obj2 = Tram('Tram', 40, 600,10)

obj.time()
obj1.time()
obj2.time()

obj.showInfoBus()
obj1.showInfoTrolleybus()
obj2.showInfoTram()

