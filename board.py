import emoji


def build_board():

    p = dict()
    for i in range(41):
        key = f"{i}"
        if i < 10:
            key = f"0{i}"
        print(key)
        p[key] = 9 * " "

    p["00"] = emoji.emojize(":red_heart:", language="alias") * 4 + 5 * " "

    board = f"""
    ┌──────────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬───────────────┐
    │              │         │         │         │         │         │         │         │         │         │               │
    │              │         │         │         │         │         │         │         │         │         │               │
    │Just Visiting │   St.   │Electric │ States  │Virginia │Pennsyl- │St James │Community│Tennessee│New York │    Free       │
    │              │ Charles │Company  │ Avenue  │ Avenue  │  vania  │ Place   │  Chest  │ Avenue  │ Avenue  │   Parking     │
    │              │  Place  │         │         │         │ Railroad│         │         │         │         │               │
    │              │         │         │         │         │         │         │         │         │         │               │
    │{p["10"]}     │{p["11"]}│{p["12"]}│{p["13"]}│{p["14"]}│{p["15"]}│{p["16"]}│{p["17"]}│{p["18"]}│{p["19"]}|{p["20"]}      │
    ├──────────────┼─────────┼─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┼───────────────┤
    │              │         │                                                                               │               │
    │Connecticut   │  Jail   │                                                                               │Kentucky Avenue│
    │Avenue        │         │                                                                               │               │
    │              │         │                                                                               │               │
    │{p["09"]}     │{p["40"]}│                                                                               │{p["21"]}      │
    ├──────────────┼─────────┘                                                                               ├───────────────┤
    │              │                                                                                         │               │
    │  Vermont     │                                                                                         │    Chance     │
    │   Avenue     │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["08"]}     │                                                                                         │{p["22"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │  Chance      │                                                                                         │Indiana Avenue │
    │              │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["07"]}     │                                                                                         │{p["23"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │ Oriental     │                                                                                         │Illinois Avenue│
    │  Avenue      │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["06"]}     │                                                                                         │{p["24"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │ Reading      │                                                                                         │ B&O Railroad  │
    │ Railroad     │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["05"]}     │                                                                                         │{p["25"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │ Income Tax   │                                                                                         │Atlantic Avenue│
    │              │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["04"]}     │                                                                                         │{p["26"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │Baltic Avenue │                                                                                         │Ventnor Avenue │
    │              │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["03"]}     │                                                                                         │{p["27"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │ Community    │                                                                                         │ Water Works   │
    │   Chest      │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["02"]}     │                                                                                         │{p["28"]}      │
    ├──────────────┤                                                                                         ├───────────────┤
    │              │                                                                                         │               │
    │Meditteranean │                                                                                         │Marvin Gardens │
    │  Avenue      │                                                                                         │               │
    │              │                                                                                         │               │
    │{p["01"]}     │                                                                                         │{p["29"]}      │
    ├──────────────┼─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┼───────────────┤
    │              │         │         │         │         │         │         │         │         │         │               │
    │              │         │         │         │         │         │         │         │         │         │               │
    │    GO!       │Boardwalk│ Luxury  │   Park  │ Chance  │  Short  │Pennsyl- │Community│ North   │ Pacific │  Go To Jail   │
    │              │         │  Tax    │   Place │         │  Line   │ vania   │  Chest  │ Carolina│ Avenue  │               │
    │              │         │         │         │         │         │ Avenue  │         │ Avenue  │         │               │
    │              │         │         │         │         │         │         │         │         │         │               │
    │{p["00"]}     │{p["39"]}│{p["38"]}│{p["37"]}│{p["36"]}│{p["35"]}│{p["34"]}│{p["33"]}│{p["32"]}│{p["31"]}│{p["30"]}      │
    └──────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴───────────────┘
    """

    return board
