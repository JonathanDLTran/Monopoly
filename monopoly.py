from copy import deepcopy
import emoji
from enum import Enum
from random import randint, shuffle
from time import sleep

from board import *
from constants import *
from utilities import *


class PropertyGroupColor(Enum):
    NO_COLOR = 0
    BROWN = 1
    CYAN = 2
    MAGENTA = 3
    ORANGE = 4
    RED = 5
    YELLOW = 6
    GREEN = 7
    BLUE = 8
    RAILROAD = 9
    UTILITY = 10

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


class Location(object):
    def __init__(self) -> None:
        self.id = -1
        self.name = ""
        self.color = PropertyGroupColor.NO_COLOR
        self.deed_price = 0
        self.house_price = 0
        self.rent = []
        self.mortgage = 0

        self.owner = BANK
        self.houses = 0

        self.mortgaged = False

    def __str__(self) -> str:
        return f"Property Name: {self.name} | Deed Price: {self.deed_price} | Mortgage Amount: {self.mortgage}"

    def __repr__(self) -> str:
        return self.__str__()


class Buildable(Location):
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

        self.mortgaged = False

    def __str__(self) -> str:
        return f"Property Name: {self.name} | Color Group: {self.color} | Deed Price: {self.deed_price} | House Price: {self.house_price} | Rent: {list(zip(['Deed Only', '1 House', '2 Houses','3 House', '4 Houses', 'Hotel'], self.rent))} | Mortgage Amount: {self.mortgage}"

    def __repr__(self) -> str:
        return self.__str__()


class Railroad(Location):
    def __init__(self, loc_id, name) -> None:
        super().__init__()
        self.id = loc_id
        self.name = name
        self.color = PropertyGroupColor.RAILROAD
        self.deed_price = 200
        self.house_price = 0
        self.rent = [25, 50, 100, 200]
        self.mortgage = 100

        self.owner = BANK
        self.houses = 0

        self.mortgaged = False


class Utility(Location):
    def __init__(self, loc_id, name) -> None:
        super().__init__()
        self.id = loc_id
        self.name = name
        self.color = PropertyGroupColor.UTILITY
        self.deed_price = 150
        self.house_price = 0
        self.rent = [4, 10]
        self.mortgage = 75

        self.owner = BANK
        self.houses = 0

        self.mortgaged = False


class Card(object):
    pass


class CommunityChest(Card):
    def __init__(self, name, action) -> None:
        super().__init__()
        self.name = name
        self.action = action

    def do_action(self, player, players, properties):
        return self.action(player, players, properties)


class Chance(Card):
    def __init__(self, name, action) -> None:
        super().__init__()
        self.name = name
        self.action = action

    def do_action(self, player, players, properties):
        return self.action(player, players, properties)


def advance_to_go(player, players, properties):
    # Do not bump up cash, as that will be handled later
    player.location = GO_ID

    print("Moving to Go")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def bank_error(player, players, properties):
    player.cash += 200
    # return true to indicate card should reenter deck
    return True


def doctors_fees(player, players, properties):
    player.cash -= 50
    if player.cash < 0:
        player.bankruptor = BANK
    # return true to indicate card should reenter deck
    return True


def sell_stock(player, players, properties):
    player.cash += 50
    # return true to indicate card should reenter deck
    return True


def cc_get_out_of_jail(player, players, properties):
    player.get_out_of_jail_cards += 1
    player.cc_out_of_jail_cards = True
    # return false to indicate card should NOT reenter deck
    return False


def go_to_jail(player, players, properties):
    player.location = JAIL_ID

    print("Moving to Jail")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def grand_opera(player, players, properties):
    for p in players:
        if p != player:
            player.cash += 50
            p.cash -= 50
            if p.cash < 0:
                p.bankruptor = player.id

    # return true to indicate card should reenter deck
    return True


def holiday_fund(player, players, properties):
    player.cash += 100

    # return true to indicate card should reenter deck
    return True


def tax_refund(player, players, properties):
    player.cash += 20

    # return true to indicate card should reenter deck
    return True


def birthday(player, players, properties):
    for p in players:
        if p != player:
            player.cash += 10
            p.cash -= 10
            if p.cash < 0:
                p.bankruptor = player.id

    # return true to indicate card should reenter deck
    return True


def life_insurance(player, players, properties):
    player.cash += 100

    # return true to indicate card should reenter deck
    return True


def hospital_fees(player, players, properties):
    player.cash -= 50
    if player.cash < 0:
        player.bankruptor = BANK

    # return true to indicate card should reenter deck
    return True


def school_fees(player, players, properties):
    player.cash -= 50
    if player.cash < 0:
        player.bankruptor = BANK

    # return true to indicate card should reenter deck
    return True


