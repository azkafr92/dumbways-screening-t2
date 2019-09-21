import secrets
import string


def generate_key():
    alphanumeric = string.ascii_letters + string.digits
    key = ''.join([secrets.choice(alphanumeric) for i in range(5)])
    return key


def generate_key_container():
    key_container = '-'.join([generate_key() for i in range(4)])
    return key_container


if __name__ == "__main__":
    for i in range(0, 251):
        print(generate_key_container())
    print('{} serial numbers has been generated.'.format(i))
