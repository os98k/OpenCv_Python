
import cv2saving video using webcam

#Code for 
"""
cap =cv2.VideoCapture(0,cv2.CAP_DSHOW);
print(cap);
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (700,460))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray", gray)
    k= cv2.waitKey(100)
    if k== ord("q") & 0xFF:
        break
    cap.release()
    cv2.destroyAllWindows()

"""

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("cap",cap.isOpened())
fourcc= cv2.VideoWriter_fourcc(*"XVID")
#output = cv2.VideoWriter("D:\\output.avi",fourcc,20.0,(640,480))
output = cv2.VideoWriter("D:\\output.avi",fourcc,20.0,(640,480),0)
while cap.isOpened():
    ret,frame = cap.read()
    #frame = cv2.resize(frame, (700,460))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,0)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    #output.write(frame)
    output.write(gray)
    if cv2.waitKey(1)==27:
        break

cap.release()    
output.release()    
cv2.destroyAllWindows()