def consultancy_fees(player, players, properties):
    player.cash += 25

    # return true to indicate card should reenter deck
    return True


def street_repairs(player, players, properties):
    repair_fee = 0
    for prop in properties:
        if prop.owner == player.id:
            n_houses = prop.houses
            if 0 < n_houses <= 4:
                repair_fee += 40
            elif n_houses == 5:
                repair_fee += 115
    print(f"You owe ${repair_fee} in fees.")
    player.cash -= repair_fee
    if player.cash < 0:
        player.bankruptor = BANK

    # return true to indicate card should reenter deck
    return True


def second_prize(player, players, properties):
    player.cash += 10

    # return true to indicate card should reenter deck
    return True


def inherit(player, players, properties):
    player.cash += 100

    # return true to indicate card should reenter deck
    return True


COMMUNITY_GET_OF_JAIL_CARD = CommunityChest(
    "Get out of jail free – This card may be kept until needed or sold/traded. ", cc_get_out_of_jail)


COMMUNITY_DECK = [
    CommunityChest("Advance To Go: Collect $200", advance_to_go),
    CommunityChest("Bank Error In Your Favor: Collect $200", bank_error),
    CommunityChest("Doctors Fees: Pay $50", doctors_fees),
    CommunityChest("From sale of stock you get $50", sell_stock),
    COMMUNITY_GET_OF_JAIL_CARD,
    CommunityChest(
        "Go to jail. Go directly to jail. Do not pass Go, Do not collect $200. s", go_to_jail),
    CommunityChest(
        "Grand Opera Night. Collect $50 from every player for opening night seats.", grand_opera),
    CommunityChest("Holiday Fund Matures: Collect $100", holiday_fund),
    CommunityChest("Income tax refund: Collect $20", tax_refund),
    CommunityChest(
        "It is your birthday. Collect $10 from every player. ", birthday),
    CommunityChest("Life insurance matures – Collect $100.", life_insurance),
    CommunityChest("Hospital Fees. Pay $50.", hospital_fees),
    CommunityChest("School fees. Pay $50.", school_fees),
    CommunityChest("Receive $25 consultancy fee. ", consultancy_fees),
    CommunityChest(
        "You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.", street_repairs),
    CommunityChest(
        "You have won second prize in a beauty contest. Collect $10.", second_prize),
    CommunityChest(
        "You inherit $100.", inherit),
]
shuffle(COMMUNITY_DECK)

COMMUNITY_TRASH_DECK = []


# ------------


def illinois_ave(player, players, properties):
    player.location = ILLINOIS_ID

    print("Moving to Illinois Avenue")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def st_charles_place(player, players, properties):
    player.location = ST_CHARLES_PLACE_ID

    print("Moving to St. Charles Place")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def nearest_utility(player, players, properties):
    location = player.location
    differences = []
    for i, u in enumerate(UTILITIES_LOCATIONS):
        diff = min(abs(location - u), abs(location + NUM_PROPERTIES - u))
        differences.append((i, diff))
    differences = sorted(differences, key=lambda pair: pair[1])

    nearest = UTILITIES_LOCATIONS[differences[0][0]]
    player.location = nearest
    player.pay_ten_times = True

    # return true to indicate card should reenter deck
    return True


def nearest_railroad(player, players, properties):
    location = player.location
    differences = []
    for i, u in enumerate(RAILROAD_LOCATIONS):
        diff = min(abs(location - u), abs(location + NUM_PROPERTIES - u))
        differences.append((i, diff))
    differences = sorted(differences, key=lambda pair: pair[1])

    nearest = RAILROAD_LOCATIONS[differences[0][0]]
    player.location = nearest
    player.pay_double_rent = True

    # return true to indicate card should reenter deck
    return True


def dividend(player, players, properties):
    player.cash += 50

    # return true to indicate card should reenter deck
    return True


def chance_get_out_of_jail(player, players, properties):
    player.get_out_of_jail_cards += 1
    player.chance_out_of_jail_cards = True
    # return false to indicate card should NOT reenter deck
    return False


def go_back_3_spaces(player, players, properties):
    player.location = (player.location + NUM_PROPERTIES - 3) % NUM_PROPERTIES

    print("Moving back 3 spaces")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def general_repairs(player, players, properties):
    repair_fee = 0
    for prop in properties:
        if prop.owner == player.id:
            n_houses = prop.houses
            if 0 < n_houses <= 4:
                repair_fee += 25
            elif n_houses == 5:
                repair_fee += 100
    print(f"You owe ${repair_fee} in fees.")
    player.cash -= repair_fee
    if player.cash < 0:
        player.bankruptor = BANK

    # return true to indicate card should reenter deck
    return True


