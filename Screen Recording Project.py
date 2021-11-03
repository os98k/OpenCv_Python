
#Screen Recorder ---

import cv2 as c
import numpy as np
import pyautogui as p


rs = p.size() #Create resolution

fn = input("Enter any file name and path") #Filename to store file and path

fps = 60.0 #foot per second

fourcc = c.VideoWriter_fourcc(*"XVID") ## *"XVID" It contain 4 parameter , name, codec,fps,resolution

output = c.VideoWriter(fn, fourcc, fps, rs)

c.namedWindow("LiveRecording", c.WINDOW_NORMAL)

c.resizeWindow("LiveRecording", (600,450))

while True:
    img = p.screenshot() #p is pyautogui library
    f = np.array(img) #np is numpy library
    
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    
    output.write(f)
    c.imshow("LiveRecording",f)
    if c.waitKey(1) == 27:
        break

output.release()    
c.destroyAllWindows()