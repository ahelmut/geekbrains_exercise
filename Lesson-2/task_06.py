# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
productlist = []

myattributes = {"название", "цена", "количество", "единица измерения"}

i = 0

# while i < 3:
#    productlist.append((i, {myattributes[0]: input("Введи " + myattributes[0] + ":"),
#                            myattributes[1]: input("Введи " + myattributes[1] + ":"),
#                            myattributes[2]: input("Введи " + myattributes[2] + ":"),
#                            myattributes[3]: input("Введи " + myattributes[3] + ":")}))
#    print(productlist[i])
#    i += 1

while i < 3:
    myproduct = {}
    for myattr in myattributes: myproduct.update({myattr:input("Введи " + myattr + ":")})
    productlist.append((i,myproduct))
    print(productlist[i])
    i+=1

myanalytics = {}
n = 0
mytemplist = []
for myattr in myattributes:
    mytemplist = []
    for product in productlist:
        mytemplist.append(product[1][myattr])

    myanalytics.update({myattr: mytemplist})

print("Результат:")
for thing in myanalytics:
    print(thing, myanalytics[thing])
