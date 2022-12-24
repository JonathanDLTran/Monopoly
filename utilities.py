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
