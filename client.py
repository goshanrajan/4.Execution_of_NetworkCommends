
import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    ip = input("Enter website to ping (or exit): ")

    s.send(ip.encode())

    if ip.lower() == "exit":
        break

    result = s.recv(4096).decode()
    print(result)

s.close()

