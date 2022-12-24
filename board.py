from utilities import extend_int_to_string

SPACE = " "
PLAYER_SYMBOL_STRING_LENGTH = 9


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

    board = f"""
    ┌───────────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬───────────────┐
    │               │         │         │         │         │         │         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │ Just Visiting │   St.   │Electric │ States  │Virginia │Pennsyl- │St. James│Community│Tennessee│New York │    Free       │
    │               │ Charles │Company  │ Avenue  │ Avenue  │ vania   │ Place   │  Chest  │ Avenue  │ Avenue  │   Parking     │
    │               │  Place  │         │         │         │ Railroad│         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │{p["10"]}      │{p["11"]}│{p["12"]}│{p["13"]}│{p["14"]}│{p["15"]}│{p["16"]}│{p["17"]}│{p["18"]}│{p["19"]}|{p["20"]}      │
    ├───────────────┼─────────┼─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┼───────────────┤
    │               │         │                                                                               │               │
    │  Connecticut  │  Jail   │                                                                               │Kentucky Avenue│
    │    Avenue     │         │                                                                               │               │
    │               │         │                                                                               │               │
    │{p["09"]}      │{p["40"]}│                                                                               │{p["21"]}      │
    ├───────────────┼─────────┘                                                                               ├───────────────┤
    │               │                                                                                         │               │
    │Vermont Avenue │                                                                                         │    Chance     │
    │               │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["08"]}      │                                                                                         │{p["22"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │    Chance     │                                                                                         │Indiana Avenue │
    │               │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["07"]}      │                                                                                         │{p["23"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │Oriental Avenue│                                                                                         │Illinois Avenue│
    │               │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["06"]}      │                                                                                         │{p["24"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │   Reading     │                                                                                         │ B&O Railroad  │
    │   Railroad    │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["05"]}      │                                                                                         │{p["25"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │  Income Tax   │                                                                                         │Atlantic Avenue│
    │               │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["04"]}      │                                                                                         │{p["26"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │ Baltic Avenue │                                                                                         │Ventnor Avenue │
    │               │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["03"]}      │                                                                                         │{p["27"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    |Community Chest│                                                                                         │  Water Works  │
    │               │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["02"]}      │                                                                                         │{p["28"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │ Mediterranean │                                                                                         │Marvin Gardens │
    │    Avenue     │                                                                                         │               │
    │               │                                                                                         │               │
    │{p["01"]}      │                                                                                         │{p["29"]}      │
    ├───────────────┼─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┼───────────────┤
    │               │         │         │         │         │         │         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │    GO!        │Boardwalk│ Luxury  │  Park   │ Chance  │  Short  │Pennsyl- │Community│ North   │ Pacific │  Go To Jail   │
    │               │         │  Tax    │  Place  │         │  Line   │ vania   │  Chest  │ Carolina│ Avenue  │               │
    │               │         │         │         │         │         │ Avenue  │         │ Avenue  │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │{p["00"]}      │{p["39"]}│{p["38"]}│{p["37"]}│{p["36"]}│{p["35"]}│{p["34"]}│{p["33"]}│{p["32"]}│{p["31"]}│{p["30"]}      │
    └───────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴───────────────┘
    """

    return board
