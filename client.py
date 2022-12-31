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
    if(datetime.now() >= endtime):
        return "------"
    elif(endtime > datetime.now()) :
        return endtime - datetime.now()
    else :
        return "Done"
    

def checkStatus(lsTd) :
    if(datetime.now() >= lsTd["Waktu Berakhir"] and lsTd["Status"] != "Selesai") :
        lsTd["Status"] = "Berakhir"
    elif(lsTd["Waktu Berakhir"] > datetime.now() and lsTd["Status"] != "Selesai") :
        lsTd["Status"] = "Belum Selesai"


def printTodo(listOfTodo) :
    idx =1
    for i in lsTodo :
        checkStatus(i)

        print(f'[{idx}]. {i["Nama"]} \t {i["Status"]} \t {countDown(i["Waktu Berakhir"])}')
        idx+=1

while 1 :
    print("To Do List App")
    printTodo(lsTodo)


    print("""
    1 : Add To Do
    2 : Check Todo
    3 : Remove To Do
    4 : Log
    5 : Exit
    """)
    inp = int(input("Masukan Pilihan : "))

    clear()
    if(inp == 1) :
        nama = input("Masukan nama todo : ")
        d, m, y = datetime.now().day, datetime.now().month, datetime.now().year
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
        clear()

    elif(inp == 2) :
        printTodo(lsTodo)

        src = input("Checked To Do :")

        for i in lsTodo :
            if i["Nama"] == src :
                i["Status"] = "Selesai"
                print(i)
                send(["Checked", i])
                # clear()
            else :
                print("Todo List tidak di temukan")
                clear()

    elif(inp == 3) :
        printTodo(lsTodo)

        src = input("Hapus :")

        for i in lsTodo :
            if i["Nama"] == src :
                lsTodo.remove(i)
                send(["Delete", i])
                clear()
            else :
                print("Todo List tidak di temukan")
                clear()

        
    elif inp == 4 : 
        print("Log disini")
        input("")
        clear()
