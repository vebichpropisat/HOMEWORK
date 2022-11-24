def memorize(fun):
    mem = {}

    def wrapper(*args):
        if args in mem:
            print("mem")
            return mem[args]
        else:
            print("rv")
            rv = fun(*args)
            mem[args] = rv
            return rv

    return wrapper
#
#
# @memorize
# def func(a, b) -> int:
#     return a * b
#
#
# # print("start")
# print(func(2, 5))
# print(func(2, 5))
# print("end")
#
# def error_handler(fun):
#     def wrapper(*args):
#         rv = 0
#         try:
#             rv = fun(*args)
#         except:
#             print(f"Ошибка функции - {fun.__name__}")
#         return rv
#
#     return wrapper
#
#
# @error_handler
# def dev(a, b) -> int:
#     return a / b
#
#
# print(dev(10, 2))
# print(dev(10, 0))
# permissions = ["user"]
#
#
# def check_permission(perm):
#     def wrapper_permission(fun):
#         def check_wrapper():
#             if perm not in permissions:
#                 raise ValueError("Нет доступа")
#             return fun()
#         return check_wrapper
#
#     return wrapper_permission
# #
# #
# @check_permission("user")
# def any_user():
#     print("Есть доступ")
#
#
# @check_permission("admin")
# def for_admin():
#     print("Для admin")
#
#
# any_user()
# for_admin()
