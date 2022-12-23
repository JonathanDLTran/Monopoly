from random import randint

from board import *

STARTING_CASH_AMOUNT = 1500


class Card(object):
    pass


class Location(Card):
    def __init__(self, name, price, fee) -> None:

        super().__init__()
        self.name = name
        self.price = price
        self.fee = fee
        self.bought = False
        self.owner = None


class Go(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class Property(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class CommunityChest(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class Chess(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class Penalty(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class Nop(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class Jail(Location):
    def __init__(self, name, price, fee) -> None:
        super().__init__(name, price, fee)


class Player(object):
    def __init__(self, player_name, location_id) -> None:
        self.player_name = player_name
        self.location = location_id
        self.properties = []
        self.cash = STARTING_CASH_AMOUNT


class Die(object):
    def __init__(self, minimum, maximum) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def roll(self):
        return randint(self.minimum, self.maximum)


class Board(object):
    def __init__(self, locations) -> None:
        self.locations = locations

    def print_board(self):
        print("---------")


class Monopoly(object):
    def __init__(self) -> None:
        self.board = None


PROPERTIES = [
    Go("Go", 1000, 100),

]

if __name__ == "__main__":
    print(BOARD)
