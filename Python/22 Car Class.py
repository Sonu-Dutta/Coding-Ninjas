from sys import stdin


class Car:
    def __init__(self, noOfGare, color):
        self.noOfGare = noOfGare
        self.color = color

    def printInfo(self):
        print("noOfGear:", self.noOfGare)
        print("color:", self.color)


class RaceCar(Car):
    def __init__(self, noOfGare, color, maxSpeed):
        super().__init__(noOfGare, color)
        self.maxSpeed = maxSpeed

    def printInfo(self):
        super().printInfo()
        print("maxSpeed:", self.maxSpeed)


noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())

raceCar = RaceCar(noOfGear, color, maxSpeed)
raceCar.printInfo()
