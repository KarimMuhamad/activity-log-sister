import socket
import pickle

hName = socket.gethostname()
ipAdd = socket.gethostbyname(hName)

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Server is on")

activity_log = []

while True:

    conn, addr = s.accept()
    data = pickle.loads(conn.recv(BUFFER_SIZE))
    activity_log.append(data)

    conn.send(pickle.dumps(activity_log))
    conn.close()