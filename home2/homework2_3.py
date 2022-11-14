def main():
    to_do = []
    while True:
        command = input(
            "1 - Добвить\n2 - Удалить\n3 - Просмотр\n4 - Изменить\n5 - Закончить\nВведите команду "
        )
        if command == "1":
            do = input("Что будем делать? ")
            to_do.append(do)
        elif command == "2":
            number = int(input("Что больше не будем делать?(введите номер) ")) - 1
            do = to_do.pop(number)
            print(f"Действие {do} удалено")
        elif command == "3":
            for i, do in enumerate(to_do):
                print(f"# {i + 1} - {do}")
        elif command == "4":
            number = int(input("Введите номер задачи ")) - 1
            do = input("Что будем делать? ")
            to_do[number] = do
        elif command == "5":
            break


if __name__ == "__main__":
    main()
