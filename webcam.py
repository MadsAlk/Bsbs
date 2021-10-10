import cv2
import prediction
import socket
from time import sleep
# ip = "192.168.1.29"
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((ip, 8080))
# print("Client: Connected")

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

cam = cv2.VideoCapture(0)

while True:
    sleep(1)
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