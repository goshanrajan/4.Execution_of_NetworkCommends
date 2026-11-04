
import socket
from pythonping import ping

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)

print("Server waiting for connection...")

c, addr = s.accept()
print("Connected to:", addr)

while True:
    msg = c.recv(1024).decode()

    if not msg or msg.lower() == "exit":
        print("Client disconnected")
        break

    try:
        result = ping(msg, count=4, verbose=False)
        c.send(str(result).encode())

    except Exception as e:
        c.send(f"Ping failed: {e}".encode())

c.close()
s.close()
