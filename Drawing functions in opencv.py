# Drawing Function in Opencv

"""
import cv2
import numpy as np

img = cv2.imread("D://video//outpt.png")
img = cv2.resize(img, (500,600))
 
#Simple line accept  five parameter 
# (img, starting, ending,color, thickness)

img = cv2.line(img, (0,0),(200,200),(154,92,434),8)

#arroweed line accept five parameter 
# (img, starting, ending,color, thickness)
img = cv2.arrowedLine(img,(0,120),(200,200),(245,7,34),8)

#rectangle accept five parameter 
# (img, starting_co, ending_co,color, thickness)
img = cv2.rectangle(img, (100,100), (200,200),(245,7,34),-1)


#circle accept five parameter 
# (img, starting_co, radius, color, thickness)
img = cv2.circle(img, (100,100), 63,(154,92,434),8)

#puttext accept these parameter 
# (img, starting_co, font,font size, , color, thickness, linetype)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img," 2thor", (30,400),font, 4, (0,154,434), 8, cv2.LINE_AA)

#ellipse accept five parameter 
# (img, starting_co, length,height, color, thickness) 0,0 are rotating point
img = cv2.ellipse(img, (100,100),(100, 63),0,0,360, 155, 8)


cv2.imshow("res", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# Drawing Function in Opencv on blank image


import cv2
import numpy as np

#img = np.zeros([512, 512, 3], np.uint8)*255 #for black screen
img = np.ones([512, 512, 3], np.uint8)*255 #for white screen
#Simple line accept  five parameter 
# (img, starting, ending,color, thickness)

img = cv2.line(img, (0,0),(200,200),(154,92,434),8)

#arroweed line accept five parameter 
# (img, starting, ending,color, thickness)
img = cv2.arrowedLine(img,(0,120),(200,200),(245,7,34),8)

#rectangle accept five parameter 
# (img, starting_co, ending_co,color, thickness)
img = cv2.rectangle(img, (100,100), (200,200),(245,7,34),-1)


#circle accept five parameter 
# (img, starting_co, radius, color, thickness)
img = cv2.circle(img, (100,100), 63,(154,92,434),8)

#puttext accept these parameter 
# (img, starting_co, font,font size, , color, thickness, linetype)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img," 2thor", (30,400),font, 4, (0,154,434), 8, cv2.LINE_AA)

#ellipse accept five parameter 
# (img, starting_co, length,height, color, thickness) 0,0 are rotating point
img = cv2.ellipse(img, (100,100),(100, 63),0,0,360, 155, 8)


cv2.imshow("res", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
