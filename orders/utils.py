from random import randint

from app.config import SECRET
from utils.general import gen_hex_hash


def generate_string_for_hash(secret, **kwargs):
    string = ':'.join([str(kwargs[key]) for key in sorted(kwargs)])
    string += secret
    return string


def generate_sign(**params):
    return gen_hex_hash(generate_string_for_hash(SECRET, **params))


def get_order_id():
    return randint(0, 10000)

