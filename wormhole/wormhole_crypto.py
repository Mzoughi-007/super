import hashlib
import random
from cryptography.fernet import Fernet
import reedsolo
import os

def load_key():
    path = os.path.join(os.path.dirname(__file__), "shared.key")
    with open(path, "rb") as f:
        return f.read()


# Generate and save Fernet key
def generate_key():
    key = Fernet.generate_key()
    with open("shared.key", "wb") as f:
        f.write(key)
    return key


# Encrypt and decrypt
def encrypt(data: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(data)

def decrypt(data: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(data)

# ECC encode/decode
def encode_rs(data: bytes) -> bytes:
    rs = reedsolo.RSCodec(10)
    return rs.encode(data)

def decode_rs(data: bytes) -> bytes:
    rs = reedsolo.RSCodec(10)
    decoded = rs.decode(data)
    if isinstance(decoded, tuple):
        return decoded[0]  # extract the data part
    return decoded

# Bit flip simulation
def flip_bits(data: bytes, flip_rate=0.01) -> bytes:
    flipped = bytearray(data)
    for i in range(len(flipped)):
        for bit in range(8):
            if random.random() < flip_rate:
                flipped[i] ^= 1 << bit
    return bytes(flipped)

# Hash validation
def hash_payload(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()

def validate_payload(payload: bytes, expected_hash: str) -> bool:
    return hash_payload(payload) == expected_hash