def reading_railroad(player, players, properties):
    player.location = READING_RAILROAD_ID

    print("Moving to Reading Railroad")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def boardwalk(player, players, properties):
    player.location = BOARDWALK_ID

    print("Moving to Boardwalk")

    sleep(1)

    print(build_board(players, properties))

    # return true to indicate card should reenter deck
    return True


def chairman(player, players, properties):
    for p in players:
        if p != player:
            p.cash += 50
            player.cash -= 50
            if player.cash < 0:
                player.bankruptor = p.id

    # return true to indicate card should reenter deck
    return True


def matures(player, players, properties):
    player.cash += 150

    # return true to indicate card should reenter deck
    return True


CHANCE_GET_OF_JAIL_CARD = Chance(
    "Get out of jail free – This card may be kept until needed or sold/traded. ", chance_get_out_of_jail)

CHANCE_DECK = [
    Chance("Advance to Go. (Collect $200)", advance_to_go),
    Chance("Advance to Illinois Ave. If you pass Go, collect $200.", illinois_ave),
    Chance("Advance to St. Charles Place.  If you pass Go, collect $200.",
           st_charles_place),
    Chance("Advance token to the nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 (ten) times the amount thrown.", nearest_utility),
    Chance("Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rent to which they are otherwise entitled. If Railroad is unowned, you may buy it from the Bank.", nearest_railroad),
    Chance("Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rent to which they are otherwise entitled. If Railroad is unowned, you may buy it from the Bank.", nearest_railroad),
    Chance("Bank pays you dividend of $50. ", dividend),
    CHANCE_GET_OF_JAIL_CARD,
    Chance("Go Back Three (3) Spaces. ", go_back_3_spaces),
    Chance("Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.", go_to_jail),
    Chance("Make general repairs on all your property: For each house pay $25, For each hotel pay $100.", general_repairs),
    Chance("Take a trip to Reading Railroad. If you pass Go, collect $200. ",
           reading_railroad),
    Chance("Take a walk on the Boardwalk. Advance token to Boardwalk. ", boardwalk),
    Chance("You have been elected Chairman of the Board. Pay each player $50.", chairman),
    Chance("Your building and loan matures. Receive $150. ", matures),
]
shuffle(CHANCE_DECK)

CHANCE_TRASH_DECK = []


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
        self.bankruptor = None

        self.chance_get_out_of_jail = False
        self.cc_get_out_of_jail = False
        self.get_out_of_jail_cards = 0

        self.pay_double_rent = False
        self.pay_ten_times = False

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
            and self.rolls_history[-3][0] == self.rolls_history[-3][1]

    def __str__(self) -> str:
        return f"{self.name} | {self.__symbol} | ${self.cash} | Get Out of Jail Cards: {self.get_out_of_jail_cards}"

    def __repr__(self) -> str:
        return self.__str__()


