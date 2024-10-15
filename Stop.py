import CategoriesOfTransport
import Transport
import random

class Stop(Transport):
    def __init__(self, pathLength, numberOfStops):
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops

    def time(self, speed):

        arrivalTime = (self.pathLength * self.numberOfStops) / speed

        ran = random.randint(0,1)
        if ran == 0 :
            arrivalTime += random.randint(0, 5)
        else:
            arrivalTime -= random.randint(0,5)

        return arrivalTime







