import emoji
from enum import Enum
from random import randint

from board import *

STARTING_CASH_AMOUNT = 1500

MAX_PLAYERS = 4


class PropertyGroupColor(Enum):
    BROWN = 1
    CYAN = 2
    MAGENTA = 3
    ORANGE = 4
    RED = 5
    YELLOW = 6
    GREEN = 7
    BLUE = 8


class PlayerSymbol(Enum):
    DOG = emoji.emojize(":dog:", language="alias")
    SHOE = emoji.emojize(":shoe:", language="alias")
    IRON = emoji.emojize(":thumbsup:", language="alias")
    HAT = emoji.emojize(":red_heart:", language="alias")

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()


REMAINING_SYMBOLS = [PlayerSymbol.DOG, PlayerSymbol.SHOE,
                     PlayerSymbol.IRON, PlayerSymbol.HAT]


def get_symbol():
    if REMAINING_SYMBOLS == []:
        raise RuntimeError("No More Symbols Remaining")
    symbol = REMAINING_SYMBOLS.pop()
    return symbol


class Card(object):
    pass


class Location(Card):
    def __init__(self) -> None:
        pass


class Go(Location):
    def __init__(self, name) -> None:
        self.name = name


class Property(Location):
    def __init__(self, name, color, price, fee) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.price = price
        self.fee = fee
        self.bought = False
        self.owner = None


class CommunityChest(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__()


class Chess(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__()


class Penalty(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__()


class Nop(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__()


class Jail(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__()


class Player(object):
    def __init__(self) -> None:
        self.player_name = ""
        self.symbol = ""

        self.location = 0
        self.properties = []

        self.cash = STARTING_CASH_AMOUNT
        self.in_jail = False

    def setup(self):
        name = input("Please input your name: ")
        symbol = get_symbol()

        self.player_name = name
        self.symbol = symbol

    def __str__(self) -> str:
        return f"{self.player_name} | {self.symbol}"

    def __repr__(self) -> str:
        return self.__str__()


class Die(object):
    def __init__(self, minimum=1, maximum=6) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def roll(self):
        return randint(self.minimum, self.maximum)


class Board(object):
    def __init__(self, locations) -> None:
        self.locations = locations

    def __str__(self) -> str:
        return BOARD

    def __repr__(self) -> str:
        return self.__str__()


class Monopoly(object):
    def __init__(self) -> None:
        self.board = None


PROPERTIES = [
    Go("Go"),
    # Property("Mediterranean Avenue", PropertyGroupColor.BROWN, )
]


def main():
    num_players = int(input("Please enter the number of players: "))
    for _ in range(num_players):
        p = Player()
        p.setup()
        print(p)


if __name__ == "__main__":
    main()
