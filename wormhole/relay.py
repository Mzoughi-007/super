import socket

EARTH_PORT = 5001
SPACECRAFT_IP = "127.0.0.1"
SPACECRAFT_PORT = 5002

# Create sockets
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(("127.0.0.1", EARTH_PORT))

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Satellite ready to forward messages...")

while True:
    message, addr = recv_sock.recvfrom(2048)
    print(f"Satellite received bundle from {addr}")

    # Forward the message as-is
    send_sock.sendto(message, (SPACECRAFT_IP, SPACECRAFT_PORT))
    print("Satellite forwarded bundle")

