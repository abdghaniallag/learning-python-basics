#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicel():
    def __init__(self, body_style):
        self.mode = "parking"
        self.speed = 0
        self.body_style = body_style

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicel):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine_type = engine_type

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "car  at ", self.speed)


class MotorCycle(Vehicel):
    def __init__(self, engine_type, has_side_car):
        super().__init__("MotorCycle")
        if has_side_car:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine_type = engine_type

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "motorcycle  at ", self.speed)


car_1 = Car("gas")
car_2 = Car("electric")

moto_1 = MotorCycle("gas", True)
print(moto_1.wheels)
print(car_1.engine_type)
print(car_2.doors)

car_1.drive(50)
car_2.drive(80)
moto_1.drive(150)
