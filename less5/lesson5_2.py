def two_list() -> None:
    list_names = ["John", "Bob", "Mike", "Anna"]
    get_names = ["Bob", "Elena", "Anna", "Victor"]
    # new_list = list(set(list_names + get_names))
    # new_list = list(set(list_names) - set(get_names))
    # new_list = list(set(list_names) ^ set(get_names))
    new_list = list(set(list_names) & set(get_names))
    print(new_list)


if __name__ == "__main__":
    two_list()
