# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_division(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        print("Ошибка! Знаменатель равен 0.")
        exit(1)
    except:
        print("Ошибка!")
        exit(2)


while True:
    try:
        mynumerator = float(input("Введи числитель:"))
        break
    except ValueError:
        print("Ошибка!")

while True:
    try:
        mydenominator = float(input("Введи знаменатель:"))
        break
    except ValueError:
        print("Ошибка!")

print('%.2f' % mynumerator + " / " + '%.2f' % mydenominator + " = " + '%.2f' % round(
    my_division(mynumerator, mydenominator), 2))
