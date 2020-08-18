# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from PhoneBook_lib import *

phone_book = dict()

welcome()

while True:
    menu()
    choice = int(input("Введите режим работы: "))

    if choice == 1:
        print(phone_book)
    elif choice == 2:    # TODO сделать проверку существования телефона в справочнике
        tel = input("Введите номер телефона: ")
        value = input_data()
        phone_book[tel] = value
    elif choice == 3:   # TODO Редактирование записи
        print()
    elif choice == 4:   # TODO удаление записи
        print()
    elif choice == 0:   
        print("До свидания")
        break
    else:
        print("Неправильный режим")
        continue
