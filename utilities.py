def get_uint_input(msg, invalid_msg, min_int=1, max_int=4):
    while True:
        str_input = input(msg).strip()

        if str_input.isdigit():
            int_input = int(str_input)
            if min_int <= int_input <= max_int:
                return int_input

        print(invalid_msg)
