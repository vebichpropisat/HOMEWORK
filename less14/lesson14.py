def my_decorator_class(cls):
    class MyCls:
        def __init__(self, *args, **kwargs):
            # как создали этот MyCls, также создадим и декорируемый класс
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                # проверяю это атребут ли класса MyCls
                x = super().__getattribute__(s)
            except AttributeError:
                # нет
                pass
            else:
                # да, это атребут ли класса MyCls
                return x
            # пробую вызвать атрибут обьекта
            attr = self._obj.__getattribute__(s)
            # метод ли он?
            if isinstance(attr, type(self.__init__)):
                # да
                print("Вызван метод: ", attr)
                return attr
            else:
                # не метод
                print("Значение: ", attr)
                return attr

    return MyCls


@my_decorator_class
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def set_age(self, value):
        self.__age = value

    def get_age(self):
        print(self.__age)


person = Person("John")
person.get_age()
person.set_age(25)
person.get_age()
print(person.name)
