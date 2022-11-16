def main() -> None:
    my_string = "fsjf78 u95dfd3fl l1d 7"
    my_string += " "
    numbers = []
    temp = ""
    for i in my_string:
        if i.isdigit():
            temp += i
        elif temp:
            numbers.append(int(temp))
            temp = ""
    print(numbers)


if __name__ == "__main__":
    main()
