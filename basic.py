import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('cat',img)

#convertin to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray Image',gray)


#Blur an Image

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)


#edge cascade

canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)


#dialating the image

dialated  = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('Dialed',dialated)



#Eroding
eroding = cv.erode(dialated,(3,3),iterations=3)
cv.imshow('Eroded',eroding)


#resize

resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resize)


#croping

cropped = img[50:200,200:400]
cv.imshow('Cropped Image',cropped)






cv.waitKey(0)
