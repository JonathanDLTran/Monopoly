from constants import *
from utilities import extend_int_to_string, format_string


def build_board(players, properties):

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

    for prop in properties:
        property_index = prop.id
        if prop.houses:
            n_houses = prop.houses
            assert 0 < n_houses <= 4
            h[property_index] = n_houses * HOUSE + \
                (PLAYER_SYMBOL_STRING_LENGTH - n_houses * 2) * SPACE

    # create owned by property dictionary
    o = dict()
    for i in range(41):
        key = extend_int_to_string(i)
        o[key] = PLAYER_SYMBOL_STRING_LENGTH * SPACE

    for prop in properties:
        property_index = prop.id
        for player in players:
            if player.id == prop.owner:
                o[property_index] = format_string(
                    player.name, PLAYER_SYMBOL_STRING_LENGTH)

    board = f"""
    ┌───────────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬───────────────┐
    │               │{GRE_HDR}│         │{GRE_HDR}│{GRE_HDR}│         │{YEL_HDR}│         │{YEL_HDR}│{YEL_HDR}│               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │ Just Visiting │   St.   │Electric │ States  │Virginia │Pennsyl- │St. James│Community│Tennessee│New York │    Free       │
    │               │ Charles │Company  │ Avenue  │ Avenue  │ vania   │ Place   │  Chest  │ Avenue  │ Avenue  │   Parking     │
    │               │  Place  │         │         │         │ Railroad│         │         │         │         │               │
    │               │Prop. 11 │Prop. 12 │Prop. 13 │Prop. 14 │Prop. 15 │Prop. 16 │         │Prop. 18 │Prop. 19 │               │
    │{o["10"]}      │{o["11"]}│{o["12"]}│{o["13"]}│{o["14"]}│{o["15"]}│{o["16"]}│{o["17"]}│{o["18"]}│{o["19"]}│{o["20"]}      │
    │{h["10"]}      │{h["11"]}│{h["12"]}│{h["13"]}│{h["14"]}│{h["15"]}│{h["16"]}│{h["17"]}│{h["18"]}│{h["19"]}│{h["20"]}      │
    │{p["10"]}      │{p["11"]}│{p["12"]}│{p["13"]}│{p["14"]}│{p["15"]}│{p["16"]}│{p["17"]}│{p["18"]}│{p["19"]}│{p["20"]}      │
    ├───────────────┼─────────┼─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┼───────────────┤
    │{RED_HDR      }│         │                                                                               │{BLU_HDR      }│
    │  Connecticut  │  Jail   │                                                                               │Kentucky Avenue│
    │    Avenue     │         │                                                                               │               │
    │  Property 9   │         |                                                                               │  Property 21  │
    │{o["09"]}      │{o["40"]}│                                                                               │{o["21"]}      │
    │{h["09"]}      │{h["40"]}│                                                                               │{h["21"]}      │
    │{p["09"]}      │{p["40"]}│                                                                               │{p["21"]}      │
    ├───────────────┼─────────┘                                                                               ├───────────────┤
    │{RED_HDR      }│                                                                                         │               │
    │Vermont Avenue │                                                                                         │    Chance     │
    │               │                                                                                         │               │
    │  Property 8   │                                                                                         │               │
    │{o["08"]}      │                                                                                         │{o["22"]}      │
    │{h["08"]}      │                                                                                         │{h["22"]}      │
    │{p["08"]}      │                                                                                         │{p["22"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │{BLU_HDR      }│
    │    Chance     │                                                                                         │Indiana Avenue │
    │               │                                                                                         │               │
    │               │                                                                                         │  Property 23  │
    │{o["07"]}      │                                                                                         │{o["23"]}      │
    │{h["07"]}      │                                                                                         │{h["23"]}      │
    │{p["07"]}      │                                                                                         │{p["23"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │{RED_HDR      }│                                                                                         │{BLU_HDR      }│
    │Oriental Avenue│                                                                                         │Illinois Avenue│
    │               │                                                                                         │               │
    │  Property 6   │                                                                                         │  Property 24  │
    │{o["06"]}      │                                                                                         │{o["24"]}      │
    │{h["06"]}      │                                                                                         │{h["24"]}      │
    │{p["06"]}      │                                                                                         │{p["24"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    │   Reading     │                                                                                         │ B&O Railroad  │
    │   Railroad    │                                                                                         │               │
    │  Property 5   │                                                                                         │  Property 25  │
    │{o["05"]}      │                                                                                         │{o["25"]}      │
    │{h["05"]}      │                                                                                         │{h["25"]}      │
    │{p["05"]}      │                                                                                         │{p["25"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │{VIO_HDR      }│
    │  Income Tax   │                                                                                         │Atlantic Avenue│
    │               │                                                                                         │               │
    │               │                                                                                         │  Property 26  │
    │{o["04"]}      │                                                                                         │{o["26"]}      │
    │{h["04"]}      │                                                                                         │{h["26"]}      │
    │{p["04"]}      │                                                                                         │{p["26"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │{GRY_HDR      }│                                                                                         │{VIO_HDR      }│
    │ Baltic Avenue │                                                                                         │Ventnor Avenue │
    │               │                                                                                         │               │
    │  Property 3   │                                                                                         │  Property 27  │
    │{o["03"]}      │                                                                                         │{o["27"]}      │
    │{h["03"]}      │                                                                                         │{h["27"]}      │
    │{p["03"]}      │                                                                                         │{p["27"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │               │                                                                                         │               │
    |Community Chest│                                                                                         │  Water Works  │
    │               │                                                                                         │               │
    │               │                                                                                         │  Property 28  │
    │{o["02"]}      │                                                                                         │{o["28"]}      │
    │{h["02"]}      │                                                                                         │{h["28"]}      │
    │{p["02"]}      │                                                                                         │{p["28"]}      │
    ├───────────────┤                                                                                         ├───────────────┤
    │{GRY_HDR      }│                                                                                         │{VIO_HDR      }│
    │ Mediterranean │                                                                                         │Marvin Gardens │
    │    Avenue     │                                                                                         │               │
    │  Property 1   │                                                                                         │  Property 29  │
    │{o["01"]}      │                                                                                         │{o["29"]}      │
    │{h["01"]}      │                                                                                         │{h["29"]}      │
    │{p["01"]}      │                                                                                         │{p["29"]}      │
    ├───────────────┼─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┼───────────────┤
    │               │{WHI_HDR}│         │{WHI_HDR}│         │         │{BEI_HDR}│         │{BEI_HDR}|{BEI_HDR}│               │
    │               │         │         │         │         │         │         │         │         │         │               │
    │    GO!        │Boardwalk│ Luxury  │  Park   │ Chance  │  Short  │Pennsyl- │Community│ North   │ Pacific │  Go To Jail   │
    │               │         │  Tax    │  Place  │         │  Line   │ vania   │  Chest  │ Carolina│ Avenue  │               │
    │               │         │         │         │         │         │ Avenue  │         │ Avenue  │         │               │
    │               │Prop. 39 │         │Prop. 37 │         │Prop. 35 │Prop. 34 │         │Prop. 32 │Prop. 31 │               │
    │{o["00"]}      │{o["39"]}│{o["38"]}│{o["37"]}│{o["36"]}│{o["35"]}│{o["34"]}│{o["33"]}│{o["32"]}│{o["31"]}│{o["30"]}      │
    │{h["00"]}      │{h["39"]}│{h["38"]}│{h["37"]}│{h["36"]}│{h["35"]}│{h["34"]}│{h["33"]}│{h["32"]}│{h["31"]}│{h["30"]}      │
    │{p["00"]}      │{p["39"]}│{p["38"]}│{p["37"]}│{p["36"]}│{p["35"]}│{p["34"]}│{p["33"]}│{p["32"]}│{p["31"]}│{p["30"]}      │
    └───────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴───────────────┘
    """

    return board
