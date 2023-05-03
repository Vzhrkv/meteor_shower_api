import hashlib


def hash_password(password):
    encoded_password = password.encode()
    hashed_password = hashlib.sha256(encoded_password).hexdigest()
    return hashed_password
