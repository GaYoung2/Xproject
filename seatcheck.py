import socket
import threading
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import math

data = "0"
constant_object = ['chair', 'dining table']

def detect():
    global data
    region = [[130,40,150,80,0],[130,120,150,90,0],[70,180,230,200,0],[350,30,200,90,0],[350,130,100,75,0],[350,200,200,200,0]]
    def onMouse(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(event,x,y, )
    def seat_use(bbox, label, region):
        str_buffer = ['0','0','0','0','0','0']
        for i in range(len(region)):
            count = 0
            midle_seat = (region[i][0]+region[i][2]/2,region[i][1]+region[i][3]/2)
            for j in range(len(bbox)):
                midle_object = (bbox[j][2]-(bbox[j][2]-bbox[j][0])/2,bbox[j][3]-(bbox[j][3]-bbox[j][1])/2)
                x_dis=midle_object[0]-midle_seat[0]
                y_dis=midle_object[1]-midle_seat[1]
                max_dis=max(region[i][2]/2,region[i][3]/2)
                dis = math.sqrt((x_dis*x_dis)+(y_dis*y_dis))
                if dis <= max_dis and label[j] not in constant_object:
                    count = 1
                    if (region[i][4]>5):
                        str_buffer[i] = '1'
                    else:
                        str_buffer[i] = '0'
            if count == 1:
                if region[i][4]<10:
                    region[i][4] += 1
            elif count==0:
                if region[i][4]>0:
                    region[i][4] -= 1
            print(i,region[i][4])
        return ''.join(str_buffer)
    webcam = cv2.VideoCapture(1)
    if not webcam.isOpened():
        print("Could not open webcam")
        exit()
    while webcam.isOpened():
        status, frame = webcam.read()
        if not status:
            break
        cv2.waitKey(1000)
        bbox, label, conf = cv.detect_common_objects(frame)
        data = seat_use(bbox, label, region)
        print(data)
        """ for i in range(len(bbox)):
            print(bbox[i], label[i], conf[i])  """

        out = draw_bbox(frame, bbox, label, conf, write_conf=True)
        cv2.imshow("Cam", out)
        cv2.setMouseCallback("Cam",onMouse)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    webcam.release()
    cv2.destroyAllWindows()  

def send_data():
    global data
    msg = data
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()

webcam_thread = threading.Thread(target=detect)
webcam_thread.start()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.11', 10007))
server_socket.listen(0)

while True:
    client_socket, addr = server_socket.accept()
    send_thread = threading.Thread(target=send_data)
    send_thread.start()