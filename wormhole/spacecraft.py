import socket
from wormhole_crypto import load_key, decrypt, decode_rs, validate_payload

SPACECRAFT_PORT = 5002
key = load_key()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", SPACECRAFT_PORT))

print("Spacecraft ready to receive commands...")

while True:
    message, addr = sock.recvfrom(2048)
    try:
        hash_val, encrypted = message.split(b"||", 1)
        if not validate_payload(encrypted, hash_val.decode()):
            print("Hash mismatch — possible corruption.")
        decrypted = decrypt(encrypted, key)
        recovered = decode_rs(decrypted)
        print(f"Spacecraft received: {recovered.decode()} from {addr}")
    except Exception as e:
        print(f"Decryption or recovery failed: {e}")

