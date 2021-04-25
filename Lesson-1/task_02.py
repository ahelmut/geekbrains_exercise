# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_sec = (input("Введи время в секундах(целое):"))

if not time_sec.isdecimal():
    print("Ошибка!")
    exit(456)

sec = str(int(time_sec) % 60).zfill(2)
min = str((int(time_sec) // 60) % 60).zfill(2)
hour = str((int(time_sec) // 60) // 60)

if len(hour) == 1:
    hour = hour.zfill(2)

print((hour) + ":" + (min) + ":" + (sec))
