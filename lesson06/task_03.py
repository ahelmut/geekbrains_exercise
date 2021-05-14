# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    __name = str()
    __surname = str()
    __position = str()
    _income = {"wage": 0, "bonus": 0}

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_position(self):
        return self.__position

    def get_wage(self):
        return self._income['wage']

    def get_bonus(self):
        return self._income['bonus']

    def __init__(self, name, surname, position, wage, bonus):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.get_name() + " " + self.get_surname()

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()


my_employee = Position('John', 'Smith', 'Manager', 3.00, 1.00)

print(my_employee.get_full_name())
print(my_employee.get_total_income())
