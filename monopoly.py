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
    def __init__(self, loc_id, name, color, deed_price, house_price, rent, mortgage) -> None:
        super().__init__()
        self.id = loc_id
        self.name = name
        self.color = color
        self.deed_price = deed_price
        self.house_price = house_price
        self.rent = rent
        self.mortgage = mortgage

        self.owner = None
        self.houses = 0

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
    def __init__(self, player_id) -> None:
        self.id = player_id
        self.name = ""
        self.__symbol = ""

        self.__location = 0

        self.cash = STARTING_CASH_AMOUNT
        self.in_jail = False

    def setup(self):
        name = input("Please input your name: ")
        symbol = get_symbol()

        self.name = name
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
        return f"{self.name} | {self.__symbol} | ${self.cash}"

    def __repr__(self) -> str:
        return self.__str__()


PROPERTIES = [
    Property("01", MEDITERRANEAN_AVENUE, PropertyGroupColor.BROWN,
             60, 50, [2, 10, 30, 90, 160, 250], 30),
    Property("03", BALTIC_AVENUE, PropertyGroupColor.BROWN,
             60, 50, [4, 20, 60, 180, 320, 450], 30),
    Property("06", ORIENTAL_AVENUE, PropertyGroupColor.CYAN,
             100, 50, [6, 30, 90, 270, 400, 550], 50),
    Property("08", VERMONT_AVENUE, PropertyGroupColor.CYAN,
             100, 50, [6, 30, 90, 270, 400, 550], 50),
    Property("09", CONNECTICUT_AVENUE, PropertyGroupColor.CYAN,
             120, 50, [8, 40, 100, 300, 450, 550], 60),
    Property("11", ST_CHARLES_PLACE, PropertyGroupColor.MAGENTA,
             140, 100, [10, 50, 150, 450, 625, 750], 70),
    Property("13", STATES_AVENUE, PropertyGroupColor.MAGENTA,
             140, 100, [10, 50, 150, 450, 625, 750], 70),
    Property("14", VIRGINIA_AVENUE, PropertyGroupColor.MAGENTA,
             160, 100, [12, 60, 180, 500, 700, 900], 80),
    Property("16", ST_JAMES_PLACE, PropertyGroupColor.ORANGE,
             180, 100, [14, 70, 200, 550, 750, 950], 90),
    Property("18", TENNESSEE_AVENUE, PropertyGroupColor.ORANGE,
             180, 100, [14, 70, 200, 550, 750, 950], 90),
    Property("19", NEW_YORK_AVENUE, PropertyGroupColor.ORANGE,
             200, 100, [16, 80, 220, 600, 800, 1000], 100),
    Property("21", KENTUCKY_AVENUE, PropertyGroupColor.RED,
             220, 150, [18, 90, 250, 700, 875, 1050], 110),
    Property("23", INDIANA_AVENUE, PropertyGroupColor.RED,
             220, 150, [18, 90, 250, 700, 875, 1050], 110),
    Property("24", ILLINOIS_AVENUE, PropertyGroupColor.RED,
             240, 150, [20, 100, 300, 750, 925, 1100], 120),
    Property("26", ATLANTIC_AVENUE, PropertyGroupColor.YELLOW,
             260, 150, [22, 110, 330, 800, 975, 1150], 130),
    Property("27", VENTNOR_AVENUE, PropertyGroupColor.YELLOW,
             260, 150, [22, 110, 330, 800, 975, 1150], 130),
    Property("29", MARVIN_GARDENS, PropertyGroupColor.YELLOW,
             280, 150, [24, 120, 360, 850, 1025, 1200], 140),
    Property("31", PACIFIC_AVENUE, PropertyGroupColor.GREEN,
             300, 200, [26, 130, 390, 900, 1100, 1275], 150),
    Property("32", NORTH_CAROLINA_AVENUE, PropertyGroupColor.GREEN,
             300, 200, [26, 130, 390, 900, 1100, 1275], 150),
    Property("34", PENNSYLVANIA_AVENUE, PropertyGroupColor.GREEN,
             320, 200, [28, 150, 450, 1000, 1200, 1400], 160),
    Property("37", PARK_PLACE, PropertyGroupColor.BLUE,
             350, 200, [35, 175, 500, 1100, 1300, 1500], 175),
    Property("39", BOARDWALK, PropertyGroupColor.BLUE,
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
    for prop in PROPERTIES:
        if prop.name == name:
            return prop
    raise RuntimeError(f"Cannot Find Property {prop}.")


def one_round(players):

    for player in players:
        print(build_board(players, PROPERTIES))

        # roll dice
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        print(f"Rolling dice... {die1}, {die2}.")
        number_steps = die1 + die2
        player.location = (player.location + number_steps) % NUM_PROPERTIES

        sleep(1)

        print(build_board(players, PROPERTIES))

        # user gives input
        while True:
            user_input = input("Please input a command: ")
            if user_input == "buy":
                location = player.location
                location_key = extend_int_to_string(location)
                if location_key in CAN_BUILD:
                    property_name = INDEX_TO_PROPERTY_MAP[location_key]
                    property_obj = get_property(property_name)
                    property_obj.owner = player.id
                    property_obj.houses += 1
                    player.cash -= property_obj.deed_price
                    # handle bankruptcy
            elif user_input == "board":
                print(build_board(players, PROPERTIES))
            elif user_input == "user":
                print(player)
            elif user_input == "show properties":
                for prop in PROPERTIES:
                    if prop.owner == player.id:
                        print(prop)
            elif user_input == "finish":
                break


def setup_players(n_players):
    players = []
    for _ in range(n_players):
        p = Player(gen_player_id())
        p.setup()
        players.append(p)
    return players


def main():
    n_players = get_uint_input("Please enter the number of players: ",
                               "Number of players must be an integer between 1 and 4.", 1, 4)
    players = setup_players(n_players)

    print(build_board(players, PROPERTIES))

    while True:
        start = input("Ready to start? ")
        if start == "Y":
            break

    while True:
        sleep(0.5)
        one_round(players)


if __name__ == "__main__":
    main()
