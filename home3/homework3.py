def piz(ingredients: tuple) -> str:
    pizza = []
    for ing in ingredients:
        command = input(f"Добавить {ing}? (Да/Нет) ").title()
        if command == "Да":
            pizza.append(ing)
    if not pizza:
        print("Вы ничего не заказали")
        command = "Нет"
    else:
        print("Пицца:")
        for ing in pizza:
            print(f"{ing}")
        command = input("Заказ верный? (Да/Нет) ").title()
    return command


def main() -> None:
    ingredients = ("сыр", "перец", "ананасы", "помидоры", "маслины", "грибы", "огурци")
    command = input("Хотите ли вы сделать заказ? (Да/Нет) ").title()
    while command == "Да":
        command = piz(ingredients)
        if command == "Да":
            print("Заказ принят. Ожидайте")
            break
        elif command == "Нет":
            command = input("Хотите ли вы сделать заказ заново? (Да/Нет) ").title()
    if command == "Нет":
        print("Заказ отменен")


if __name__ == "__main__":
    main()
