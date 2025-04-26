import cv2 as cv



img = cv.imread('Photos/group 1.jpg')





gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)


print(f'Number of faces found = {len(faces_rect)}')


for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
    # cv.putText(img,'Face Detected',(x,y-10),cv.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

cv.imshow('Detected Faces',img)
cv.waitKey(0)