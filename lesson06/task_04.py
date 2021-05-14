# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car():
    __speed = float()
    __color = str()
    __name = str()
    __is_police = False
    __direction = 1
    __directions = {1: "North", 2: "East", 3: "South", 4: "West"}

    def speed(self):
        return self.__speed

    def set_is_police(self, is_police=True):
        self.__is_police = is_police

    def show_speed(self):
        print("Скорость: " + '%.2f' % self.__speed + " км/ч")

    def show_direction(self):
        print("Направляюсь на " + self.__directions[self.__direction] + ".")

    def show_details(self):
        print("Name: " + self.__name + '\n' + "Color: " + self.__color + '\n' + "Is_police: " + str(self.__is_police))

    def go(self, speed):
        print("Еду!")
        self.__speed = speed
        self.show_speed()
        self.show_direction()

    def stop(self):
        self.__speed = 0
        print("Остановился!")
        self.show_speed()

    def turn(self, direction):
        if direction == 'left':
            self.__direction -= 1
            if self.__direction < 1: self.__direction = self.__direction + 4
            print("Повернул налево!")
            self.show_direction()
        elif direction == 'right':
            self.__direction += 1
            if self.__direction > 4: self.__direction = self.__direction - 4
            print("Повернул направо!")
            self.show_direction()
        else:
            print("Неизвестное направление, продолжаю прямолинейное движение!")
            self.show_direction()

    def __init__(self, color, name):
        try:
            self.__color = str(color)
            self.__name = str(name)
        except:
            print("Error!")


# TownCar, SportCar, WorkCar, PoliceCar

class TownCar(Car):
    def show_speed(self):
        l_speed = self.speed()
        print("Скорость: " + '%.2f' % l_speed + " км/ч")
        if l_speed > 60.0: print("Превышение скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        l_speed = self.speed()
        print("Скорость: " + '%.2f' % l_speed + " км/ч")
        if l_speed > 40.0: print("Превышение скорости!")


class PoliceCar(Car):
    def __init__(self, color, name):
        try:
            self.__color = str(color)
            self.__name = str(name)
        except:
            print("Error!")
        self.set_is_police(True)


car_1 = TownCar("red", "TownCar №1")
car_1.show_details()
car_1.go(70)
car_1.turn("left")
car_1.turn("right")
car_1.turn("right")
car_1.show_speed()
car_1.stop()

print('\n')

car_2 = WorkCar("green", "WorkCar №1")
car_2.show_details()
car_2.go(70)
car_2.turn("left")
car_2.turn("right")
car_2.turn("right")
car_2.show_speed()

print('\n')

car_3 = SportCar("green", "SportCar №1")
car_3.show_details()
car_3.go(70)
car_3.turn("left")
car_3.turn("right")
car_3.turn("right")
car_3.show_speed()

print('\n')

car_4 = PoliceCar("Police", "PoliceCar №1")
car_4.show_details()
car_4.go(70)
car_4.turn("left")
car_4.turn("right")
car_4.turn("right")
car_4.show_speed()
