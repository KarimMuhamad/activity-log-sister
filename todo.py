import socket

hName = socket.gethostname()
ipAdd = socket.gethostbyname(hName)

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str("Hallo From Client" + hName).encode())
data = s.recv(BUFFER_SIZE).decode()
print(data)