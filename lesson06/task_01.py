# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.


from time import sleep


class TrafficLight():
    __mycolor = str()

    def running(self):
        self.__switchred()
        self.__switchyellow()
        self.__switchgreen()

    def __switchgreen(self):
        self.__mycolor = 'green'
        print(self.__mycolor)
        sleep(1)

    def __switchyellow(self):
        self.__mycolor = 'yellow'
        print(self.__mycolor)
        sleep(2)

    def __switchred(self):
        self.__mycolor = 'red'
        print(self.__mycolor)
        sleep(7)

    def __init__(self):
        self.__mycolor = ''


mytrafficlight = TrafficLight()

mytrafficlight.running()
