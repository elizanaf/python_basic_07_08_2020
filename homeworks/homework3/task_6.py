"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(str):
    """Returns the word as a title.

    :param str: string
    :return: string
    """
    return str.title()

def if_low_case(str):
    """Checks if every letter is low.

    :param str: string
    :return: int
    """
    flag = 0
    for el in str:
        if el >= 'A' and el <= 'Z':
            flag = 1
    return flag



def convert_to_title():
    """Converts every word of the sentence to the title.

    :return:
    """
    while True:
        str = input("Please, enter your string...")

        if if_low_case(str):
            print("Enter words with lower letters...Try again...")
            continue

        break
    my_list = str.split(' ')

    for el in my_list:
        print(int_func(el), end = ' ')




a()