# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание.
# Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class OrganicCell():

    @property
    def cellqty(self):
        return self.__cellqty

    def __init__(self, cells):
        try:
            self.__cellqty = int(cells)
        except:
            self.__cellqty = 0
            print("Ошибка! Нечисловое количество ячеек!")

    def __add__(self, other):
        new_cell = OrganicCell(self.cellqty + other.cellqty)
        return new_cell

    def __sub__(self, other):
        if self.cellqty - other.cellqty > 0:
            new_cell = OrganicCell(self.cellqty - other.cellqty)
        else:
            print("Ошибка! Количество ячеек не может быть отрицательным!")
            new_cell = OrganicCell(0)
        return new_cell

    def __mul__(self, other):
        new_cell = OrganicCell(self.cellqty * other.cellqty)
        return new_cell

    def __truediv__(self, other):
        try:
            new_cell = OrganicCell(self.cellqty // other.cellqty)
        except ZeroDivisionError:
            print("Ошибка, деление на 0!")
            new_cell = OrganicCell(0)

        return new_cell

    @staticmethod
    def make_order(l_cell, row_length):
        j = 0
        result_str = str()
        for i in range(l_cell.cellqty):
            result_str = result_str + "*"
            j += 1
            if j == row_length:
                j = 0
                result_str = result_str + '\n'
        return result_str


mycell_1 = OrganicCell(7)
mycell_2 = OrganicCell(7)

mycell_3 = mycell_1 + mycell_2

print(mycell_3.cellqty)

print(OrganicCell.make_order(mycell_3, 5))