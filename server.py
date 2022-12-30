import socket

hName = socket.gethostname()
ipAdd = socket.gethostbyname(hName)

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen()

print("Server is on")

while True:
    conn, addr = s.accept()
    print("Connected to", addr)
    data = conn.recv(BUFFER_SIZE).decode()
    conn.send("Hallo From Server".encode())
    print(data)
    conn.close()