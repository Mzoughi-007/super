import socket, sys
from wormhole_crypto import load_key, encrypt, encode_rs, hash_payload

SATELLITE_IP = "127.0.0.1"
SATELLITE_PORT = 5001
key = "q-yQMksID1FOSioaLvWNf5Fmjd0aq92FsHCUL1i7rRI="
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if len(sys.argv) > 1:
    commands = [" ".join(sys.argv[1:])]
else:
    commands = [input("Enter command to send: ")]

for cmd in commands:
    encoded = encode_rs(cmd.encode())
    if isinstance(encoded, tuple):
        encoded = encoded[0]
    if not isinstance(encoded, bytes):
        encoded = bytes(encoded)
    encrypted = encrypt(encoded, key)
    hash_val = hash_payload(encrypted).encode()
    bundle = hash_val + b"||" + encrypted
    sock.sendto(bundle, (SATELLITE_IP, SATELLITE_PORT))
    print(f"Earth sent: {cmd}")

sock.close()

