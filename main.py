from boat import Boat
from car import Car
from engine import Engine
from gas_tank import GasTank
from solar_car import SolarCar
from wheels import Wheels


def test_drive(driveable):
    driveable.get_wheels_count()
    driveable.turn('Ліво')
    driveable.accelerate()
    driveable.turn('Ліво')
    driveable.brake()


if __name__ == '__main__':
    car = Car(GasTank(23), Engine(35), Wheels(4))
    solarCar = SolarCar(GasTank(12), Engine(25), Wheels(4))
    boat = Boat(GasTank(50), Engine(36), Wheels(0))

    vehicles = [boat, car, solarCar]

    for i in vehicles:
        test_drive(i)
