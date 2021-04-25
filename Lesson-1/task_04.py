# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numb = input("Введите целое положительное число N:")

if not numb.isdecimal():
    print("Ошибка!")
    exit(456)

digit = 0
i = 0

while i < len(numb):
    if int(numb[i]) > digit: digit = int(numb[i])
    if digit == 9: break
    i += 1

print("Самая большая цифра =", digit)
