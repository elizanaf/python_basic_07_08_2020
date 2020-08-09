"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

num = input("Enter a positive number... ")
num = int(num)
if num <= 0:
    print("ERROR.")
    exit(1)

max_num = 0

while num:
    tmp = num % 10
    if tmp > max_num:
        max_num = tmp
    num //= 10

print("MAX:",max_num)
