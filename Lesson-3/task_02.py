# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
# Антон Гельмут 1985 Москва anton.helmut@gmail.com 89629611312

def my_division(**strings):
    mystring = ""
    i = 0
    for attribute, text in strings.items():
        i += 1
        if i == len(strings.items()):
            mystring = mystring + f"{attribute}: {text}"
        else:
            mystring = mystring + f"{attribute}: {text}" + ", "

    print(mystring)


while True:
    mylist = input("Введи через пробел имя, фамилия, год рождения, город проживания, email, телефон:").split(" ")
    try:
        my_division(name=mylist[0], lastname=mylist[1], year=mylist[2], city=mylist[3], email=mylist[4],
                    phone=mylist[5])
        break
    except IndexError:
        print("Ошибка! Недостаточно аргументов.")
