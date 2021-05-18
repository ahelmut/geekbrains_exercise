# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix():
    rows = []
    __width = int()
    __height = int()

    def __init__(self, *args):
        self.__height = len(list(args))

        if not self.__height == 0:
            self.__width = len(list(args)[0])
        else:
            self.__width = 0

        for el in list(args):
            if not type(el) == type([]): raise ValueError
            if not self.__width == len(el): raise ValueError

        self.rows = list(args)

    def __str__(self):
        return ('\n'.join(['  '.join([str(item) for item in row]) for row in self.rows]))

    def __add__(self, other):
        result = Matrix()
        if not self.width == other.width: raise ValueError
        if not self.height == other.height: raise ValueError

        for i in range(len(self.rows)):
            row = []
            if not len(self.rows[i]) == len(other.rows[i]): raise ValueError
            for j in range(len(self.rows[i])):
                row.append(self.rows[i][j] + other.rows[i][j])
            result.rows.append(row)
        return result

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


matrix1 = Matrix([1, 2, 3])

matrix2 = Matrix([1, 2, 3], [4, 5, 6])

matrix3 = Matrix([1], [2], [3])

matrix4 = matrix1 + matrix1

matrix5 = matrix2 + matrix2

matrix6 = matrix3 + matrix3

matrix7 = Matrix([1, 2, 3, 3], [4, 5, 6, 6])
# matrix8 = matrix7 + matrix2

try:
    matrix9 = matrix1 + matrix3
except ValueError:
    print("Ошибка! Размерность 1-го слагаемого: " + str(matrix1.height) + "x" + str(
        matrix1.width) + '\n' + "Размерность 1-го слагаемого: " + str(matrix3.height) + "x" + str(matrix3.width))

print()
print(matrix1)
print()
print(matrix2)
print()
print(matrix3)
print()
print(matrix4)
print()
print(matrix5)
print()
print(matrix6)
