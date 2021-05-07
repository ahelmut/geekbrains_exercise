# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary = {}
with open('dictionary.txt', "r", encoding='utf-8') as fdictionary:
    for line in fdictionary:
        dictionary[line.replace('\n', '').split(":")[0]] = line.replace('\n', '').split(":")[1]

input_file = open('text_4.txt', "r", encoding='utf-8')
output_file = open('task_04_output.txt', "w", encoding='utf-8')

while True:
    line = input_file.readline()
    if line == '': break
    translated_line = ""
    i = 0

    for word in line.replace('\n', ' \n').split(" "):
        i += 1
        try:
            if word.istitle():
                translated_word = dictionary[word.lower()].title()
            else:
                translated_word = dictionary[word.lower()]
        except KeyError:
            translated_word = word

        translated_line = translated_line + translated_word

        if i < len(line.replace('\n', '').split(" ")): translated_line = translated_line + " "

    output_file.write(translated_line)

input_file.close()
output_file.close()
