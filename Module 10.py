
class Elevator:
    current_floor = 0

    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.go_up()
            elif self.current_floor > floor:
                self.go_down()
        return self.current_floor

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        self.current_floor -= 1


class Building:
    elevator_list = []

    def __init__(self, bottom, top, elevator_num):
        self.top = top
        self.bottom = bottom
        self.elevator_num = elevator_num
        for h in range(0, elevator_num):
            h = Elevator(self.top, self.bottom)
            self.elevator_list.append(h)

    def run_elevator(self, des_floor):
        for h in self.elevator_list:
            h.go_to_floor(des_floor)

    def fire_alarm(self):
        for h in self.elevator_list:
            h.go_to_floor(self.bottom)


# Test elevator class
elevator = Elevator(1, 7)
elevator.go_to_floor(5)
print(elevator.current_floor)
elevator.go_to_floor(1)
print(elevator.current_floor)

building1 = Building(1, 8, 3)
building1.run_elevator(5)
building1.fire_alarm()
for ele in building1.elevator_list:
    print(ele.current_floor)