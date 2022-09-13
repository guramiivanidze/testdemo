import names

import random
import string


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


names = {
    "first_name": names.get_first_name("male"),
    "last_name": names.get_last_name(),
    "full_name": names.get_full_name("male"),
    "name_with_space": names.get_first_name("male") + " ",
    "name_with_nonASCI": names.get_first_name("male") + "სს",
    "name_with_number": names.get_first_name("male") + "12",
    "name_with_symbol": names.get_first_name("male") + "@",
    "first_space_then_name": " " + names.get_first_name("male"),
    "empty": "",
}

emails = {
    "random_email": random_char(7) + "@gmail.com",
    "without_ATSIGN": random_char(7) + "gmail.com",
    "without_domain": random_char(7) + "gmail",
    "non_ASCII": "ასდას@გმაილ.ცომ",
    "only_domain": "gmail.com",
}

current_Address = {
    "full_address": random_char(7) +" "+ str(int(random.random() * 10)),
}


