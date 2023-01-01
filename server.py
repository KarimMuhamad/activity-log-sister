import socket
import pickle
from os import system, name

hName = socket.gethostname()
ipAdd = socket.gethostbyname(hName)

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 8024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Server is on")

activity_log = []

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

while True:

    conn, addr = s.accept()
    data = pickle.loads(conn.recv(BUFFER_SIZE))
    activity_log.append(data)
    
    conn.send(pickle.dumps(activity_log))

    for i in activity_log :
        print(f'{i["host"]} ({i["ip_addres"]}) {i["date"]} {i["time"]} melakukan {i["activity"]} value [{i["value"]}]')
        clear()

    conn.close()