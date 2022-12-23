from enum import Enum
from random import randint

from board import *

STARTING_CASH_AMOUNT = 1500


class PropertyGroupColor(Enum):
    BROWN = 1
    CYAN = 2
    MAGENTA = 3
    ORANGE = 4
    RED = 5
    YELLOW = 6
    GREEN = 7
    BLUE = 8


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
    def __init__(self, player_name, location_id) -> None:
        self.player_name = player_name
        self.location = location_id
        self.properties = []
        self.cash = STARTING_CASH_AMOUNT
        self.in_jail = False


class Die(object):
    def __init__(self, minimum, maximum) -> None:
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

if __name__ == "__main__":
    print(BOARD)
