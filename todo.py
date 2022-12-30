import socket
import pickle
from datetime import date, datetime

hName = socket.gethostname()
ipAdd = socket.gethostbyname(hName)

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

def send(command) :
    log = {
        "host" : hName,
        "ip_addres" : ipAdd,
        "date" : date.today().strftime("%d/%m/%Y"),
        "time" : datetime.now().strftime("%H:%M:%S"),
        "activity" : command[0],
        "value" : command[1]
    }
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(pickle.dumps(log))
    s.close()