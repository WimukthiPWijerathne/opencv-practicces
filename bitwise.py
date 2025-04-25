import cv2 as cv
import numpy as np



blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)


#bitwise AND

bitwise_and = cv.bitwise_and(rectangle,circle)
#return the intersection of the two shapes

#bitwise OR

bitwise_or = cv.bitwise_or(rectangle,circle)


#bitwise XOR

#use for showing the non intersecting area

bitwise_xor = cv.bitwise_xor(rectangle,circle)


#bitwise NOT

bitwise_not = cv.bitwise_not(circle)
#return the inverse of the shape



cv.waitKey(0)