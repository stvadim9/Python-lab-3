from driveable import Driveable
class Vehicle(Driveable):

    def __init__(self, gas_tank, engine, wheels):
        self.gas_tank = gas_tank
        self.engine = engine
        self.wheels = wheels.get_count()
        self.speed = 0

    def get_wheels_count(self):
        if self.wheels == 0:
            print("Човен без коліс")
        else:
            print('Кількість коліс ' + str(self.wheels))

    def accelerate(self):
        self.speed = self.speed + self.gas_tank.get()
        print('Прискорення до ' + str(self.speed) + 'км/год')

    def turn(self, side):
        print('Поворот на ' + str(side))

    def brake(self):
        while self.speed != 0:
            self.speed = self.speed - (self.speed / 2)
            if self.speed == 1:
                self.speed = 0
                break
            print('Швидкість: ' + str(self.speed) + 'км/год')
            break
        print('stop')
