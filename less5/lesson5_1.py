def func_one() -> None:
    animals = {"Tiger", "Cat", "Dog", "Pig"}
    print(animals)
    print(type(animals))


# func_one()


def func_two() -> None:
    animals = {"Tiger", "Cat", "Tiger", "Dog", "Pig", "Dog"}
    print(animals)


# func_two()


def func_three() -> None:
    animals = {"Tiger", "Cat"}
    print(animals)
    animals.add("Tiger")
    print(animals)


# func_three()


def func_four() -> None:
    animals = set("Tiger")
    print(animals)
    animals.add("Dog")
    print(animals)


# func_four()


def func_five() -> None:
    animals = {"Tiger", "Cat"}
    print(animals)
    # animals.update("Dog")
    # print(animals)
    dog = {"Dog", "Cat"}
    # animals.update(dog)
    # print(animals)

    # result = animals.intersection(dog)
    result = animals.difference(dog)
    print(result)


# func_five()


def func_six() -> None:
    animals = {"Tiger", "Cat"}
    for i in animals:
        print(i)


# func_six()


def func_seven() -> None:
    animals = frozenset(["Tiger", "Cat"])
    print(animals)
    print(type(animals))


func_seven()