BUILADBLES = [
    Buildable("01", MEDITERRANEAN_AVENUE, PropertyGroupColor.BROWN,
              60, 50, [2, 10, 30, 90, 160, 250], 30),
    Buildable("03", BALTIC_AVENUE, PropertyGroupColor.BROWN,
              60, 50, [4, 20, 60, 180, 320, 450], 30),
    Buildable("06", ORIENTAL_AVENUE, PropertyGroupColor.CYAN,
              100, 50, [6, 30, 90, 270, 400, 550], 50),
    Buildable("08", VERMONT_AVENUE, PropertyGroupColor.CYAN,
              100, 50, [6, 30, 90, 270, 400, 550], 50),
    Buildable("09", CONNECTICUT_AVENUE, PropertyGroupColor.CYAN,
              120, 50, [8, 40, 100, 300, 450, 550], 60),
    Buildable("11", ST_CHARLES_PLACE, PropertyGroupColor.MAGENTA,
              140, 100, [10, 50, 150, 450, 625, 750], 70),
    Buildable("13", STATES_AVENUE, PropertyGroupColor.MAGENTA,
              140, 100, [10, 50, 150, 450, 625, 750], 70),
    Buildable("14", VIRGINIA_AVENUE, PropertyGroupColor.MAGENTA,
              160, 100, [12, 60, 180, 500, 700, 900], 80),
    Buildable("16", ST_JAMES_PLACE, PropertyGroupColor.ORANGE,
              180, 100, [14, 70, 200, 550, 750, 950], 90),
    Buildable("18", TENNESSEE_AVENUE, PropertyGroupColor.ORANGE,
              180, 100, [14, 70, 200, 550, 750, 950], 90),
    Buildable("19", NEW_YORK_AVENUE, PropertyGroupColor.ORANGE,
              200, 100, [16, 80, 220, 600, 800, 1000], 100),
    Buildable("21", KENTUCKY_AVENUE, PropertyGroupColor.RED,
              220, 150, [18, 90, 250, 700, 875, 1050], 110),
    Buildable("23", INDIANA_AVENUE, PropertyGroupColor.RED,
              220, 150, [18, 90, 250, 700, 875, 1050], 110),
    Buildable("24", ILLINOIS_AVENUE, PropertyGroupColor.RED,
              240, 150, [20, 100, 300, 750, 925, 1100], 120),
    Buildable("26", ATLANTIC_AVENUE, PropertyGroupColor.YELLOW,
              260, 150, [22, 110, 330, 800, 975, 1150], 130),
    Buildable("27", VENTNOR_AVENUE, PropertyGroupColor.YELLOW,
              260, 150, [22, 110, 330, 800, 975, 1150], 130),
    Buildable("29", MARVIN_GARDENS, PropertyGroupColor.YELLOW,
              280, 150, [24, 120, 360, 850, 1025, 1200], 140),
    Buildable("31", PACIFIC_AVENUE, PropertyGroupColor.GREEN,
              300, 200, [26, 130, 390, 900, 1100, 1275], 150),
    Buildable("32", NORTH_CAROLINA_AVENUE, PropertyGroupColor.GREEN,
              300, 200, [26, 130, 390, 900, 1100, 1275], 150),
    Buildable("34", PENNSYLVANIA_AVENUE, PropertyGroupColor.GREEN,
              320, 200, [28, 150, 450, 1000, 1200, 1400], 160),
    Buildable("37", PARK_PLACE, PropertyGroupColor.BLUE,
              350, 200, [35, 175, 500, 1100, 1300, 1500], 175),
    Buildable("39", BOARDWALK, PropertyGroupColor.BLUE,
              400, 200, [50, 200, 600, 1400, 1700, 2000], 200), ]

RAILROADS = [
    Railroad("05", READING_RAILROAD),
    Railroad("15", PENNSYLVANIA_RAILROAD),
    Railroad("25", B_AND_O_RAILROAD),
    Railroad("35", SHORT_LINE),
]

UTILITIES = [
    Utility("12", ELECTRIC_COMPANY),
    Utility("28", WATER_WORKS),
]

PROPERTIES = BUILADBLES + RAILROADS + UTILITIES


def get_property(prop_id):
    for prop in PROPERTIES:
        if prop.id == prop_id:
            return prop
    raise RuntimeError(f"Cannot Find Property {prop}.")


def auction(players, prop_name):
    auction_values = []
    for p in players:
        if not p.bankrupt:
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


def is_on_another_player_property(player, players, properties):
    location = player.location
    location_key = extend_int_to_string(location)
    if location_key not in CAN_OWN:
        return (False, None, None)
    prop = get_property(location_key)
    if prop.owner == player.id or prop.owner == BANK or prop.mortgaged:
        return (False, None, None)
    other_player_id = prop.owner
    other_player = None
    for p in players:
        if p.id == other_player_id:
            other_player = p
            break
    return (True, other_player, prop)


def has_monopoly(player, prop, properties):
    prop_color = prop.color
    property_group = [p for p in properties if p.color == prop_color]
    for prop in property_group:
        if prop.owner != player.id:
            return False
    return True


