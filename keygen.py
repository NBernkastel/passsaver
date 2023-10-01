from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os


def keygen(password: str) -> bytes:
    password = password.encode()
    salt = b'[U\xc2\xb7U1\xa0\x80\x04\x13Np\x1eM\x90\xa3'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )
    return base64.urlsafe_b64encode(kdf.derive(password))
