import socket
import reedsolo

EARTH_IP = "127.0.0.1"
EARTH_PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

rs = reedsolo.RSCodec(10)
message = b"Check radiation shielding"
encoded = rs.encode(message)

sock.sendto(encoded, (EARTH_IP, EARTH_PORT))
print(f"Sent message: {message}")

sock.close()

