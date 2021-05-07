# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
# фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', "r", encoding='utf-8') as f:
    lw_personal = []
    n = 0
    l_total = 0.00

    for line in f:
        if line.replace('\n', '') == '': continue
        n += 1
        try:
            if float(line.replace('\n', '').split(" ")[1]) < 20000:
                lw_personal.append(line.replace('\n', '').split(" ")[0])

            l_total = l_total + float(line.replace('\n', '').split(" ")[1])
        except:
            print("Ошибка! Строка №" + str(n))
            continue

    print("Сотрудники с ЗП менее 20000:", *lw_personal)

    try:
        avg_wage = l_total / n
    except ZeroDivisionError:
        avg_wage = 0

    print("Средняя ЗП:", '%.2f' % avg_wage)
