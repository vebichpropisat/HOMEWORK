def main():
    play_list = ["sound1", "sound2", "sound3", "sound4", "sound5"]
    print(play_list)
    one = play_list.index(input("Введите первый трек "))
    two = play_list.index(input("Введите второй трек "))
    play_list[one], play_list[two] = play_list[two], play_list[one]
    print(play_list)


if __name__ == "__main__":
    main()
