# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothe(ABC):
    _total = 0

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calc(self):
        pass

    @classmethod
    def addtotal(cls, value):
        cls._total = cls._total + value


#    @property
#   @classmethod
#    def total(cls):
#        return cls.__total

class Coat(Clothe):

    def __init__(self, size):
        self.__name = 'Coat'
        self.__size = size

    @property
    def name(self):
        return self.__name

    @property
    def calc(self):
        Clothe.addtotal(self.__size / 6.5 + 0.5)
        return (self.__size / 6.5 + 0.5)


class Blazer(Clothe):

    def __init__(self, height):
        self.__name = 'Blazer'
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def calc(self):
        Clothe.addtotal(self.__height * 2 + 0.3)
        return (self.__height * 2 + 0.3)


my_coat = Coat(10)
print(my_coat.name, my_coat.calc)

my_blazer = Blazer(10)
print(my_blazer.name, my_blazer.calc)

print("Расход ткани всего:", Clothe._total)
