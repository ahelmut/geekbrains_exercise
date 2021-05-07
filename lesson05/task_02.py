# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_02_data.txt', "r", encoding='utf-8') as f:
    n = 0
    l_words = 0
    for line in f:
        n += 1
        if line.replace('\n', '') == '':
            l_words = 0
        else:
            l_words = len(line.replace('\n', '').split(" "))

        print("Строка #" + str(n) + ". Количество слов: " + str(l_words))
        l_words = 0

    print('Всего строк:' + str(n))
