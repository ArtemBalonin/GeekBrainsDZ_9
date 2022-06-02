class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
    def go(self):
        print(f"{self.color} {self.name} поехала")
    def stop(self):
        print(f"{self.color} {self.name} остановилась")
    def turn(self, direction):
        self.direction = direction
        print(f"{self.color} {self.name} повернула на {self.direction}")
    def show_speed(self):
        print(f"Скорость: {self.speed}")
class TownCar(Car):
    def __init__ (self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 60 else print("Превышена допустимая скорость")
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 40 else print("Превышена допустимая скорость")
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

c, t, s, w, p = Car(40, "Красная", "KIA"), TownCar(65, "Белая", "PRIORA"), SportCar(40, "Черный", "Porshe"), \
    WorkCar(40, "Желтая", "Pego"), PoliceCar(40, "Серебристая", "Vesta")

t.go(), t.turn("право"), t.stop()
t.show_speed()
print(f"Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n")

s.go(), s.turn("право"), s.stop()
s.show_speed()
print(f"Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n")

p.go(), p.turn("право"), p.stop()
p.show_speed()
print(f"Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n")