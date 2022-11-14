def main():
    to_do = ['Task']
    while True:
        command = input("1 - Добвить\n2 - Удалить\n3 - Просмотр\n4 - Изменить\nВведите команду ")
        if command == "1":
            task = input("Что будем делать? ")
            to_do.append(task)
        elif command == "2":
            task_number = int(input("Введите номер задачи "))
            task = to_do.pop(task_number)
            print(f"Задача {task} удалена")
        elif command == "3":
            for i, task in enumerate(to_do):
                print(f"# {i} - {task}")
        elif command == "4":
            task_number = int(input("Введите номер задачи "))
            task = input("Введите задачу ")
            to_do[task_number] = task


# if __name__ == "__main__":
#     main()


def my_todo():
    to_do = ['Task']
    while True:
        command = input("1 - Добвить\n2 - Удалить\n3 - Просмотр\n4 - Изменить\nВведите команду ")
        if command == "1":
            task = input("Что будем делать? ")
            to_do.append(task)
        elif command == "2":
            try:
                task_number = int(input("Введите номер задачи "))
            except ValueError:
                print("Вы ввели не число")
                continue
            try:
                task = to_do.pop(task_number)
            except IndexError:
                print(f"Задача {task_number} не найдена")
            else:
                print(f"Задача {task} удалена")
        elif command == "3":
            for i, task in enumerate(to_do):
                print(f"# {i} - {task}")
        elif command == "4":
            task_number = int(input("Введите номер задачи "))
            task = input("Введите задачу ")
            # to_do[task_number] = task
            to_do.insert(task_number, task)


my_todo()