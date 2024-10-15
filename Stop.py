
import CategoriesOfTransport
import random


class Stop(Bus):
    def __init__(self,model, speed, pathLength, numberOfStops):
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        super().__init__(model,speed)

    def time(self):

        arrivalTime = (self.pathLength * self.numberOfStops) / self.speed

        ran = random.randint(0,1)
        if ran == 0 :
            arrivalTime += random.randint(0, 5)
        else:
            arrivalTime -= random.randint(0,5)

        print(arrivalTime)



obj = Stop('Nissan', 50, 600, 5)


obj.time()





