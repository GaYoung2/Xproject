import socket
import threading
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import math

data = ""

def detect():
    global data
    region = [[0,0,100,100,0],]
    def seat_use(bbox):
        str_buffer = ""
        for i in range(len(region)):
            midle_seat = (region[i][0]+region[i][2]/2,region[i][1]+region[i][3]/2)
            for j in range(len(bbox)):
                midle_object = (bbox[j][0]+bbox[i][2]/2,bbox[i][1]+bbox[i][3]/2)
                x_dis=midle_object[0]-midle_seat[0]
                y_dis=midle_object[1]-midle_seat[1]
                max_dis=region[i][2]+bbox[j][2]
                dis = math.sqrt((x_dis*x_dis)+(y_dis*y_dis))
                if dis <= max_dis and len(str_buffer)<len(region):
                    if region[i][4]>50:
                        str_buffer = str_buffer + "1"
                    else:
                        str_buffer = str_buffer + "0"
                        region[i][4] = 0
                    region[i][4] += 1
                    print(region[i][4])
        return str_buffer       
    webcam = cv2.VideoCapture(1)

    if not webcam.isOpened():
        print("Could not open webcam")
        exit()

    while webcam.isOpened():
        status, frame = webcam.read()

        if not status:
            break

        bbox, label, conf = cv.detect_common_objects(frame)
        data = seat_use(bbox)
        for i in range(len(bbox)):
            print(bbox[i], label[i], conf[i]) 

        out = draw_bbox(frame, bbox, label, conf, write_conf=True)
        cv2.imshow("Cam", out)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    webcam.release()
    cv2.destroyAllWindows()  

webcam_thread = threading.Thread(target=detect)
webcam_thread.start()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.8', 10007))
server_socket.listen(0)

while True:
    client_socket, addr = server_socket.accept()
    msg = data
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()
    pass