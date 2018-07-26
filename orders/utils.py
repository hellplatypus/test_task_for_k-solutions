from app_obj_for_gunicorn import app
from utils.general import gen_hex_hash


def generate_string_for_hash(secret, **kwargs):
    string = ':'.join([str(kwargs[key]) for key in sorted(kwargs)])
    string += secret
    return string


def generate_sign(**params):
    secret = app.config.get('SECRET', None)
    return gen_hex_hash(generate_string_for_hash(secret, **params))


if __name__ == '__main__':
    print(generate_sign(a=1, b=2))

