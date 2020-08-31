"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def get_salary(*args):
    """Counts the salary.

    :param hour: float
    :param price: float
    :param bonus: float
    :return:
    """
    print(args[0] * args[1] + args[2])


_, *args = argv

flag = 1

for idx, itm in enumerate(args):
    try:
        args[idx] = float(itm)
    except ValueError as e:
        flag = 0
        print(e)
        break

if flag:
    print("SALARY:")
    get_salary(*args)

