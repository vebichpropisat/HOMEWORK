class Room:
    def __init__(self, l=0, w=0):
        self.l = l
        self.w = w

    def get_s(self):
        return self.l * self.w

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.get_s() + other
        elif isinstance(other, Room):
            return self.get_s() + other.get_s()
        return 0


class House:
    def __init__(self, *args):
        self.rooms = []
        while True:
            command = input("Добавить комнату? (д/н) ")
            if command == "д":
                ll = int(input("Введите длинну комнаты "))
                ww = int(input("Введите ширину комнаты "))
                self.rooms.append(Room(ll, ww))
            else:
                break
        self.s = 0

    def get_s(self):
        for room in self.rooms:
            self.s += room.get_s()
        return self.s


house = House()
print(f"Площадь дома = {house.get_s()}")
