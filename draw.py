import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype='uint8')##here we give 3 is for the number of colrs
# cv.imshow('Blank',blank)
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('cat',img)



##print the image with certain colour

# blank[:] = 0,255,0  ##make whole of the blank image into the green colour
# cv.imshow('green image',blank)




##drawa a rectangle

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)

cv.imshow('Rectangle',blank)

##draw a circle

cv.circle(blank,(250,250),40,(0,255,0),thickness=2)
cv.imshow('Circle with blnk',blank)



#draw a line

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=2)
cv.imshow("Blank image with line",blank)

#write text on an image

cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
cv.waitKey(0)