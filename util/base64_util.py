import base64


def encode(name: str):
    return base64.b64encode(name.encode("ascii")).decode("ascii")
