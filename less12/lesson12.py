# def first(msg):
#     print(msg)
#
#
# first("Hello")
#
# second = first
# second("Hello")

###


# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operate(func, x):
#     result = func(x)
#     return result
#
#
# print(operate(inc, 3))
# print(operate(dec, 3))


#
# def is_called():
#     def is_returned():
#         print("Hello")
#     return is_returned
#
#
# new = is_called()
#
#
# new()

###


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


#
#
# ordinary()
# pretty = make_pretty(ordinary)
# pretty()

##

# @make_pretty
# def ordinary():
#     print("i am ordinary")
#
# ordinary()


def smart_divide(func):
    def inner(*args, **kwargs):
        print("I am going to divide")
        return func(*args, **kwargs)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


#
# divide(2, 5)
###


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


# @star
# @percent
def printer(msg):
    print(msg)


# printer("Hello")


printer = star(percent(printer))
printer("Hi")
