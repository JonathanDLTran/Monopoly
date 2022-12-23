from board import *

STARTING_CASH_AMOUNT = 1500


class Card(object):
    pass


class Property(Card):
    def __init__(self, name, price, fee) -> None:

        super().__init__()
        self.name = name
        self.price = price
        self.fee = fee
        self.bought = False
        self.owner = None
        self.handler = lambda: print("No Handler")


class CommunityChest(Card):
    def __init__(self) -> None:
        super().__init__()


class Chance(Card):
    def __init__(self) -> None:
        super().__init__()


class Player(object):
    def __init__(self, player_name, location_id) -> None:
        self.player_name = player_name
        self.location = location_id
        self.properties = []
        self.cash = STARTING_CASH_AMOUNT


class Board(object):
    def __init__(self, locations) -> None:
        self.locations = locations

    def print_board(self):
        print("---------")


class Monopoly(object):
    def __init__(self) -> None:
        self.board = None


PROPERTIES = [
    Property("Go", 1000, 100),
    Property("Boardwalk", 1000, 100),
    Property("Atlantic Avenue", 1000, 100),
]

if __name__ == "__main__":
    print(BOARD)
