import socket
import reedsolo

RECEIVER_IP = "127.0.0.1"
RECEIVER_PORT = 5002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((RECEIVER_IP, RECEIVER_PORT))

rs = reedsolo.RSCodec(10)

message, addr = sock.recvfrom(2048)
try:
    recovered, _, _ = rs.decode(message)
    print(f"Recovered message: {recovered}")
except reedsolo.ReedSolomonError:
    print("ECC recovery failed")

sock.close()

