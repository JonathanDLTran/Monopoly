import emoji

STARTING_CASH_AMOUNT = 1500
MAX_PLAYERS = 4

NUM_PROPERTIES = 40

SPACE = " "
PLAYER_SYMBOL_STRING_LENGTH = 9

MEDITERRANEAN_AVENUE = "Mediterranean Avenue"
BALTIC_AVENUE = "Baltic Avenue"
READING_RAILROAD = "Reading Railroad"
ORIENTAL_AVENUE = "Oriental Avenue"
VERMONT_AVENUE = "Vermont Avenue"
CONNECTICUT_AVENUE = "Connecticut Avenue"
ST_CHARLES_PLACE = "St. Charles Place"
ELECTRIC_COMPANY = "Electric Company"
STATES_AVENUE = "States Avenue"
VIRGINIA_AVENUE = "Virginia Avenue"
PENNSYLVANIA_RAILROAD = "Pennsylvania Railroad"
ST_JAMES_PLACE = "St. James Place"
TENNESSEE_AVENUE = "Tennessee Avenue"
NEW_YORK_AVENUE = "New York Avenue"
KENTUCKY_AVENUE = "Kentucky Avenue"
INDIANA_AVENUE = "Indiana Avenue"
ILLINOIS_AVENUE = "Illinois Avenue"
B_AND_O_RAILROAD = "B&O Railroad"
ATLANTIC_AVENUE = "Atlantic Avenue"
VENTNOR_AVENUE = "Ventnor Avenue"
WATER_WORKS = "Water Works"
MARVIN_GARDENS = "Marvin Gardens"
PACIFIC_AVENUE = "Pacific Avenue"
NORTH_CAROLINA_AVENUE = "North Carolina Avenue"
PENNSYLVANIA_AVENUE = "Pennsylvania Avenue"
SHORT_LINE = "Short Line"
PARK_PLACE = "Park Place"
BOARDWALK = "Boardwalk"

PROPERTY_TO_INDEX_MAP = {
    MEDITERRANEAN_AVENUE: "01",
    BALTIC_AVENUE: "03",
    READING_RAILROAD: "05",
    ORIENTAL_AVENUE: "06",
    VERMONT_AVENUE: "08",
    CONNECTICUT_AVENUE: "09",
    ST_CHARLES_PLACE: "11",
    ELECTRIC_COMPANY: "12",
    STATES_AVENUE: "13",
    VIRGINIA_AVENUE: "14",
    PENNSYLVANIA_RAILROAD: "15",
    ST_CHARLES_PLACE: "16",
    TENNESSEE_AVENUE: "18",
    NEW_YORK_AVENUE: "19",
    KENTUCKY_AVENUE: "21",
    INDIANA_AVENUE: "23",
    ILLINOIS_AVENUE: "24",
    B_AND_O_RAILROAD: "25",
    ATLANTIC_AVENUE: "26",
    VENTNOR_AVENUE: "27",
    WATER_WORKS: "28",
    MARVIN_GARDENS: "29",
    PACIFIC_AVENUE: "31",
    NORTH_CAROLINA_AVENUE: "32",
    PENNSYLVANIA_AVENUE: "34",
    SHORT_LINE: "35",
    PARK_PLACE: "37",
    BOARDWALK: "39",
}

INDEX_TO_PROPERTY_MAP = {
    PROPERTY_TO_INDEX_MAP[k]: k for k in PROPERTY_TO_INDEX_MAP
}

CAN_BUILD = {k for k in INDEX_TO_PROPERTY_MAP}

HOUSE = emoji.emojize(":house:")
HOTEL = emoji.emojize(":hotel:")

# --------- USER COMMANDS ----------


YES_COMMAND = ["y", "yes"]
BUY_COMMANDS = ["b", "buy"]
INVENTORY_COMMANDS = ["i", "inv", "inventory"]
FINISH_COMMANDS = ["f", "fin", "finish"]
