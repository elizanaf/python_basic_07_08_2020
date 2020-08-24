"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
import string

def data_f (name : string = "None", surname : string = "None", year_of_birth : string = "None", native_town : string = "None", email : string = "None", phone : string = "None") :
    """Writes data in one string.

    :param name: string
    :param surname: string
    :param year_of_birth: string
    :param native_town: string
    :param email: string
    :param phone: string
    :return:
    """
    print(name + " ," + surname + " ," + year_of_birth + " ," + native_town + " ," + email + " ," + phone)


name = input("Enter the name... ")
if name.isdigit():
    print("ERROR in the format of name.")
    name = "None"
surname = input("Enter the surname...")
if surname.isdigit():
    print("ERROR in the format of surname.")
    surname = "None"
year_of_birth = input("Enter the year of birth... ")
if year_of_birth.isalpha():
    print("ERROR in the format of year of  birth.")
    year_of_birth = "None"
native_town = input("Enter the native town... ")
if native_town.isdigit():
    print("ERROR in the format of native town.")
    native_town = "None"
email = input("Enter the email... ")
phone = input("Enter the phone... ")
if phone.isalpha():
    print("ERROR in the format of phone.")
    phone = "None"

data_f(name, surname, year_of_birth, native_town, email, phone)