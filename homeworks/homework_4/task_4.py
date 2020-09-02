"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
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


new_list = [el for el in my_list if my_list.count(el) == 1]


print(new_list)