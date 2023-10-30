
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
            print(self.current_floor)
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
        for h in range(1, elevator_num+1):
            h = Elevator(self.bottom, self.top)
            self.elevator_list.append(h)

    def run_elevator(self,elevator_index, des_floor):
        self.elevator_list[elevator_index].go_to_floor(des_floor)

    def fire_alarm(self):
        for h in self.elevator_list:
            h.go_to_floor(self.bottom)
            print(h.current_floor)

# Test elevator class
elevator = Elevator(1, 7)
elevator.go_to_floor(5)
elevator.go_to_floor(1)

building1 = Building(1, 8, 3)
building1.run_elevator(1,5)
building1.fire_alarm()

