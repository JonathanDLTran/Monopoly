from constants import *
from utilities import extend_int_to_string


def build_board(players):

    # create player symbol dictionary
    p = dict()
    for i in range(41):
        key = extend_int_to_string(i)
        p[key] = PLAYER_SYMBOL_STRING_LENGTH * SPACE

    # assign locations for each player appropriately
    for i, player in enumerate(players):
        location = player.location
        key = extend_int_to_string(location)
        current_symbol_string = p[key]
        current_symbol_list = list(current_symbol_string)
        non_space_symbols = []
        for c in current_symbol_list:
            if c != SPACE:
                non_space_symbols.append(c)
        non_space_symbols.append(str(player.symbol))
        len_non_space_symbols = 2 * len(non_space_symbols)
        non_space_symbols += SPACE * \
            (PLAYER_SYMBOL_STRING_LENGTH - len_non_space_symbols)
        p[key] = "".join(non_space_symbols)

    # create player properties dictionary
    h = dict()
    for i in range(41):
        key = extend_int_to_string(i)
        h[key] = PLAYER_SYMBOL_STRING_LENGTH * SPACE

    for player in players:
        for prop in player.properties:
            property_name = prop.name
            property_index = PROPERTY_TO_INDEX_MAP[property_name]
            h[property_index] = HOUSE + 7 * SPACE

    board = f"""
    ┌───────────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬───────────────┐
    │               │         │         │         │         │         │         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │ Just Visiting │   St.   │Electric │ States  │Virginia │Pennsyl- │St. James│Community│Tennessee│New York │    Free       │
    │               │ Charles │Company  │ Avenue  │ Avenue  │ vania   │ Place   │  Chest  │ Avenue  │ Avenue  │   Parking     │
    │               │  Place  │         │         │         │ Railroad│         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │{h["10"]}      │{h["11"]}│{h["12"]}│{h["13"]}│{h["14"]}│{h["15"]}│{h["16"]}│{h["17"]}│{h["18"]}│{h["19"]}│{h["20"]}      │
    │{p["10"]}      │{p["11"]}│{p["12"]}│{p["13"]}│{p["14"]}│{p["15"]}│{p["16"]}│{p["17"]}│{p["18"]}│{p["19"]}│{p["20"]}      │
    ├───────────────┼─────────┼─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┼───────────────┤
    │               │         │                                                                               │               │
    │  Connecticut  │  Jail   │                                                                               │Kentucky Avenue│
    │    Avenue     │         │                                                                               │               │
    │{h["09"]}      │{h["40"]}│                                                                               │{h["21"]}      │
    │{p["09"]}      │{p["40"]}│                                                                               │{p["21"]}      │
    ├───────────────┼─────────┘                                                                               ├───────────────┤
    │               │                                                                                         │               │
    │Vermont Avenue │                                                                                         │    Chance     │
    │               │                                                                                         │               │
    │{h["08"]}      │                                                                                         │{h["22"]}      │
    │{p["08"]}      │                                                                                         │{p["22"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │    Chance     │                                                                                         │Indiana Avenue │
    │               │                                                                                         │               │
    │{h["07"]}      │                                                                                         │{h["23"]}      │
    │{p["07"]}      │                                                                                         │{p["23"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │Oriental Avenue│                                                                                         │Illinois Avenue│
    │               │                                                                                         │               │
    │{h["06"]}      │                                                                                         │{h["24"]}      │
    │{p["06"]}      │                                                                                         │{p["24"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │   Reading     │                                                                                         │ B&O Railroad  │
    │   Railroad    │                                                                                         │               │
    │{h["05"]}      │                                                                                         │{h["25"]}      │
    │{p["05"]}      │                                                                                         │{p["25"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │  Income Tax   │                                                                                         │Atlantic Avenue│
    │               │                                                                                         │               │
    │{h["04"]}      │                                                                                         │{h["26"]}      │
    │{p["04"]}      │                                                                                         │{p["26"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │ Baltic Avenue │                                                                                         │Ventnor Avenue │
    │               │                                                                                         │               │
    │{h["03"]}      │                                                                                         │{h["27"]}      │
    │{p["03"]}      │                                                                                         │{p["27"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    |Community Chest│                                                                                         │  Water Works  │
    │               │                                                                                         │               │
    │{h["02"]}      │                                                                                         │{h["28"]}      │
    │{p["02"]}      │                                                                                         │{p["28"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │ Mediterranean │                                                                                         │Marvin Gardens │
    │    Avenue     │                                                                                         │               │
    │{h["01"]}      │                                                                                         │{h["29"]}      │
    │{p["01"]}      │                                                                                         │{p["29"]}      │
    ├───────────────┼─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┼───────────────┤
    │               │         │         │         │         │         │         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │    GO!        │Boardwalk│ Luxury  │  Park   │ Chance  │  Short  │Pennsyl- │Community│ North   │ Pacific │  Go To Jail   │
    │               │         │  Tax    │  Place  │         │  Line   │ vania   │  Chest  │ Carolina│ Avenue  │               │
    │               │         │         │         │         │         │ Avenue  │         │ Avenue  │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │{h["00"]}      │{h["39"]}│{h["38"]}│{h["37"]}│{h["36"]}│{h["35"]}│{h["34"]}│{h["33"]}│{h["32"]}│{h["31"]}│{h["30"]}      │
    │{p["00"]}      │{p["39"]}│{p["38"]}│{p["37"]}│{p["36"]}│{p["35"]}│{p["34"]}│{p["33"]}│{p["32"]}│{p["31"]}│{p["30"]}      │
    └───────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴───────────────┘
    """

    return board
