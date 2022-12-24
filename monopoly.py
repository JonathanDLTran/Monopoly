from time import sleep
import emoji
from enum import Enum
from random import randint

from board import *
from utilities import *

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
    CAR = emoji.emojize(":car:", language="alias")
    HAT = emoji.emojize(":top_hat:", language="alias")

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()


REMAINING_SYMBOLS = [PlayerSymbol.DOG, PlayerSymbol.SHOE,
                     PlayerSymbol.CAR, PlayerSymbol.HAT]


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
        self.__symbol = ""

        self.__location = 0
        self.properties = []

        self.cash = STARTING_CASH_AMOUNT
        self.in_jail = False

    def setup(self):
        name = input("Please input your name: ")
        symbol = get_symbol()

        self.player_name = name
        self.__symbol = symbol

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def symbol(self):
        return self.__symbol

    def __str__(self) -> str:
        return f"{self.player_name} | {self.__symbol}"

    def __repr__(self) -> str:
        return self.__str__()


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

NUM_PROPERTIES = 40  # len(PROPERTIES)
assert NUM_PROPERTIES > 0


def game_over():
    pass


def player_one_round(player):

    # roll dice
    print("Rolling dice ...")
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    print(f"{die1}, {die2}")
    number_steps = die1 + die2
    player.location = (player.location + number_steps) % NUM_PROPERTIES

    # user gives input


def setup_players(n_players):
    players = []
    for _ in range(n_players):
        p = Player()
        p.setup()
        players.append(p)
    return players


def main():
    n_players = get_uint_input("Please enter the number of players: ",
                               "Number of players must be an integer between 1 and 4.", 1, 4)
    players = setup_players(n_players)

    print(build_board(players))
    # for p in players:
    #     player_one_round(p)
    # print(build_board(players))

    while True:
        sleep(0.5)
        for p in players:
            player_one_round(p)
        print(build_board(players))


if __name__ == "__main__":
    main()
