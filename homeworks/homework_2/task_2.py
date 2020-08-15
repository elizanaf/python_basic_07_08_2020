"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
3. Пользователь вводит месяц в виде целого числа от 1 до 12. С
"""

my_list = []


while True:
    data = input("Enter the element of the list, please...   ")
    if data == '':
        print("EOF")
        break
    my_list.append(data)

print(my_list)
count_of_elements = len(my_list)

i = 0
while i < count_of_elements:
    tmp = my_list[i + 1]
    my_list.insert(i, tmp)
    my_list.pop(i+1)



    i += 1
    count_of_elements -=1
    print("ok")




print(my_list)