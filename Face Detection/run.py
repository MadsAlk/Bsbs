from detection import detect
from collect_data import shoot
from train_model import train
import socket

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


print(firebase_admin)

cred = credentials.Certificate("firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bsbs-2854d-default-rtdb.europe-west1.firebasedatabase.app/'
})


print(db.reference('Customer').child('1181638').child('year').get())

# def register():
#     id = input("please enter your id")
#     fname = input("please enter your first name")
#     lname = input("please enter your last name")
#     print("please enter your birthdate")
#     year = input("Year:")
#     month = input("month:")
#     day = input("day")



# ip = "192.168.1.12"  # IP of Raspberry Pi

# # start server
# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind((ip, 8080))
# serv.listen(5)
# print("SERVER: started")

# while True:
#     # establish connection
#     conn, addr = serv.accept()
#     recieved_msg = ''
#     print("SERVER: connection to Client established")

#     # while True:
#     # receive data and print
#     data = conn.recv(4096).decode()
#     # if not data: break
#     if not data:
#         sleep(1)
#         # data = conn.recv(4096).decode()
#     # recieved_msg += data
#     recieved_msg = data
#     print("Recieved: ", recieved_msg)

#     if recieved_msg == 'connected':
#         print(msg)
    
    
#     print("Welcome to Bsbs, enter:")
#     print("1: if your have an account")
#     print("2: if you are a new user")
#     user = int(input())
#     if user == 1:
#         id = detect()
#     else:
#         register()
#         print("take pictures")
#         shoot(id)
#         print("please wait while the your account is being created")
#         train()
#         print("Ready")
#         id = detect()

#     # send message back to client
#     msg = "detected " + id 
#     conn.send(msg.encode())

#     # close connection and exit
#     # conn.close()
#     # break




    