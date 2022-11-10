import random


def main():
    while True:
        random_number = random.randint(0, 10)
        user_number = int(input("Введите число "))

        if random_number == user_number:
            print("Вы выйграли")
        else:
            print("Вы проиграли")

        answer = input("Играть еще? ")

        if answer == "Нет":
            break
        elif answer == "Да":
            continue


if __name__ == "__main__":
    main()
