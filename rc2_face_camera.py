import cv2
import numpy as np
import time
import os

# set the camera parameters 

camera_ID = 0

capture_wait_time = 1

camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

output = cv2.VideoWriter('./video/output.avi', fourcc, 20.0, (660, 500))

frame_gap = 25

imshow_str = '24 HOURS MONITORING'

# start the monitoring
frame_ID = 0

show_DetectWin = False
minNeighbors = 6

x_gap = 10
y_gap = 10
w_gap = 10
h_gap = 30

def detectFace(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_Cascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_alt.xml')
    faces = face_Cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=minNeighbors)

    # print(f"{frame.shape = }")
    frame_H = frame.shape[0]
    frame_W = frame.shape[1]


    for x, y, w, h in faces:
        if show_DetectWin:
            if x-x_gap > 0:
                x -= x_gap
            else:
                x = 0
            if y-y_gap > 0:
                y -= y_gap
            else:
                y = 0
            if w+w_gap < frame_W:
                w += w_gap
            else:
                w = frame_W
            if h+h_gap < frame_H:
                h += h_gap
            else:
                h = frame_H
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)

        if w >w_gap and h > h_gap:
            img_title = time.strftime('%H-%M-%S', time.localtime())
            img_dir = time.strftime('%Y-%m-%d', time.localtime())
            # print(f'{img_title = }')
            # print(f'{img_dir = }')

            cv2.waitKey(capture_wait_time * 1000)
            img_dir = './screenshot/' + img_dir + '/'
            if not os.path.exists(img_dir):
                os.mkdir(img_dir)
            cv2.imwrite(img_dir + img_title + '.jpg', frame)


while camera.isOpened():
    frame_ID += 1
    if frame_ID % frame_gap == 0:
        ret, frame = camera.read()
        # print(f'{ret = }')
        # print(f'{frame = }')

        if not ret:
            print('Unable to capture, exit recording')
            break

        # Can capture
        output.write(frame)

        # Detect Face
        detectFace(frame)

        # show frame
        cv2.imshow(imshow_str, frame)

        # Exit by pressing key e
        if cv2.waitKey(1) == ord('e'):
            break

# After completed monitoring
# release resource
camera.release()
output.release()
# destroy windows
cv2.destroyAllWindows()






