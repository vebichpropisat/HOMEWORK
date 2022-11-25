# class MyClassFunc:
#     def __call__(self, a, b):
#         print(a + b)
#
#
# fun = MyClassFunc()
# fun(2, 6)


# class MyDecorator:
#     def __init__(self, func):
#         print('метод __init__')
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('перед вызовом wrapper', self.func.__name__)
#         rv = self.func(*args, **kwargs)
#         print('после вызовом wrapper')
#         return rv
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class MyDecorator:
#     def __init__(self, name):
#         print('__init__:', name)
#         self.name = name
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             print('до функции')
#             func(a, b)
#             print('после функции')
#         return wrapper
#
#
# @MyDecorator("test2")
# def add(a, b):
#     print('функция add', a, b)
#
#
# print('старт')
# add(10, 20)
# print('конец')


# def decorator(name):
#     print('decorator:', name)
#
#     def real_decorator(func):
#         print('сам декоратор', func.__name__)
#
#         def decorated(*args, **kwargs):
#             print('до функции', func.__name__)
#             ret = func(*args, **kwargs)
#             print('после функции', func.__name__)
#             return ret
#
#         return decorated
#
#     return real_decorator
#
#
# @decorator('test')
# def add(a, b):
#     print('функция add')
#     return a + b
#
#
# print('старт')
# r = add(10, 10)
# print(r)
# print('конец')
from functools import wraps


def my_decorator(func):
    """Декоратор"""

    @wraps(func)
    def decorated():
        """Функция decorated"""
        func()

    return decorated


@my_decorator
def wrapped():
    """Оборачивемая функция"""
    print("функция wrapped")


# print('старт')
# print(wrapped.__name__)
# print(wrapped.__doc__)


@my_decorator
class My:
    def __init__(self, a):
        print(a)


my = My("Hi")
