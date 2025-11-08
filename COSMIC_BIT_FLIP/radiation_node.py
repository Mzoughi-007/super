import socket
import random

EARTH_IP = "127.0.0.1"
EARTH_PORT = 5001
CORRUPTION_IP = "127.0.0.1"
CORRUPTION_PORT = 5002

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind((EARTH_IP, EARTH_PORT))

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

corrupted_once = False

while True:
    message, addr = recv_sock.recvfrom(2048)
    if not corrupted_once:
        message = bytearray(message)
        indices = random.sample(range(len(message)), 2)
        for i in indices:
            bit = 1 << random.randint(0, 7)
            message[i] ^= bit
        message = bytes(message)
        corrupted_once = True
        print("Corrupted message (2 bits flipped)")
    send_sock.sendto(message, (CORRUPTION_IP, CORRUPTION_PORT))
    break  # only process one message

