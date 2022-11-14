def calc(numbers):
    i = 0
    for number in numbers:
        i += int(number)
    return i


def test():
    print("Hi")


def main():
    numbers = input("Введите числа через запятую ")
    list_number = numbers.split(", ")
    result = calc(list_number)
    print(result)
    my_test = test()
    print(my_test)


if __name__ == "__main__":
    main()
