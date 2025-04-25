import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)


#Averaging

#use the averae intensity of the surrounding pixels to smooth the image

average = cv.blur(img,(3.3))


#Gaussian Blur
#less bluring comparing to the averaging method

gass  = cv.GaussianBlur(img,(3,3),0)


#median blur
#use the median of the surrounding pixels to smooth the image.good for reducing the noise
median = cv.medianBlur(img,3)


#Bilateral bluring

bilateral = cv.bilateralFilter(img,5,15,15)



cv.waitKey(0)

