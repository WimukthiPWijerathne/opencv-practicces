import cv2 as cv

##reading images

img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):   ##this function is used for resize the frame to a perticular size
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width,height)


    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



# reading video********

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
