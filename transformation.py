import cv2 as cv
import numpy as np 


img = cv.imread('Photos/park.jpg')
cv.imshow('PARK',img)


#Translation

def translate(img,x,y):
    transmet = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmet,dimensions)


# -x --->left
# -y --->Up

translatd = translate(img,100,100)
cv.imshow('translated',translatd)


#rotation

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)


    return cv.warpAffine(img,rotMat,dimensions)

roated = rotate(img,45)

cv.imshow('Rotated',roated)

#resizing

cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

#flip

flip = cv.flip(img,0)

#  0-->flip vertically
#  1--->flip horizintally
#  -1--->verically as well as horizontally





#cropping


cropped = img[200:400,300:400]



    


cv.waitKey(0)