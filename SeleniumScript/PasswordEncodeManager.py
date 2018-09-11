import base64


def passwordEncoder(password):
    encoded = password.encode('ascii')
    print("after ascii encoding")
    print(encoded)
    print('\n')

    base64encoded = base64.b64encode(encoded)
    print("after base64 encoding")
    print(base64encoded)
    print('\n')

    # base64decoded = base64.b64decode(base64encoded)
    # print("after base 64 decoding")
    # print(base64decoded)
    # print('\n')
    #
    # decoded = base64decoded.decode('ascii')
    # print("after ascii decoding")
    # print(decoded)


    return base64encoded


def passwordDecoder(password):
    base64decoded = base64.b64decode(password)
    print("after base 64 decoding")
    print(base64decoded)
    print('\n')

    decoded = base64decoded.decode('ascii')
    print("after ascii decoding")
    print(decoded)

    return decoded


def password():
    Password = b'czkzMTYyNDZj'
    return Password

