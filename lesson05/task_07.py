# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('text_7.txt', "r", encoding='utf-8') as f:
    profit_dict = {}
    n_comp = 0
    total_profit = 0.0
    avg_profit_dict = {}

    for line in f:
        l_profit = 0.0
        l_list = line.replace('\n', '').split(" ")
        try:
            l_profit = float(l_list[2]) - float(l_list[3])
        except:
            continue

        profit_dict[l_list[0]] = l_profit  # '%.2f' %

        if l_profit >= 0:
            n_comp = n_comp + 1
            total_profit = total_profit + l_profit

    avg_profit_dict["average_profit"] = (total_profit / n_comp)  # '%.2f' %

with open('text_7.json', "w", encoding='utf-8') as f:
    f.write(json.dumps([profit_dict, avg_profit_dict], ensure_ascii=False, indent=3))

# print(json.dumps([profit_dict,avg_profit_dict], ensure_ascii=False))

# for el in profit_dict.items():
#     print(el)
#
# print(avg_profit_dict)
