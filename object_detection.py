import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

use_seat = []
missed = []


def seat_use(bbox, region):
    use_seat.clear()
    for i in range(len(region)):
        for j in range(len(bbox)):
            if bbox[j][0]<=region[i][0]<=bbox[j][2] and bbox[j][1]<=region[i][1]<=bbox[j][3]:
                use_seat.append(i)
                
# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

region = [(100,100),(200,200)]

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    if not status:
        break

    # apply object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(frame)
    seat_use(bbox,region)
    print(use_seat)
    for i in range(len(bbox)):
        if label[i] == 'person':
            print(bbox[i], label[i], conf[i])

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)
    # display output
    cv2.imshow("Real-time object detection", out)
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows()   

