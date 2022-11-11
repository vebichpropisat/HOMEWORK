def main():
    to_do = []
    while True:
        command = input(
            "1 - Добвить\n2 - Удалить\n3 - Просмотр\n" "4 - Закончить\nВведите команду "
        )
        if command == "1":
            do = input("Что будем делать? ")
            to_do.append(do)
        elif command == "2":
            do = input("Что больше не будем делать? ")
            if do in to_do:
                to_do.remove(do)
        elif command == "3":
            for do in to_do:
                print(f"{do}")
        elif command == "4":
            break


if __name__ == "__main__":
    main()
