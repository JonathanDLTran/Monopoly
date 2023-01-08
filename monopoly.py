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

        self.owner = BANK
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
        self.turns_in_jail = 0

        self.rolls_history = []

        self.bankrupt = False

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

    def reduce_history(self):
        if len(self.rolls_history) >= 3:
            self.rolls_history = self.rolls_history[1:]

    def purge_history(self):
        self.rolls_history = []

    def triple_doubles(self):
        return len(self.rolls_history) >= 3 \
            and self.rolls_history[-1][0] == self.rolls_history[-1][1] \
            and self.rolls_history[-2][0] == self.rolls_history[-2][1] \
            and self.rolls_history[-3][0] == self.rolls_history[-3][1] \


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


def get_property(prop_id):
    for prop in PROPERTIES:
        if prop.id == prop_id:
            return prop
    raise RuntimeError(f"Cannot Find Property {prop}.")


def auction(players, prop_name):
    auction_values = []
    for p in players:
        player_amt = input(
            f"Enter an integer value greater than or equal to 10, for the auction of the property {prop_name}. Values not in this range will indicate no participation in the auction: ")
        player_amt = player_amt.strip().lower()
        if player_amt.isnumeric() and int(player_amt) >= 10 and 0 <= int(player_amt) <= p.cash:
            auction_values.append((p, int(player_amt)))
    sorted_values = sorted(
        auction_values, key=lambda pair: pair[1], reverse=True)
    if len(sorted_values) == 0:
        print("No One Voted in Auction; Bank Retains Property.")
        return (False, None)
    if len(sorted_values) > 1 and sorted_values[0][1] == sorted_values[1][1]:
        print("Tie in auction; Bank Retains Property.")
        return (False, None)
    return (True, sorted_values[0])


def one_round(players):

    for player in players:

        # check victory condition
        if not player.bankrupt:
            for p in players:
                if p != player and not p.bankrupt:
                    break
            else:
                print(
                    f"Victory for {player.name}! You are the last non-bankrupt player.")
                exit(0)

        # skip bankrupt players
        if player.bankrupt:
            continue

        # print current board state
        print(build_board(players, PROPERTIES))

        # roll dice, irregardless if player is in jail or not.
        die1 = randint(1, 6)
        die2 = randint(1, 6)

        # player in jail
        if player.in_jail:
            player.turns_in_jail += 1
            print(
                f"Either pay a ${JAIL_AMT} fee to leave jail, or roll dice and get doubles, or use a get out of jail card. ")
            jail_input = input(f"Do you want to pay ${JAIL_AMT}? ")

            can_leave_jail = False
            if jail_input == "yes" and player.cash >= JAIL_AMT:
                print("Ok, leaving jail.")
                player.cash -= JAIL_AMT
                can_leave_jail = True

            print(f"Rolling dice... {die1}, {die2}.")

            if die1 == die2:
                print("Rolled Doubles. Leaving Jail.")
                can_leave_jail = True

            if player.turns_in_jail == JAIL_MAX_TURNS:
                print(
                    f"Max Turns in Jail Reached. ${JAIL_AMT} charged to leave.")
                player.cash -= JAIL_AMT

            if not can_leave_jail:
                continue
            else:
                player.turns_in_jail = 0
                player.in_jail = False
                player.location = JUST_VISITING_ID
                player.purge_history()

        # only continue if player is not in jail, or leaves jail

        print(f"Rolling dice... {die1}, {die2}.")
        player.reduce_history()
        player.rolls_history.append((die1, die2))
        number_steps = die1 + die2

        old_location = player.location
        player.location = (player.location + number_steps) % NUM_PROPERTIES

        sleep(1)

        print(build_board(players, PROPERTIES))

        # Grab current location of player
        location = player.location
        location_key = extend_int_to_string(location)

        # check if enter JAIL conditions is true
        go_to_jail = False
        # if rolled doubles 3 times in a row, GO TO JAIL
        if player.triple_doubles():
            go_to_jail = True
            print("You rolled doubles 3 times in a row. You are sent to jail.")

        # land on GO TO JAIL
        if player.location == GO_TO_JAIL_ID:
            go_to_jail = True
            print("You landed on GO TO JAIL. You are sent to jail.")

        if go_to_jail:
            print("You lose this turn.")
            player.location = JAIL_ID
            player.in_jail = True

            sleep(2)

            print(build_board(players, PROPERTIES))

            sleep(2)

            continue

        # pass GO, get $200
        if player.location < old_location:
            print("You passed Go! You earn $200!")
            player.cash += GO_AMT

        # Land on Income Tax
        if player.location in [INCOME_TAX_ID, LUXURY_TAX_ID]:
            print(f"You have be accessed a ${TAX_AMT}.")
            player.cash -= TAX_AMT

        # property is owned by bank: either sell to current player, or attempt to auction to all players
        if location_key in CAN_BUILD:
            property_obj = get_property(location_key)
            if property_obj.owner == BANK:
                user_input = input("Do you want to buy this property?: ")
                if user_input == "yes":
                    property_obj.owner = player.id
                    property_obj.houses += 1
                    player.cash -= property_obj.deed_price
                    # handle bankruptcy
                else:
                    auction_result = auction(players, property_obj.name)
                    if auction_result[0]:
                        auction_player, player_amt = auction_result[1]
                        property_obj.owner = auction_player.id
                        property_obj.houses += 1
                        player.cash -= player_amt

        # user gives input
        while True:
            user_input = input("Please input a command: ")
            if user_input == "board":
                print(build_board(players, PROPERTIES))
            elif user_input == "user":
                print(player)
            elif user_input == "show properties":
                for prop in PROPERTIES:
                    if prop.owner == player.id:
                        print(prop)
            elif user_input == "finish":
                break

        # Final check of player's cash balance for bankruptcy at end of turn
        if player.cash < 0:
            print("You have become bankrupt at the end of the turn. Game over.")
            player.bankrupt = True


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
