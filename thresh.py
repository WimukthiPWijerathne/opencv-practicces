import cv2 as cv


#thresholding is a binarizing a image

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding

threshold,thresh = cv.threshold(gray,150,155,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

#inverse thresholding
threshold,thresh_inv = cv.threshold(gray,150,155,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse',thresh_inv)

#adaptive thresholding
addaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Threshold',addaptive_thresh)



cv.waitKey(0)