"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

def read_list(*flag):
    """ Reads the list.
    :param flag: int
    :return:
    """
    flag = 1
    list = []
    while True:
        tmp = input("Please, enter the member of the list")
        if tmp == '':
            return list
        try:
            tmp = float(tmp)
            list.append(tmp)
        except ValueError as e:
            flag = 0
            print(e)
            return


flag = 1

my_list = read_list(flag)


if(flag == 0):
    exit(1)

new_list = [el for idx, el in enumerate(my_list) if idx != 0 and el > my_list[idx - 1]]

print(new_list)

