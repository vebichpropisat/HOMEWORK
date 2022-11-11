def main():
    play_list = ["sound1", "sound2", "sound3", "sound4", "sound5"]
    print(play_list)
    one = input("Введите первый трек ")
    two = input("Введите второй трек ")
    one = play_list.index(one)
    two = play_list.index(two)
    play_list[one], play_list[two] = play_list[two], play_list[one]
    print(play_list)


if __name__ == "__main__":
    main()
