def main():
    # list_numbers = [1, 2, 3, 4, 5]
    # print(list_numbers)
    # empty = []
    # print(empty)
    list_numbers = [1, "Hi", [3, 4], 5]
    # print(list_numbers)
    # list_numbers[3] = "Test"
    list_numbers.append("Test")
    print(list_numbers)

# main()

def my_list():
    names = ["Иван", "Мария", "Петр", "Андрей", "Лена"]
    friend_name = input("Введите имя для проверки ")
    for name in names:
        if friend_name == name:
            print(f"Имя {friend_name} найдено")

# my_list()

def search_name():
    list_name = ["Иван", "Мария", "Петр", "Андрей", "Лена"]
    name = input("Введите имя для проверки ")
    name = name.title()
    if name in list_name:
        print(f"Имя {name} найдено")
    else:
        print(f"Имя {name} не найдено")

search_name()