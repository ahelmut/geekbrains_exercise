# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime


class MyDate():
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    @classmethod
    def set_date(cls, text_date):
        return cls(*text_date.split("-"))

    @staticmethod
    def check(ldate):
        try:
            datetime.date(ldate.year, ldate.month, ldate.day)
        except Exception as err:
            return err


date_1 = MyDate.set_date("64-13-2021")

print(f'{date_1.day}' + '.' + f'{date_1.month}' + '.' + f'{date_1.year}')

print(MyDate.check(date_1))

date_1 = MyDate.set_date("64-12-2021")

print(f'{date_1.day}' + '.' + f'{date_1.month}' + '.' + f'{date_1.year}')

print(MyDate.check(date_1))

date_1 = MyDate.set_date("31-12-2021")

print(f'{date_1.day}' + '.' + f'{date_1.month}' + '.' + f'{date_1.year}')

print(MyDate.check(date_1))
