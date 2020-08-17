"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5,
 3, 3, 2]."""


def isint(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def binarySearch(list, number, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    if list[mid] == int(number):
        return mid
    elif list[mid] < int(number):
        return binarySearch(list, number, start, mid - 1)
    elif list[mid] > int(number):
        return binarySearch(list, number, mid + 1, end)



my_list = [9, 9, 8, 7, 5, 5, 5, 3, 2, 2, 1]


while True:
    number = input("Please, enter a natural number")


    if number == '':
        print("EOF")
        break

    if(number.isalpha()):
        print("Not a number, try again...")
        continue


    if not(isint(number)):
        print("Not a natural number, please, try again...")
        continue

    number = int(number)

    if number <= 0:
        print("Not a natural number, please, try again...")
        continue

    count_of_el = my_list.count(number)

    idx = binarySearch(my_list, int(number), 0, len(my_list) - 1)

    pos = idx + count_of_el

    if idx != -1:
        my_list.insert(pos, number)
    else:
        for el in my_list:
            if number > el:
                my_list.insert(my_list.index(el), number)
                flag = 1
                break
        if(flag):
            print(my_list)
            continue
        my_list.insert(len(my_list), number)

    print(my_list)