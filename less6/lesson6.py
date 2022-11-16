import re


def main() -> None:
    my_string = "fsjf78 u95dfd3fl l1d 7"
    numbers = []
    temp = ""
    for i in my_string:
        if i.isdigit():
            temp += i
        elif temp:
            numbers.append(int(temp))
            temp = ""
    if i.isdigit():
        numbers.append(int(i))
    print(numbers)


# main()


def search_number() -> None:
    my_string = "fsjf78 u95dfd3fl l1d 7"
    nums = re.findall("[0-9]+", my_string)
    numbers = []
    for i in nums:
        numbers.append(int(i))
    print(numbers)


# search_number()


def sesrch() -> None:
    my_string = "fsjf78 u95dfd3fl l1d 7"
    numbers = [int(i) for i in re.findall("\d+", my_string)]
    print(numbers)


sesrch()
