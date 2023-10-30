import random


class Car:
    current_speed = 0
    travelled_dis = 0

    def __init__(self, regis_num, max_speed):
        self.regis_num = regis_num
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed >= self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed <= 0:
            self.current_speed = 0
        return self.current_speed

    def drive(self, hours):
        self.travelled_dis += (self.current_speed * hours)


class ElectricCar(Car):
    def __init__(self, regis_num, max_speed, battery):
        super().__init__(regis_num, max_speed)
        self.battery = battery


class GasolineCar(Car):
    def __init__(self, regis_num, max_speed, tank):
        super().__init__(regis_num, max_speed)
        self.tank = tank


car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.2)
car1.accelerate(100)
car2.accelerate(120)
car1.drive(3)
car2.drive(3)
print(f"After 3 hours, electric car drove {car1.travelled_dis} km")
print(f"After 3 hours, gasoline car drove {car2.travelled_dis} km")