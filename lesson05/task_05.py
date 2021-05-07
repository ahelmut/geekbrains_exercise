# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint, random

n = randint(0, 100)

with open('task_05_output.txt', "w", encoding='utf-8') as f:
    for i in range(n):
        f.write(str('%.2f' % (random() * 1000)) + ' ')
    f.write(str('%.2f' % (random() * 1000)))

with open('task_05_output.txt', "r", encoding='utf-8') as f:
    l_numblist = f.read().replace('\n', '').split(" ")

total = 0.0
for numb in l_numblist:
    total = total + float(numb)

print("Сумма чисел в файле:" + '%.2f' % total)