def trade(player, players, properties):
    trade_player = input(
        "Who do you want to trade with? Input the player's name: ")
    if trade_player == player.name:
        print("You cannot trade with yourself.")
        return False
    other_player = None
    for p in players:
        if p != player and p.name == trade_player and not p.bankrupt:
            other_player = p
            break
    else:
        print("You must trade with an non-bankrupt player in the game.")
        return False
    assert other_player != None

    your_trade = input(
        "What are you trading: 'money' / 'property' / 'Jail Card'? ")
    their_trade = input(
        "What are you trading for: 'money' / 'property' / 'Jail Card'? ")
    if your_trade == their_trade == "money":
        print("You cannot trade money for money")
        return False
    if your_trade == "Jail Card" and player.get_out_of_jail_cards == 0:
        print("You must have a get out of jail card to trade it.")
        return False
    if their_trade == "Jail Card" and other_player.get_out_of_jail_cards == 0:
        print("Your trade partner must have a get out of jail card to trade it.")
        return False

    your_money_amt = None
    their_money_amt = None
    your_property = None
    their_property = None
    your_jail_card = your_trade == "Jail Card"
    their_jail_card = their_trade == "Jail Card"
    if your_trade == "money":
        your_money_amt = input(
            "Input an amount of money you are giving for the trade: ")
        if not your_money_amt.isnumeric() or int(your_money_amt) <= 0:
            print("Money amount must be a non-zero positive amount and an integer.")
            return False
        if int(your_money_amt) > player.cash:
            print("Money amount must less than the cash you have currently.")
            return False
    if their_trade == "money":
        their_money_amt = input(
            "Input an amount of money you trade partner will give for the trade: ")
        if not their_money_amt.isnumeric() or int(their_money_amt) <= 0:
            print("Money amount must be a non-zero positive amount and an integer.")
            return False
        if int(their_money_amt) > other_player.cash:
            print("Money amount must less than the cash your partner has have currently.")
            return False

    if your_trade == "property":
        your_property = input(
            "Please input your property number you are trading: ")
        if not your_property.isnumeric() or (extend_int_to_string(int(your_property)) not in CAN_OWN):
            print("Property Must be a numeric value corresponding to a buyable property.")
            return False
        location_key = extend_int_to_string(int(your_property))
        prop = get_property(location_key)
        if prop.owner != player.id:
            print("You must own the property to trade it.")
            return False
        if prop.houses > 0:
            print("You can only trade a property with no houses or hotels.")
            return False
        your_property = prop
    if their_trade == "property":
        their_property = input(
            "Please input the property number your trade partner is trading: ")
        if not their_property.isnumeric() or (extend_int_to_string(int(their_property)) not in CAN_OWN):
            print("Property Must be a numeric value corresponding to a buyable property.")
            return False
        location_key = extend_int_to_string(int(their_property))
        prop = get_property(location_key)
        if prop.owner != other_player.id:
            print("Your trade partner must own the property to trade it.")
            return False
        if prop.houses > 0:
            print(
                "Your trade partner can only trade a property with no houses or hotels.")
            return False
        their_property = prop

    agreement_to_trade = input(
        "Do both parties agree to trade? 'yes' to agree: ")
    if agreement_to_trade != 'yes':
        print("Agreement not reached. Trade cancelled.")
        return False

    print("Trade will happen.")
    if your_money_amt != None:
        player.cash -= int(your_money_amt)
        other_player.cash += int(your_money_amt)
    if their_money_amt != None:
        player.cash += int(their_money_amt)
        other_player.cash -= int(their_money_amt)
    if your_property != None:
        your_property.owner = other_player.id
    if their_property != None:
        their_property.owner = player.id

    if your_jail_card:
        player.get_out_of_jail_cards -= 1
        other_player.get_out_of_jail_cards += 1
        if player.chance_get_out_of_jail:
            player.chance_get_out_of_jail = False
            other_player.chance_get_out_of_jail = True
        else:
            player.cc_get_out_of_jail = False
            other_player.cc_get_out_of_jail = True
    if their_jail_card:
        other_player.get_out_of_jail_cards -= 1
        player.get_out_of_jail_cards += 1
        if other_player.chance_get_out_of_jail:
            other_player.chance_get_out_of_jail = False
            player.chance_get_out_of_jail = True
        else:
            other_player.cc_get_out_of_jail = False
            player.cc_get_out_of_jail = True

    return True


def handle_bankruptcy(player, players, properties):
    assert player.bankrupt
    assert player.bankruptor != None
    if player.bankruptor == BANK:
        print(
            f"Bank receiving all of {player.name}'s properties and get out of jail free cards.")
        for p in properties:
            if p.owner == player.id:
                # return all houses and hotels
                p.houses = 0
                result, auction_data = auction(players, p.name)
                if result:
                    # auction succeedd
                    (auction_winner, auction_amt) = auction_data
                    auction_winner.cash -= auction_amt
                    p.owner = auction_winner.id
                else:
                    # auction failed
                    p.owner = BANK

        if player.chance_get_out_of_jail:
            player.chance_get_out_of_jail = False
            CHANCE_TRASH_DECK.append(CHANCE_GET_OF_JAIL_CARD)
        if player.cc_get_out_of_jail:
            player.cc_get_out_of_jail = False
            COMMUNITY_TRASH_DECK.append(COMMUNITY_GET_OF_JAIL_CARD)
        player.get_out_of_jail_cards = 0
    else:
        print(
            f"Player {player.bankruptor.name} receiving all of {player.name}'s properties and get out of jail free cards.")
        for p in properties:
            if p.owner == player.id:
                p.owner = player.bankruptor.id
        if player.chance_get_out_of_jail:
            player.bankruptor.chance_get_out_of_jail = True
            player.chance_get_out_of_jail = False
        if player.cc_get_out_of_jail:
            player.bankruptor.cc_get_out_of_jail = True
            player.cc_get_out_of_jail = False
        player.bankruptor.get_out_of_jail_cards += player.get_out_of_jail_cards
        player.get_out_of_jail_cards = 0


