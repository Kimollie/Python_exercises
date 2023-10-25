import random
class Car:
    regis_num = None
    max_speed = 0
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


# Test function
test_car = Car("ABC-123",142)
print(f"Registration number: {test_car.regis_num} Maximum speed: {test_car.max_speed}km/h")

test_car.accelerate(30)
test_car.accelerate(70)
test_car.accelerate(50)
print(f"Current speed of the car: {test_car.current_speed}")

test_car.accelerate(-200)
print(f"Final speed: {test_car.current_speed}")

# Car race
cars = []
fastest = 0
for i in range(1,11):
    regis_num = "ABC-" + str(i)
    max_speed = random.randint(100,201)
    car = Car(regis_num, max_speed)
    cars.append(car)

while fastest < 10000:
    for car in cars:
        if car.travelled_dis > fastest:
            fastest = car.travelled_dis
        car.accelerate(random.randint(-10,16))
        car.drive(1)


print("{:<20} {:<15} {:<15} {:<15}".format("Registration Number", "Maximum speed", "Current speed", "Travelled distance"))
for car in cars:
    print(
        "{:<20} {:<15} {:<15} {:<15}".format(car.regis_num, car.max_speed, car.current_speed, car.travelled_dis))



