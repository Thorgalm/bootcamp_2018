class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self._traveled_distance = 0

    def drive(self, distance):
        if self._traveled_distance + distance > self.max_range:
            to_travel = self.max_range - self._traveled_distance
            return to_travel
        else:
            self._traveled_distance += distance
            return distance

    def charge(self):
        self._traveled_distance = 0


def test_electricCar_drive_below_max_range():
    car = ElectricCar(100)  # ustawiam max range
    assert car.drive(70) == 70


def test_electricCar2():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30

def test_electricCar3():
    car = ElectricCar(100)  # ustawiam max range
    assert car.drive(130) == 100

def test_electricCar4():
    car = ElectricCar(100)
    assert car.drive(130) == 100
    car.charge()
    assert car.drive(50) == 50
