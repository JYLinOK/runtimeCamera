import cv2

# set the camera parameters 

camera_ID = 0

camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

output = cv2.VideoWriter('./video/output.avi', fourcc, 20.0, (660, 500))

frame_gap = 25

imshow_str = '24 HOURS MONITORING'

# start the monitoring
frame_ID = 0

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






