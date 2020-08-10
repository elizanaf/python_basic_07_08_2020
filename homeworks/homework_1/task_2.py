"""2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
hours = 0
minutes = 0
seconds = 0

time_in_sec = input("Enter time in seconds... ")

if int(time_in_sec) < 0:
    print("Invalid time.")
    exit(1)

time_in_sec = int(time_in_sec)

if time_in_sec < 3600:
    hours = 0
else:
    hours = time_in_sec // 3600
    time_in_sec = time_in_sec - hours * 3600



if time_in_sec < 60:
    minutes = 0
else:
    minutes = time_in_sec // 60
    seconds = time_in_sec - minutes * 60


print('Time in format hh:mm:ss: {0:02}:{1:02}:{2:02}' .format(hours,minutes,seconds))

