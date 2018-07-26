import hashlib


def gen_hex_hash(string):
    """
    produces hash from the string
    :param string: any string
    :return: HEX representation of the hash
    """
    return hashlib.sha256(string.encode()).hexdigest()
