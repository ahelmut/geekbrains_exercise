# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

numb = input("Введите целое положительное число N:")

if not numb.isdecimal():
    print("Ошибка!")
    exit(456)

result = int(numb) + int(2*numb) + int(3*numb)

print("N + NN + NNN =", result)