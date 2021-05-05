# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count, cycle


def mygen(x=int(0)):
    a = 1
    if x < 0: yield 0

    for x1 in range(1, (x + 1)):
        a = a * x1
        yield a


result = 1

mygenerator = mygen(int(input("Введи целое натуральное число: ")))

for el in mygenerator:
    print(el)