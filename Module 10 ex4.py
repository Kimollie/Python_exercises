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


class Race:
    car_list = []

    def __init__(self, name, distance, car_num):
        self.name = name
        self.distance = distance
        self.car_num = car_num
        for i in range(1, car_num + 1):
            regis_num = "ABC-" + str(i)
            max_speed = random.randint(100, 201)
            car = Car(regis_num, max_speed)
            self.car_list.append(car)

    def hour_pass(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 16))
            car.drive(1)

    def print_status(self):
        print("{:<20} {:<15} {:<15} {:<15}".format("Registration Number", "Maximum speed", "Current speed",
                                                   "Travelled distance"))
        for car in self.car_list:
            print(
                "{:<20} {:<15} {:<15} {:<15}".format(car.regis_num, car.max_speed, car.current_speed,
                                                     car.travelled_dis))

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_dis >= self.distance:
                return True


# Car race
race = Race("Grand Demolition Derby", 8000, 10)
hour = 0

while not race.race_finished():
    race.hour_pass()
    hour += 1
    if (hour % 10) == 0:
        print(f"\n{hour} hours has passed\n")
        race.print_status()

print(f"\nTotal {hour} hours has passed\nResult of {race.name} is:")
race.print_status()
