"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = input("PLEASE, ENTER YOUR NUMBER... ")


tmp1 = n + n

tmp2 = tmp1 + n

answer = int(n) + int(tmp1) + int(tmp2)

print("ANSWER:", n, "+", tmp1, "+", tmp2, "=", answer)


