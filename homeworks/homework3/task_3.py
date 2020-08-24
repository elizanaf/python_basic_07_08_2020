"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func (arg_1 : float, arg_2 : float, arg_3 : float):
    """Counts the greatest sum of the elements.

    :param arg_1: float
    :param arg_2: float
    :param arg_3: float
    :return: float
    """
    sum = arg_1 + arg_2
    if sum < arg_1 + arg_3:
        sum = arg_1 + arg_3
    if sum < arg_2 + arg_3:
        sum = arg_2 + arg_3

    return sum


a = input("Please, enter a number...")
b = input("Please, enter a number...")
c = input("Please, enter a number...")

print("Sum = ", my_func(float(a), float(b), float(c)))
