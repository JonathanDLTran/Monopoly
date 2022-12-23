import emoji


def build_board():

    p0 = emoji.emojize(":red_heart:", language="alias") * 4
    p1 = emoji.emojize(":red_heart:", language="alias") * 4

    board = f"""
    ┌──────────────┬────────┬─────────┬──────────┬─────────┬──────────┬────────┬─────────┬─────────┬──────────┬───────────────┐
    │              │        │         │          │         │          │        │         │         │          │               │
    │              │        │         │          │         │          │        │         │         │          │               │
    │              │St.     │Electric │ States   │Virginia │Pennsyl-  │St James│Community│Tennessee│New York  │               │
    │Just Visiting │ Charles│Company  │ Avenue   │ Avenue  │  vania   │ Place  │  Chsst  │ Avenue  │ Avenue   │     Free      │
    │              │  Place │         │          │         │ Railroad │        │         │         │          │   Parking     │
    │              │        │         │          │         │          │        │         │         │          │               │
    │{p1}          │{p1}    │{p1}     │{p1}      │{p1}     │{p1}      │{p1}    │{p1}     │{p1}     │{p1}      |{p1}           │
    ├──────────────┼────────┼─────────┴──────────┴─────────┴──────────┴────────┴─────────┴─────────┴──────────┼───────────────┤
    │              │        │                                                                                 │               │
    │Connecticut   │        │                                                                                 │               │
    │Avenue        │ Jail   │                                                                                 │Kentucky Avenue│
    │{p1}          │{p1}    |                                                                                 │               │
    ├──────────────┼────────┘                                                                                 │{p1}           │
    │              │                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │  Vermont     │                                                                                          │               │
    │   Avenue     │                                                                                          │    Chance     │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │              │                                                                                          │               │
    │  Chance      │                                                                                          │Indiana Avenue │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │ Oriental     │                                                                                          │Illinois Avenue│
    │  Avenue      │                                                                                          │               │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │              │                                                                                          │               │
    │ Reading      │                                                                                          │B&O Railroad   │
    │ Railroad     │                                                                                          │               │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │              │                                                                                          │               │
    │   Income Tax │                                                                                          │Atlantic Avenue│
    │              │                                                                                          │               │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │              │                                                                                          │               │
    │  Baltic      │                                                                                          │ Ventnor Avenue│
    │  Avenue      │                                                                                          │               │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │ Community    │                                                                                          │               │
    │   Chest      │                                                                                          │ Water Works   │
    │              │                                                                                          │               │
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┤                                                                                          ├───────────────┤
    │              │                                                                                          │               │
    │Meditteranean │                                                                                          │               │
    │  Avenue      │                                                                                          │ Marvin Gardens│
    │{p1}          │                                                                                          │{p1}           │
    ├──────────────┼─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬──────────┼───────────────┤
    │              │         │         │         │         │         │         │         │         │          │               │
    │              │         │         │         │         │         │         │         │         │          │               │
    │              │         │         │         │         │         │         │         │         │          │               │
    │              │         │         │         │         │         │         │         │         │          │               │
    │    GO!       │Boardwalk│ Luxury  │   Park  │ Chance  │  Short  │Pennsyl- │Community│ North   │ Pacific  │  Go To Jail   │
    │              │         │  Tax    │   Place │         │  Line   │ vania   │  Chest  │ Carolina│ Avenue   │               │
    │              │         │         │         │         │         │ Avenue  │         │ Avenue  │          │               │
    │{p0}          │{p1}     │{p1}     │{p1}     │{p1}     │{p1}     │{p1}     │{p1}     │{p1}     │{p1}      │{p1}           │
    └──────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴──────────┴───────────────┘
    """

    return board
