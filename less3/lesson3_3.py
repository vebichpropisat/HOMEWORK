def func():
    play_list = ['1', '2', "sound3", "sound5", "sound5"]
    # play_list = ['1', '2']
    ints = []

    try:
        for line in play_list:
            ints.append(int(line))
    except ValueError:
        print('Это не число.')
    # else:
    #     print('Всё хорошо.')
    # finally:
    #     print(ints)


func()