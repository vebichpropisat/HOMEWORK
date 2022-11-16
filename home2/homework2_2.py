import json


def name_input():
    name = input("Введите имя ").title()
    return name


def func():
    with open("homework2_2_file.json", encoding="utf-8") as f:
        contacts = json.load(f)
    while True:
        command = input(
            "1 - Добвить\n2 - Удалить\n3 - Просмотр\n" "4 - Закончить\nВведите команду "
        )
        if command == "1":
            name = name_input()
            if contacts.get(name):
                print("Такое имя уже существует")
                continue
            car = input("Введите марку машины ")
            contacts[name] = car
        elif command == "2":
            name = name_input()
            if contacts.get(name):
                contacts.pop(name)
                print(f"{name} уехал")
            else:
                print(f"Водитель {name} не найдено")
        elif command == "3":
            for name, car in contacts.items():
                print(f"{name} - {car}")
        elif command == "4":
            break
        with open("homework2_2_file.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(contacts))
            print("Данные сохранены")


if __name__ == "__main__":
    func()
