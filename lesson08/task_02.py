# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class MyValueError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class MyRealNumber():
    def __init__(self, value):
        try:
            self.value = float(value)
        except:
            raise MyValueError(f'{value}' + ' не является вещественным числом.')

    def __truediv__(self, other):
        if other.value == 0:
            c = MyRealNumber('inf')
            raise MyZeroDivisionError("Деление на ноль.")
        else:
            c = MyRealNumber(self.value / other.value)

        return c

    def __str__(self):
        return str(self.value)


while True:

    try:
        l_numerator = input("Введи числитель:")
        l_denominator = input("Введи знаменатель:")
        if l_numerator == '' or l_denominator == '': break

        l_numerator = MyRealNumber(l_numerator)
        l_denominator = MyRealNumber(l_denominator)

        l_div = l_numerator / l_denominator
        print(f'{l_numerator}' + " / " + f'{l_denominator}' + " = " + f'{l_div}')
    except (MyValueError, MyZeroDivisionError) as err:
        print(err)
