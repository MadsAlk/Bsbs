from detection import detect
from collect_data import shoot
from train_model import train
import socket
from time import sleep

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


print(firebase_admin)

cred = credentials.Certificate("firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bsbs-2854d-default-rtdb.europe-west1.firebasedatabase.app/'
})



# print(db.reference('Customer').child('1181638').child('year').get())

def register():
    id = input("please enter your id")
    fname = input("please enter your first name")
    lname = input("please enter your last name")
    print("please enter your birthdate")
    year = input("Year:")
    month = input("month:")
    day = input("day")
    return id



ip = "192.168.1.5" #"192.168.1.12"  IP of Raspberry Pi

# # start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8081))
serv.listen(5)
print("SERVER: started")

while True:
    # establish connection
    conn, addr = serv.accept()
    recieved_msg = ''
    print("SERVER: connection to Client established")


    data = conn.recv(4096).decode()
    while not data:
        print("XXX didnt recieve data from conn XXX")
        sleep(1)
        data = conn.recv(4096).decode()

    print("Recieved: ", data)

    # if recieved_msg == 'connected':
    #     print(recieved_msg)
    
    
    print("Welcome to Bsbs, enter:")
    print("1: if your have an account")
    print("2: if you are a new user")


    try:
        user = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        user = 1


    if user == 1:
        id = detect()
    else:
        id = register()
        print("take pictures")
        shoot(id)
        print("please wait while the your account is being created")
        train()
        print("Ready")
        id = detect()

    # send message back to client
    msg = "detected " + id 
    conn.send(msg.encode())

    # close connection and exit
    # conn.close()
    # break




    