import cv2
import numpy as np
import datetime
#cap = cv2.VideoCapture("D://video//Si.mp4")
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("for width", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fro width",cap.get(3))
print("fro heigth",cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = cv2.resize(frame,(250,250))
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = "height" + str(cap.get(3)) + "width" + str(cap.get(4))
        frame= cv2.putText(frame, text, (10,20), font, 1, (0,120,0), 1, cv2.LINE_AA)
        date_data = "Date: "+str(datetime.datetime.now())
        #date_data = "date: "+ str(datetime.datetime.now())
        frame= cv2.putText(frame, date_data, (20,50), font, 1, (0,120,0), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) ==27:
        #if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()
