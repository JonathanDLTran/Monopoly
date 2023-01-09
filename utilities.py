from constants import PLAYER_ID, SPACE


def get_uint_input(msg, invalid_msg, min_int=1, max_int=4):
    while True:
        str_input = input(msg).strip()

        if str_input.isdigit():
            int_input = int(str_input)
            if min_int <= int_input <= max_int:
                return int_input

        print(invalid_msg)


def extend_int_to_string(i):
    assert 0 <= i < 100

    str_of_int = f"{i}"
    if i < 10:
        str_of_int = f"0{i}"

    return str_of_int


def gen_player_id():
    global PLAYER_ID
    PLAYER_ID += 1
    return PLAYER_ID


def format_string(string, length):
    assert 0 < length
    if len(string) < length:
        return string + SPACE * (length - len(string))
    return string[:length]


def is_string_plus_number(string, user_input):
    if SPACE not in user_input:
        return (False, None)
    split_input = user_input.split(SPACE)
    if len(split_input) != 2:
        return (False, None)
    if split_input[0] != string:
        return (False, None)
    if not split_input[1].isnumeric():
        return (False, None)
    return (True, int(split_input[1]))
