def func():
    pass


# func()


def my_name(name):
    print(name)


# my_name("Mika")


def calc(a, b=5):
    c = a + b
    return c


result = calc("hi")
print(result)


def my_func(*args):
    print(args)
    print(type(args))


# my_test_list = [1, 2, 3, "Hi", 4]
# my_func(*my_test_list)


def my_func_2(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))


# my_test_dict = {"key": 1, "word": "Hi", "number": 4}
# my_func_2(my_test_dict)


def my_func_3(b, **kwargs):
    # print(a)
    print(b)
    # print(args)
    print(kwargs)


# my_func_3("test", key=1, key2=44)
