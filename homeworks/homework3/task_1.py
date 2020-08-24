"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def division_f ():
    """Divides a number.

    :return: float
    """
    a = input ("Enter the first number...")
    if a.isalpha():
        print("Error...")
        exit(1)
    b = input("Enter the second number...")
    if b.isalpha() or float(b) == 0:
        print("Error...")
        exit(1)

    return float(a) / float(b)


print("ANSWER:\n", division_f())