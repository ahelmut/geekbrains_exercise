# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class MyValueError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class MyComplex():

    @classmethod
    def make_complex(cls, txt):
        l_real_part = ''
        l_imaginery_part = ''
        l_sign = 1
        l_txt = txt

        if txt[0] == '-':
            l_sign = (-1)
            l_txt = txt[1:]

        while True:

            try:
                l_real_part = l_sign * float(txt)
                l_imaginery_part = float(0)
                break
            except:
                pass

            if not l_txt[-1] == 'j': raise MyValueError(txt + " не является комплексным числом.")

            try:
                l_real_part = float(0)
                l_imaginery_part = l_sign * float(l_txt[:-1])
                break
            except:
                pass

            try:
                l_real_part = l_sign * float(l_txt.split('+')[0])
                l_imaginery_part = float(l_txt.split('+')[1][:-1])
                break
            except:
                pass

            try:
                l_real_part = l_sign * float(l_txt.split('-')[0])
                l_imaginery_part = (-1) * float(l_txt.split('-')[1][:-1])
                break
            except:
                pass

        if l_real_part == '' or l_imaginery_part == '': raise MyValueError(txt + " не является комплексным числом.")

        result = cls(l_real_part, l_imaginery_part)
        return result

    def __init__(self, a, b):
        self.real_part = float(a)
        self.imaginery_part = float(b)

    def __str__(self):
        l_plus_string = "+"
        if self.imaginery_part < 0: l_plus_string = "-"
        return str(self.real_part) + l_plus_string + str(abs(self.imaginery_part)) + "j"

    def __add__(self, other):
        result = MyComplex(self.real_part + other.real_part, self.imaginery_part + other.imaginery_part)
        return result

    def __mul__(self, other):
        result = MyComplex(self.real_part * other.real_part - self.imaginery_part * other.imaginery_part,
                           self.real_part * other.imaginery_part + self.imaginery_part * other.real_part)
        return result


mycomp_1 = MyComplex(3, -3)
print(mycomp_1)

mycomp_2 = MyComplex.make_complex("-3+2j")
print(mycomp_2)

mycomp_4 = mycomp_1 + mycomp_2
print(mycomp_4)

mycomp_3 = mycomp_1 * mycomp_2
print(mycomp_3)
