import random
import string

TOKEN_LENGTH = 4


def encode():
    return __generate_bas62()


def __generate_bas62():
    chars = string.ascii_letters + string.digits
    base62 = ''
    for _ in range(TOKEN_LENGTH):
        base62 += random.choice(chars)
    return base62
