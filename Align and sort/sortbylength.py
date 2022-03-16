import cv2 #importing opencv
import numpy as np #importing numpy
import math #importing math
from operator import itemgetter #we use this model to sort our list
img = cv2.imread('qn.jpg') # read image
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert default BGR to grayscale
_,frame = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY) # this functions turns the intensity to pure black or pure white

def my_func(image):
    temp = []
    contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours from the image argument
    for i in contours: #loop through our detected contours
        area = cv2.contourArea(i) #find area of the contour
        (x,y,width,height) = cv2.boundingRect(i) #get the parameters of the bounding rectangle of the contour
        if area > 500 and cv2.contourArea(i) < 1500: #only selects the contours with this area range
            cv2.rectangle(img,(x,y),(x+width,y+height),(255,0,0),1)
            rect = cv2.minAreaRect(i) #get the rotated rectangle box that contain our contour
            print(rect[2])
            box = cv2.boxPoints(rect) # get 4 points of the rectangle box
            (x1,y1) = (int(box[0][0]),int(box[0][1]))
            (x2,y2) = (int(box[1][0]),int(box[1][1]))
            (x3,y3) = (int(box[2][0]),int(box[2][1]))
            (x4,y4) = (int(box[3][0]),int(box[3][1]))
            cv2.line(img,(x1,y1),(x3,y3),(255,0,0),2) #draw a diagonal line to approximate it as the detected line
            x = [(x1,y1),rect[2],area] #create a list and append it in temporary list to further return it
            temp.append(x)
    temp = sorted(temp,key=itemgetter(2)) #this sorts our list on the basis of bounding rectangle area
    # so the longest line will have the largest bounding area and we can easily sort it.
    return temp #returns our list

list = my_func(frame) #this function returns a list with [starting coodrinate ,bounding rectangle area]
for i in range(0,len(list)): #loop through the list to display their number order
    cv2.putText(img,str(i+1),list[i][0],cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)

cv2.imshow('window2',img)
cv2.imshow('window',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
