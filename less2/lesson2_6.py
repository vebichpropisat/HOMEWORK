def main():
    contacts = {"Петя": 111222, "Лена": 443322, "Андрюха": 564235}
    while True:
        command = input("1 - Добвить\n2 - Удалить\n3 - Просмотр\nВведите команду ")
        if command == '1':
            name = input("Введите имя ")
            if contacts.get(name):
                print("Такое имя уже существует")
                continue
            tel = int(input("Введите телефон "))
            contacts[name] = tel
        elif command == '2':
            name = input("Введите имя ")
            if contacts.get(name):
                contacts.pop(name)
                print(f"Контакт {name} удален")
            else:
                print(f"Имя {name} не найдено")
        elif command == '3':
            for name, phone in contacts.items():
                print(f"{name} - {phone}")

# main()

def func():
    contacts = {"Петя": "BMW", "Лена": "AUDI", "Андрюха": "Mazda"}
    print(contacts)

func()