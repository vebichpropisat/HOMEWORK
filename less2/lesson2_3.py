def main():
    play_list = ["sound1", "sound2", "sound3", "sound4", "sound5"]
    print(play_list)

    # s1 = play_list[1]
    # s2 = play_list[3]
    # play_list[1] = s2
    # play_list[3] = s1

    # play_list[1], play_list[3] = s2, s1

    play_list[1], play_list[3] = play_list[3], play_list[1]
    print(play_list)


main()


def func():
    # my_list = [1, 2, 3, 4]
    # a, *b, c = my_list
    a, b = 1, 2
    print(a)
    print(b)
    # print(c)


# func()
