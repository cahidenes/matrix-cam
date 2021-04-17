import cv2 as cv
import matrixConverter
import time, math

cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FPS, 30)
_ = cam.read()
frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

matrixConverter.init(frame_width, frame_height)

lasttime = time.time()

while True:
    noErrors, raw = cam.read()
    if not noErrors:
        print("some error occured while reading from camera")
        exit(1)

    matrix = matrixConverter.convert(raw)
    cv.imshow('matrix', matrix)
    if cv.waitKey(20) == ord('q'):
        break

    print('FPS:', 1/(time.time()-lasttime))
    lasttime = time.time()

cv.destroyAllWindows()