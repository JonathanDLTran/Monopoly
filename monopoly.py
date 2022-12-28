from copy import deepcopy
import emoji
from enum import Enum
from random import randint
from time import sleep

from board import *
from constants import *
from utilities import *


class PropertyGroupColor(Enum):
    BROWN = 1
    CYAN = 2
    MAGENTA = 3
    ORANGE = 4
    RED = 5
    YELLOW = 6
    GREEN = 7
    BLUE = 8

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()


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
    def __init__(self, name, color, deed_price, house_price, rent, mortgage) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.deed_price = deed_price
        self.house_price = house_price
        self.rent = rent
        self.mortgage = mortgage

    def __str__(self) -> str:
        return f"Property Name: {self.name} | Color Group: {self.color} | Deed Price: {self.deed_price} | House Price: {self.house_price} | Rent: {list(zip(['Deed Only', '1 House', '2 Houses','3 House', '4 Houses', 'Hotel'], self.rent))} | Mortgage Amount: {self.mortgage}"

    def __repr__(self) -> str:
        return self.__str__()


class Railroad(Location):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.deed_price = 200
        self.rent = [25, 50, 100, 200]
        self.mortgage = 100


class Utility(Location):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.deed_price = 150
        self.rent = [4, 10]
        self.mortgage = 75


class CommunityChest(Location):
    def __init__(self) -> None:
        super().__init__()


class Chance(Location):
    def __init__(self) -> None:
        super().__init__()


class Penalty(Location):
    def __init__(self) -> None:
        super().__init__()


class Nop(Location):
    def __init__(self) -> None:
        super().__init__()


class Jail(Location):
    def __init__(self) -> None:
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
        return f"{self.player_name} | {self.__symbol} | ${self.cash}"

    def __repr__(self) -> str:
        return self.__str__()


PROPERTIES = [
    Property(MEDITERRANEAN_AVENUE, PropertyGroupColor.BROWN,
             60, 50, [2, 10, 30, 90, 160, 250], 30),
    Property(BALTIC_AVENUE, PropertyGroupColor.BROWN,
             60, 50, [4, 20, 60, 180, 320, 450], 30),
    Property(ORIENTAL_AVENUE, PropertyGroupColor.CYAN,
             100, 50, [6, 30, 90, 270, 400, 550], 50),
    Property(VERMONT_AVENUE, PropertyGroupColor.CYAN,
             100, 50, [6, 30, 90, 270, 400, 550], 50),
    Property(CONNECTICUT_AVENUE, PropertyGroupColor.CYAN,
             120, 50, [8, 40, 100, 300, 450, 550], 60),
    Property(ST_CHARLES_PLACE, PropertyGroupColor.MAGENTA,
             140, 100, [10, 50, 150, 450, 625, 750], 70),
    Property(STATES_AVENUE, PropertyGroupColor.MAGENTA,
             140, 100, [10, 50, 150, 450, 625, 750], 70),
    Property(VIRGINIA_AVENUE, PropertyGroupColor.MAGENTA,
             160, 100, [12, 60, 180, 500, 700, 900], 80),
    Property(ST_JAMES_PLACE, PropertyGroupColor.ORANGE,
             180, 100, [14, 70, 200, 550, 750, 950], 90),
    Property(TENNESSEE_AVENUE, PropertyGroupColor.ORANGE,
             180, 100, [14, 70, 200, 550, 750, 950], 90),
    Property(NEW_YORK_AVENUE, PropertyGroupColor.ORANGE,
             200, 100, [16, 80, 220, 600, 800, 1000], 100),
    Property(KENTUCKY_AVENUE, PropertyGroupColor.RED,
             220, 150, [18, 90, 250, 700, 875, 1050], 110),
    Property(INDIANA_AVENUE, PropertyGroupColor.RED,
             220, 150, [18, 90, 250, 700, 875, 1050], 110),
    Property(ILLINOIS_AVENUE, PropertyGroupColor.RED,
             240, 150, [20, 100, 300, 750, 925, 1100], 120),
    Property(ATLANTIC_AVENUE, PropertyGroupColor.YELLOW,
             260, 150, [22, 110, 330, 800, 975, 1150], 130),
    Property(VENTNOR_AVENUE, PropertyGroupColor.YELLOW,
             260, 150, [22, 110, 330, 800, 975, 1150], 130),
    Property(MARVIN_GARDENS, PropertyGroupColor.YELLOW,
             280, 150, [24, 120, 360, 850, 1025, 1200], 140),
    Property(PACIFIC_AVENUE, PropertyGroupColor.GREEN,
             300, 200, [26, 130, 390, 900, 1100, 1275], 150),
    Property(NORTH_CAROLINA_AVENUE, PropertyGroupColor.GREEN,
             300, 200, [26, 130, 390, 900, 1100, 1275], 150),
    Property(PENNSYLVANIA_AVENUE, PropertyGroupColor.GREEN,
             320, 200, [28, 150, 450, 1000, 1200, 1400], 160),
    Property(PARK_PLACE, PropertyGroupColor.BLUE,
             350, 200, [35, 175, 500, 1100, 1300, 1500], 175),
    Property(BOARDWALK, PropertyGroupColor.BLUE,
             400, 200, [50, 200, 600, 1400, 1700, 2000], 200), ]

RAILROADS = [
    Railroad(READING_RAILROAD),
    Railroad(PENNSYLVANIA_RAILROAD),
    Railroad(B_AND_O_RAILROAD),
    Railroad(SHORT_LINE),
]

UTILITIES = [
    Utility(ELECTRIC_COMPANY),
    Utility(WATER_WORKS),
]


def game_over():
    pass


def get_property(name):
    global PROPERTIES

    new_properties = []
    final_property = None
    for prop in PROPERTIES:
        if prop.name != name:
            new_properties.append(prop)
        else:
            final_property = prop

    PROPERTIES = new_properties
    return final_property


def one_round(players):

    for player in players:
        print(build_board(players))

        # roll dice
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        print(f"Rolling dice... {die1}, {die2}.")
        number_steps = die1 + die2
        player.location = (player.location + number_steps) % NUM_PROPERTIES

        sleep(1)

        print(build_board(players))

        # user gives input
        while True:
            user_input = input("Please input a command: ")
            if user_input == "buy":
                location = player.location
                location_key = extend_int_to_string(location)
                if location_key in CAN_BUILD:
                    property_name = INDEX_TO_PROPERTY_MAP[location_key]
                    property_obj = get_property(property_name)
                    if property_obj != None:
                        player.properties.append(property_obj)
                        player.cash -= property_obj.deed_price
                        # handle bankruptcy
            elif user_input == "board":
                print(build_board(players))
            elif user_input == "user":
                print(player)
            elif user_input == "show properties":
                for prop in player.properties:
                    print(prop)
            elif user_input == "finish":
                break


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

    while True:
        start = input("Ready to start? ")
        if start == "Y":
            break

    while True:
        sleep(0.5)
        one_round(players)


if __name__ == "__main__":
    main()
