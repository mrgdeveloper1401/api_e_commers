from string import digits
from random import choices


def random_code():
    return int(''.join(choices(digits, k=9)))
