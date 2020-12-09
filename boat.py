from vehicle import Vehicle


class Boat(Vehicle):
    def __init__(self, gas_tank, engine, wheels):
        super(Boat, self).__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print('Швидкість корабля ' + str(self.speed))
        super(Boat, self).accelerate()

    def turn(self, side):
        print('Човен повернув')
        super(Boat, self).turn(side)

    def brake(self):
        super(Boat, self).brake()
        print('Човен зупинився')
        print('----------')

    def get_wheels_count(self):
        super(Boat, self).get_wheels_count()
