class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "You are going"
    def stop(self):
        return "You have stopped"

    def turn_left(self):
        return "You have turned left"

    def turn_right(self):
        return "You have turnrf right"

    def show_speed(self):
        return "You current speed is {self.speed}"

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed() > 60:
            return "You are over the speed limit"
        else:
            return "Keep moving"

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed < 40:
            return "Keep moving"
        else:
            return "You are over the speed limit"
class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

Audi = TownCar(50, "black", "Town")
Truck = WorkCar(30, "yellow", "Work")
Porshe = SportCar(90, "red", "Sport")
BMW = PoliceCar(120, "blue", "Police")

print(Audi.turn_left())
print(Audi.show_speed())
print(Truck.show_speed())
print(BMW.is_police())
print(BMW.show_speed())




