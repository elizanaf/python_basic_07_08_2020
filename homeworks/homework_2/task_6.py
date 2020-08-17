"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

my_list = []
my_tuple = ()

count = 0


while True:
    name = input("Please, enter the name of the product...   ")
    if name == '':
        break
    price = input("Please, enter the price of the product...   ")
    if price.isalpha():
        print("Error...")
        exit(1)
    if price == '':
        break
    amount = input("Please, enter the amount of the product...   ")
    if price.isalpha():
        print("Error...")
        exit(1)
    if price == '':
        break
    unit = input("Please, enter the unit of the product...   ")
    if unit == '':
        break

    count += 1

    my_tuple = (count, {"name" : name, "price" : price, "amount" : amount, "unit" : unit})

    my_list.append(my_tuple)

    print(my_list)

result_dict = {}
result_list_name = []
result_list_price = []
result_list_amount = []
result_list_unit = []

for el1 in my_list:
    result_list_name.append(el1[1].setdefault("name"))
    result_dict.update({"name": result_list_name})

    result_list_price.append(el1[1].setdefault("price"))
    result_dict.update({"price": result_list_price})

    result_list_amount.append(el1[1].setdefault("amount"))
    result_dict.update({"amount": result_list_amount})

    result_list_unit.append(el1[1].setdefault("unit"))
    result_dict.update({"unit": result_list_unit})



print("RESULT:\n",result_dict)


