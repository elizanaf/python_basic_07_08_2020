"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
my_list = ['', "Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"]

print(my_list)

month = input("Enter a number from 1 to 12...")

if(not(month.isdigit())):
    print("Not a number!")
    exit(1)

month = int(month)

if(month < 1 or month > 12):
    print("The month does not exist!")
    exit(1)

print(my_list[month])