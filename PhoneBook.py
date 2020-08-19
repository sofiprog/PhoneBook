from PhoneBook_lib import *

phone_book = dict()

welcome()  # Ввод приветствия программы

while True:
    menu()  # Вывод пунктов меню
    choice = int(input("Введите режим работы: "))

    if choice == 1:  # Вывод на экран всех записей
        show(phone_book)
    elif choice == 2:  # Добавление записи
        input_record(phone_book)
    elif choice == 3:  # Редактирование записи
        edit_record(phone_book)
    elif choice == 4:  # Удаление записи
        delete_record(phone_book)
    elif choice == 5:  # Сохранение данных в файл
        export_to_file(phone_book)
    elif choice == 0:  # Выход из программы
        print("До свидания")
        break
    else:
        print("Неправильный режим")
