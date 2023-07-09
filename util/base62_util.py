import random
import string

token_lengh = 4


def encode():
    return __generate_bas62()


def __generate_bas62():
    chars = string.ascii_letters + string.digits
    base62 = ''
    for _ in range(token_lengh):
        base62 += random.choice(chars)
    return base62