def one_round(players):
    global COMMUNITY_DECK
    global COMMUNITY_TRASH_DECK
    global CHANCE_DECK
    global CHANCE_TRASH_DECK

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
        die1 = 3  # randint(1, 6)
        die2 = 4  # randint(1, 6)

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

            if not can_leave_jail and player.get_out_of_jail_cards > 0:
                resp = input("Would you like to use get out of jail card?")
                if resp == "yes":
                    player.get_out_of_jail_cards -= 1
                    can_leave_jail = True
                    if player.chance_get_out_of_jail:
                        player.chance_get_out_of_jail = False
                        CHANCE_TRASH_DECK.append(CHANCE_GET_OF_JAIL_CARD)
                    else:
                        player.cc_get_out_of_jail = False
                        COMMUNITY_TRASH_DECK.append(COMMUNITY_GET_OF_JAIL_CARD)

            if not can_leave_jail:
                print(f"Rolling dice... {die1}, {die2}.")

            if not can_leave_jail and die1 == die2:
                print("Rolled Doubles. Leaving Jail.")
                can_leave_jail = True

            if not can_leave_jail and player.turns_in_jail == JAIL_MAX_TURNS:
                print(
                    f"Max Turns in Jail Reached. ${JAIL_AMT} charged to leave.")
                player.cash -= JAIL_AMT
                if player.cash < 0:
                    player.bankruptor = BANK

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

        # chance card
        if player.location in CHANCE_LOCATIONS:
            if CHANCE_DECK == []:
                CHANCE_DECK = deepcopy(CHANCE_TRASH_DECK)
                shuffle(CHANCE_DECK)
                CHANCE_TRASH_DECK = []

            assert CHANCE_DECK != []
            chance_card = CHANCE_DECK.pop()
            print(chance_card.name)
            action_result = chance_card.do_action(
                player, players, PROPERTIES)
            if action_result:
                CHANCE_TRASH_DECK.append(chance_card)

        # community chest card
        if player.location in COMMUNITY_CHEST_LOCATIONS:
            if COMMUNITY_DECK == []:
                COMMUNITY_DECK = deepcopy(COMMUNITY_TRASH_DECK)
                shuffle(COMMUNITY_DECK)
                COMMUNITY_TRASH_DECK = []

            assert COMMUNITY_DECK != []
            community_card = COMMUNITY_DECK.pop()
            print(community_card.name)
            action_result = community_card.do_action(
                player, players, PROPERTIES)
            if action_result:
                COMMUNITY_TRASH_DECK.append(community_card)

        # check if enter JAIL conditions is true
        go_to_jail = False

        # for chance or community chest go to jail
        if player.location == JAIL_ID:
            go_to_jail = True

        # if rolled doubles 3 times in a row, GO TO JAIL
        if player.triple_doubles():
            go_to_jail = True
            print("You rolled doubles 3 times in a row. You are sent to jail.")

        # land on GO TO JAIL
        if player.location == GO_TO_JAIL_ID:
            go_to_jail = True
            print("You landed on GO TO JAIL. You are sent to jail.")

        if go_to_jail:
            resp = input("Would you like to use get out of jail card?")
            if resp == "yes":
                go_to_jail = False
                player.location = JUST_VISITING_ID
                player.get_out_of_jail_cards -= 1
                can_leave_jail = True
                if player.chance_get_out_of_jail:
                    player.chance_get_out_of_jail = False
                    CHANCE_TRASH_DECK.append(CHANCE_GET_OF_JAIL_CARD)
                else:
                    player.cc_get_out_of_jail = False
                    COMMUNITY_TRASH_DECK.append(COMMUNITY_GET_OF_JAIL_CARD)

        if go_to_jail:
            print("You lose this turn.")
            player.location = JAIL_ID
            player.in_jail = True

            sleep(2)

            print(build_board(players, PROPERTIES))

            sleep(2)

            continue

        # Grab updated location of player, after chance or community chest or go to jail movements
        location = player.location
        location_key = extend_int_to_string(location)

        # pass GO, get $200
        if player.location <= old_location:
            print(f"You passed Go! You earn ${GO_AMT}!")
            player.cash += GO_AMT

        # Land on Income Tax
        if player.location in [INCOME_TAX_ID, LUXURY_TAX_ID]:
            print(f"You have been accessed a ${TAX_AMT} tax.")
            player.cash -= TAX_AMT
            if player.cash < 0:
                player.bankruptor = BANK

        # Land on another player's property
        if is_on_another_player_property(player, players, PROPERTIES)[0]:
            _, other_player, other_player_prop = is_on_another_player_property(
                player, players, PROPERTIES)
            rent = 0
            if isinstance(other_player_prop, Buildable):
                other_player_houses = other_player_prop.houses
                rent = other_player_prop.rent[other_player_houses]
                # if has monopoly and unimproved, double rent
                if has_monopoly(other_player, other_player_prop, PROPERTIES) and other_player_houses == 0:
                    rent *= 2
            elif isinstance(other_player_prop, Railroad):
                num_rrs_owned = len(
                    [p for p in PROPERTIES if isinstance(p, Railroad) and p.owner == other_player.id])
                if num_rrs_owned == 1:
                    rent = (die1 + die2) * ONE_RAILROAD_RENT
                elif num_rrs_owned == 2:
                    rent = (die1 + die2) * TWO_RAILROAD_RENT
                elif num_rrs_owned == 3:
                    rent = (die1 + die2) * THREE_RAILROAD_RENT
                elif num_rrs_owned == 4:
                    rent = (die1 + die2) * FOUR_RAILROAD_RENT
                else:
                    raise RuntimeError(f"Railroads owned must be less than 4.")
            elif isinstance(other_group_prop, Utility):
                num_utils_owned = len(
                    [p for p in PROPERTIES if isinstance(p, Utility) and p.owner == other_player.id])
                if num_utils_owned == 1:
                    rent = (die1 + die2) * ONE_UTILITIES_MULTIPLIER
                elif num_utils_owned == 2:
                    rent = (die1 + die2) * TWO_UTILITIES_MULTIPLIER
                else:
                    raise RuntimeError(f"Utilities owned must be less than 2.")
            else:
                raise RuntimeError(
                    f"Property object {other_player_prop} type {type(other_player_prop)} not recognized. ")

            assert rent != None and type(rent) == int and rent > 0
            if player.pay_double_rent:
                print("You have to pay double rent per the chance card.")
                rent * - 2
                player.pay_double_rent = False
            elif player.pay_ten_times:
                print(
                    "You have to pay ten times the sum of this dice roll per the chance card.")
                roll1 = randint(1, 6)
                roll2 = randint(1, 6)
                print(
                    f"Rolled {roll1}, {roll2}. You owe {10 * (roll1 + roll2)}.")
                rent = 10 * (roll1 + roll2)
                player.pay_ten_times = False

            print(f"You owe {other_player.name} ${rent} in rent.")
            other_player.cash += rent
            player.cash -= rent
            if player.cash < 0:
                player.bankruptor = other_player.id

        # property is owned by bank: either sell to current player, or attempt to auction to all players
        if location_key in CAN_OWN:
            property_obj = get_property(location_key)
            if property_obj.owner == BANK:
                user_input = input("Do you want to buy this property?: ")
                if user_input == "yes" and player.cash >= property_obj.deed_price:
                    property_obj.owner = player.id
                    player.cash -= property_obj.deed_price
                else:
                    auction_result = auction(players, property_obj.name)
                    if auction_result[0]:
                        auction_player, player_amt = auction_result[1]
                        property_obj.owner = auction_player.id
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
            elif user_input == "quit":
                print("Exiting game...")
                exit(0)
            elif user_input == "trade":
                trade_result = trade(player, players, PROPERTIES)
                if not trade_result:
                    print("Trade did not go through. Try again. ")
            elif is_string_plus_number("mortgage", user_input)[0]:
                _, location = is_string_plus_number("mortgage", user_input)
                if location < 0 or location >= NUM_PROPERTIES:
                    continue
                location_key = extend_int_to_string(location)
                if location_key not in CAN_OWN:
                    continue
                prop = get_property(location_key)
                if prop.owner != player.id:
                    print(f"You do not own property {prop}.")
                    continue
                if prop.houses > 0:
                    print("Can only mortgage when no houses or hotels on property.")
                    continue
                print(
                    f"Mortgaging property {prop}. Adding ${prop.mortgage} value.")
                prop.mortgaged = True
                player.cash += prop.mortgage
            elif is_string_plus_number("unmortgage", user_input)[0]:
                _, location = is_string_plus_number("unmortgage", user_input)
                if location < 0 or location >= NUM_PROPERTIES:
                    continue
                location_key = extend_int_to_string(location)
                if location_key not in CAN_OWN:
                    continue
                prop = get_property(location_key)
                if prop.owner != player.id:
                    print(f"You do not own property {prop}.")
                    continue
                if player.cash < int(prop.mortgage * 1.1):
                    print("Can only unmortgage when you have enough to pay back bank.")
                    continue
                print(
                    f"Unmortgaging property {prop}. Subtracting 1.1 * ${prop.mortgage} value.")
                prop.mortgaged = False
                player.cash -= int(1.1 * prop.mortgage)
            elif is_string_plus_number("sell", user_input)[0]:
                _, location = is_string_plus_number("sell", user_input)
                if location < 0 or location >= NUM_PROPERTIES:
                    continue
                location_key = extend_int_to_string(location)
                if location_key not in CAN_BUILD:
                    continue
                prop = get_property(location_key)
                if prop.owner != player.id:
                    print(f"You do not own property {prop}.")
                    continue
                if prop.houses == 0:
                    print("Can only sell when there is at least 1 house or hotel.")
                    continue
                # check balancing in property group
                group = [p for p in PROPERTIES if p.color ==
                         prop.color and p != prop]
                balanced = True
                for other_group_prop in group:
                    if other_group_prop.houses - 1 > prop.houses - 1:
                        balanced = False
                if not balanced:
                    print("You must sell houses or hotels in a balanced manner.")
                    continue
                print(
                    f"Selling property {prop}. Adding 0.5 * ${prop.house_price} value.")
                player.cash += int(0.5 * prop.house_price)
                prop.houses -= 1
            elif is_string_plus_number("upgrade", user_input)[0]:
                _, location = is_string_plus_number("upgrade", user_input)
                if location < 0 or location >= NUM_PROPERTIES:
                    continue
                location_key = extend_int_to_string(location)
                if location_key not in CAN_BUILD:
                    continue
                prop = get_property(location_key)
                if prop.owner != player.id:
                    print(f"You do not own property {prop}.")
                    continue
                # check all other properties in group owned by same player AND have at either the same number of houses or 1 more house
                group = [p for p in PROPERTIES if p.color ==
                         prop.color and p != prop]
                owned_by_same_player = True
                num_houses = []
                for p in group:
                    if p.owner != player.id:
                        owned_by_same_player = False
                        break
                    num_houses.append(p.houses)
                if not owned_by_same_player:
                    print(
                        "There is a property in the same color group not owned by you. You cannot build a house without a monopoly.")
                    continue
                unbalanced_houses = False
                for num_house in num_houses:
                    if (prop.houses + 1 > num_house + 1):
                        unbalanced_houses = True
                if unbalanced_houses:
                    print(
                        "Properties must be built in a balanced manner. You cannot build the house.")
                    continue
                if player.cash < prop.house_price:
                    print("You do not have enough money to upgrade property. ")
                    continue
                if prop.houses < MAX_HOUSES - 1:
                    prop.houses += 1
                    player.cash -= prop.house_price
                    print("House was built.")
                elif prop.houses < MAX_HOUSES:
                    prop.houses += 1
                    player.cash -= prop.house_price
                    print("Hotel was built.")
                else:
                    print(f"You can have at most 4 houses or a hotel on a property.")
            # Commands for Testing Purposes
            elif user_input == "+1":
                player.location = (player.location + 1) % NUM_PROPERTIES
            elif user_input == "-1":
                player.location = (player.location +
                                   NUM_PROPERTIES - 1) % NUM_PROPERTIES
            elif user_input == "buy":
                location = player.location
                location_key = extend_int_to_string(location)
                if location_key in CAN_OWN:
                    prop = get_property(location_key)
                    prop.owner = player.id
            elif user_input == "community":
                if COMMUNITY_DECK == []:
                    COMMUNITY_DECK = deepcopy(COMMUNITY_TRASH_DECK)
                    shuffle(COMMUNITY_DECK)
                    COMMUNITY_TRASH_DECK = []

                assert COMMUNITY_DECK != []
                community_card = COMMUNITY_DECK.pop()
                print(community_card.name)
                action_result = community_card.do_action(
                    player, players, PROPERTIES)
                if action_result:
                    COMMUNITY_TRASH_DECK.append(community_card)
            elif user_input == "chance":
                if CHANCE_DECK == []:
                    CHANCE_DECK = deepcopy(CHANCE_TRASH_DECK)
                    shuffle(CHANCE_DECK)
                    CHANCE_TRASH_DECK = []

                assert CHANCE_DECK != []
                chance_card = CHANCE_DECK.pop()
                print(chance_card.name)
                action_result = chance_card.do_action(
                    player, players, PROPERTIES)
                if action_result:
                    CHANCE_TRASH_DECK.append(chance_card)
            elif user_input == "bankrupt":
                player.cash = -1000
                player.bankruptor = BANK

        # Final check of player's cash balance for bankruptcy at end of turn
        if player.cash < 0:
            print("You have become bankrupt at the end of the turn. Game over.")
            player.bankrupt = True
            handle_bankruptcy(player, players, PROPERTIES)


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
