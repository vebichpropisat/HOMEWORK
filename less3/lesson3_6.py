name = "Mike"


def func():
    # name = "John"
    # print(f'Var name in func = {name}')
    i = 4
    print(i)
    i = "Mike"
    print(i)


func()
# print(name)


def func_2():
    global name_2
    name_2 = "Lena"
    print(f'Var name_2 in func_2 = {name_2}')


def func_3():
    # name_2 = "Bob"
    print(f'Var name_2 in func_3 = {name_2}')


# func_2()
# func_3()
