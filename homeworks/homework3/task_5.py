"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
import string




def is_alpha(str):
    """Checks if a letter was not entered by user.

    :param str: string
    :return: int
    """
    flag = 0
    for el in str:
        if el.isalpha():
            print("You entered not a number. Please, try again...")
            flag = 1

    return flag




def del_punc(str):
    """Deletes all the punctuation symbols from the string.

    :param str: string
    :return: string
    """
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    str = str.translate(tt)
    return str


def num_count():
    """Reads the input of the user and counts the sum of entered numbers.

    :return:
    """

    my_list = []
    sum = 0
    while True:
        flag = 0
        length = 0
        str = input("Enter numbers...")
        length = len(str)
        if str == '.':
            return

        if is_alpha(str):
            continue

        if str[-1] == '.':
            my_list.clear()
            str = del_punc(str)

            if length > len(str):
                print("You entered not a number. Please, try again...")
                continue

            my_list = str.split(' ')
            for el in my_list:
                if el == '':
                    continue
                sum += float(el)
            print(sum)
            return

        str = del_punc(str)

        if length > len(str):
            print("You entered not a number. Please, try again...")
            continue

        my_list = str.split(' ')
        for el in my_list:
            if el == '':
                continue
            sum += float(el)

        print(sum)



num_count()