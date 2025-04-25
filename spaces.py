import cv2 as cv





img = cv.imread('Photos/park.jpg')
cv.imshow('park',img)


#BGR to gra scal


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#BGR to HSV

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)


#BGR to l*a*b

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


#BGR to RGB

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

cv.waitKey(0)