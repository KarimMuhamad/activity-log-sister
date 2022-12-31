import socket
import pickle
from datetime import datetime
from os import system, name
import time

hName = socket.gethostname()
ipAdd = socket.gethostbyname(hName)

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

lsTodo = []


def send(command) :
    log = {
        "host" : hName,
        "ip_addres" : ipAdd,
        "date" : datetime.today().strftime("%d/%m/%Y"),
        "time" : datetime.now().strftime("%H:%M:%S"),
        "activity" : command[0],
        "value" : command[1]
    }

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TCP_IP, TCP_PORT)) 
    client.send(pickle.dumps(log))
    client.close()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def countDown(endtime) :
    if(datetime.now() >= endtime) :
        return "------"
    elif(endtime > datetime.now()) :
        return endtime - datetime.now()
    

def checkStatus(endtime) :
    if(datetime.now() >= endtime) :
        return "Berakhir"
    elif(endtime > datetime.now()) :
        return "Belum Selesai"

while 1 :
    print("To Do List App")
    idx =1
    for i in lsTodo :
        i["Status"] = checkStatus(i["Waktu Berakhir"])

        print(f'[{idx}]. {i["Nama"]} \t {i["Status"]} \t {countDown(i["Waktu Berakhir"])}')
        idx+=1

    print("""
    1 : Add To Do
    2 : Remove To Do
    3 : Exit
    """)
    inp = int(input("Masukan Pilihan : "))

    clear()
    if(inp == 1) :
        nama = input("Masukan nama todo : ")
        d, m, y = map(int, input("Masukan tanggal mulai (23/12/2022) : ").split("/"))
        hr, mnt = map(int, input("Masukan Jam Mulai (HH:MM): ").split(":"))
        tdoEndDate = datetime(y, m, d, hr, mnt)

        todo = {
            "Nama" : nama,
            "Waktu Mulai" : datetime.now(),
            "Waktu Berakhir" : tdoEndDate,
            "Status" : "Belum Selesai"
            }

        lsTodo.append(todo)
        send(["Add", todo])
    elif(inp == 2) :
        src = input("Hapus :")
        lsTodo.remove(src)
        send(["Delete", src])
    elif inp == 3 : 
        exit()
