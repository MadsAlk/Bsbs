# import cv2
# import prediction
# import socket
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from time import sleep

cred = credentials.Certificate('firebase_credentials.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://bsbs-2854d-default-rtdb.europe-west1.firebasedatabase.app/'
})
def update_balance(uid, balance):
    prev_balance = db.reference('Customer').child(uid).child('balance').get()
    balance+= prev_balance
    db.reference('Customer').child(uid).update({
        'balance': balance,
    })
'''
#Creating the database and adding content
ref = db.reference('/')
ref.set({
    'Customer':
        {
            '1181638' : {
                'fname' : 'Ahmad',
                'lname' : 'AlKhaldi',
                'balance' : 0.0,
                'year' : 2000,
                'month' : 10,
                'day' : 22,
                'city' : 'Jenin'
            },
            '1182972' : {
                'fname' : 'Abdallah',
                'lname' : 'Afifi',
                'balance' : 0.0,
                'year' : 2000,
                'month' : 6,
                'day' : 19,
                'city' : 'Jerusalem'
            }
        }
})
'''
'''
#Updating the database content:
ref = db.reference('Customer')
cust_ref = ref.child('Ahmad')
cust_ref.update({
    'balance' : 2.5
})
'''
'''
#Adding a new Customer
ref = db.reference('Customer')
ref.child("test").set({
            'lname' : 'Jabsheh',
            'id' : '1182932',
            'balance' : 0.0,
            'year' : 2000,
            'month' : 8,
            'day' : 11,
            'city' : 'Jerusalem'
    })
'''
'''
#deleting data
ref = db.reference('Customer').child('test')
ref.delete()
'''
'''

ip = "192.168.1.29"
#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 8080))
print("Client: Connected")

def screenshot():
    global cam
    cv2.imwrite('screenshot.png', cam.read()[1])


with open('labels.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		listli=strip_lines.split()

		m=listl.append(listli)
	print(listl)

# cam = cv2.VideoCapture(1)


while True:
    # sleep(1)
    cam.release()
    from_server = client.recv(4096).decode()
    while from_server.split()[0] != "detected":
        from_server = client.recv(4096).decode()
    cam = cv2.VideoCapture(1)
    ret, img = cam.read()

    cv2.imshow('My camera',img)

    ch = cv2.waitKey(5)
    if ch == 27:
        break
    screenshot()

    result = prediction.predict('screenshot.png')

    print(listl[result][1])

        # exit


cv2.destroyAllWindows()



'''