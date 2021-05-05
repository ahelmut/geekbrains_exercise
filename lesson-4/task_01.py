# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# python C:\Users\anton\OneDrive\Documents\Geekbrains\Python\lesson04\task_01.py


from sys import argv

l_path, l_hour, l_rate, l_bonus = argv

# l_hour, l_rate, l_bonus = 1,2,"b"

try:
    l_hour, l_rate, l_bonus = float(l_hour), float(l_rate), float(l_bonus)
except:
    print("Ошибка! Нечисловой параметр!")
    exit(1)

print("ЗП сотрудника = " + "{0:.2f}".format(l_rate * l_hour + l_bonus))
