import random


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank in "Т":
            return 11
        elif self.rank in "ВДК":
            return 10
        else:
            return f"  234567890".index(self.rank)

    def get_rank(self) -> str:
        if self.rank == "0":
            self.rank = "10"
        return f"{self.suit}{self.rank}"


class DeskCard:
    def __init__(self) -> None:
        _rank = f"234567890ВДКТ"
        _suit = "ПБЧК"
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) -> Card:
        return self.__cards.pop()


class Player:
    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name
        self.t = 0

    @property
    def hand(self) -> str:
        return f"Карты в руке: {self._hand}; Очков - {self.count}"

    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())
        if "Т" in card.get_rank():
            self.t += 1
        if self.count > 21 and self.t > 0:
            self.count -= 10
            self.t -= 1


class Dealer(Player):
    def get_cards(self, cards: DeskCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break


class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name="Dealer")

    def print(self) -> str:
        return f"\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}\n{self.dealer.hand}"

    def check_count(self) -> None:
        if self.player.count > 21:
            print(f"Вы проиграли", self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f"Вы победили!!!", self.print())
        elif self.dealer.count == self.player.count:
            print(f"Ничья", self.print())
        elif self.dealer.count > self.player.count:
            print(f"Вы проиграли", self.print())
        elif self.dealer.count < self.player.count:
            print(f"Вы победили!!!", self.print())

    def start(self) -> None:
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)

        while self.player.count < 21:
            answer = input("Карту? y/n ")
            if answer == "y":
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == "n":
                self.dealer.get_cards(self.cards)
                break
        self.check_count()


def main() -> None:
    name = input("Ваше имя ")
    game = Game(name)
    game.start()


if __name__ == "__main__":
    main()
