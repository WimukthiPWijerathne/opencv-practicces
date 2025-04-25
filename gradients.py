import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#laplacian


lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#sobel

sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
cv.imshow('Sobel X',sobelx)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('Sobel Y',sobely)


combbined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Combined Sobel',combbined_sobel)

cv.waitKey(0)
