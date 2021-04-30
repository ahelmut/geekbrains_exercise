# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def find_special_symbol(lstr="", l_symbol="!"):
    lstr = str(lstr)
    return lstr.find(l_symbol)


sum_string = 0
while True:
    mystring = input("Введи несколько чисел, разделенных пробелом:")
    symbol_index = find_special_symbol(lstr=mystring)
    if not symbol_index == -1:
        for thing in mystring[0:symbol_index].split(" "):
            try:
                sum_string = sum_string + float(thing)
            except:
                pass
        #                print("Ошибка! Введены не числа.")
        print(sum_string)
        break
    else:
        for thing in mystring.split(" "):
            try:
                sum_string = sum_string + float(thing)
            except:
                pass
        #                print("Ошибка! Введены не числа.")

        print(sum_string)
