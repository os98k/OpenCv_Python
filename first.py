import cv2
"""
image1 = cv2.imread("D:\\New folder (6)\\blog-2.jpg",0)
image1 = cv2.resize(image1, (1280,760))
image1 = cv2.flip(image1,0)
print(image1) 
cv2.imshow("orignal", image1)
cv2.waitKey()
cv2.destroyAllWindows()

image2 = cv2.imread("D:\\New folder (6)\\blog-3.jpg",0)
image2 = cv2.resize(image2, (1280,760))
print("image in grey scale", image2) 
cv2.imshow("grey scale image", image2)
cv2.waitKey()
cv2.destroyAllWindows()

image3 = cv2.imread("D:\\New folder (6)\\blog-4.jpg",-1)
image3 = cv2.resize(image3, (1280,760))
cv2.imshow("Unchanged value", image3)
cv2.waitKey()
cv2.destroyAllWindows()
"""
"""#Image color change to grey scale color
path = input("Enter your path: ")
print("you enter this path: ", path)

image1 = cv2.imread(path,0)
image1 = cv2.resize(image1, (560,700))
print(image1) 
cv2.imshow("orign", image1)
image1 = cv2.flip(image1,1)
k = cv2.waitKey(0)
if k ==ord("s"):
    cv2.imwrite("D:\outpt.png",image1)
else:
    cv2.destroyAllWindows()
    """
"""    
cap = cv2.VideoCapture("D:\\video\\VBC _ Statistical Inference.mp4")
print("cap",cap)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame, (700,460))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)
    if k ==ord("q"):
        break

cap.release()        
cv2.destroyAllWindows()



camera = "https://10.107.2.98:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)

print("cap",cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret ==True:
      frame = cv2.resize(frame, (700,460))
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
      gray = cv2.flip(gray,-1)
      cv2.imshow("gray",gray)
      cv2.imshow("frame",frame)
      
      if cv2.waitKey(1)==27:
         break

cap.release()        
cv2.destroyAllWindows()

"""
cap =cv2.VideoCapture(0);
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















