# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


revenue = input("Введите выручку:")
if not is_float(revenue):
    print("Ошибка!")
    exit(456)

revenue = float(revenue)

expence = float(input("Введите издержки:"))
if not is_float(expence):
    print("Ошибка!")
    exit(457)

expence = float(expence)

margin = revenue - expence

if margin >= 0:
    print("Прибыль =", '%.2f' % round(margin, 2))
    print("Рентабельность = ", '%.2f' % round(margin * 100 / revenue, 2) + " %")
    personal = int(input("Введите численность сотрудников:"))
    print("Прибыль на одного сотрудника =", '%.2f' % round(margin / personal, 2))
else:
    print("Убыток =", round(margin, 2))
