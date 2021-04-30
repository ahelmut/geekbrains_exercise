# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def summax(a=float(0), b=float(0), c=float(0)):
    try:
        llist = [float(a), float(b), float(c)]
    except ValueError:
        print("Ошибка!")

    llist.sort(reverse=True)
    return float(llist[0]) + float(llist[1])


myargs = input("Введи a, b и с(через пробел):").split(" ")
print("SUM MAX =", summax(*myargs))
