def main():
    contacts = {"Петя": 111222, "Лена": 443322, "Андрюха": 564235}
    while True:
        command = input(
            "1 - Добвить\n2 - Удалить\n3 - Просмотр\n"
            "4 - Изменить номер\n5 - Закончить\nВведите команду "
        )
        if command == "1":
            name = input("Введите имя ")
            name = name.title()
            if contacts.get(name):
                print("Такое имя уже существует")
                continue
            tel = int(input("Введите телефон "))
            contacts[name] = tel
        elif command == "2":
            name = input("Введите имя ")
            name = name.title()
            if contacts.get(name):
                contacts.pop(name)
                print(f"Контакт {name} удален")
            else:
                print(f"Имя {name} не найдено")
        elif command == "3":
            for name, phone in contacts.items():
                print(f"{name} - {phone}")
        elif command == "4":
            name = input("Введите имя ")
            name = name.title()
            if contacts.get(name):
                phone = int(input("Введите новый номер "))
                contacts[name] = phone
                print(f"Номер телефона контакта {name} изменен")
            else:
                print(f"Имя {name} не найдено")
        elif command == "5":
            break


main()
