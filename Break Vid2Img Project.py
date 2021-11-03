 

#Break Video into Multiple Images and store in a folder
"""
#To capture only one frame
import cv2

Vidcap = cv2.VideoCapture("D://video//hello.mp4")
ret, image =  Vidcap.read() #Read the Video
count = 0
while True:
    if ret == True:
        
        cv2.imshow("res", image)
        
        count += 1
        if cv2.waitKey(1) == 27:
            break
            cv2.destroyAllWindows()

Vidcap.release()
cv2.destroyAllWindows()
"""

import cv2

Vidcap = cv2.VideoCapture("D://video//hello.mp4")
ret, image =  Vidcap.read() #Read the Video
count = 0
while True:
    if ret == True:
        cv2.imwrite("D:\\frames\\imgN%d.jpg"%count,image)
        Vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = Vidcap.read()
        cv2.imshow("res", image)
        
        
        count += 1
        if cv2.waitKey(1) == 27:
            break
            cv2.destroyAllWindows()

Vidcap.release()
cv2.destroyAllWindows()