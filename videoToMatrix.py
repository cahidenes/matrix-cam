import cv2 as cv
import matrixConverter
import sys

if len(sys.argv) != 3:
    print("usage: python3 {} <input_video> <output_name>".format(sys.argv[0]))
    print("example: python3 {} video1.mp4 video1_matrixed")
    exit(1)

video = cv.VideoCapture(sys.argv[1])
frame_width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv.CAP_PROP_FPS)

out = cv.VideoWriter('{}.avi'.format(sys.argv[2]), cv.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

matrixConverter.init(frame_width, frame_height)

while True:
    noErrors, raw = video.read()
    if not noErrors:
        print("some error occured while reading from video")
        exit(1)

    matrix = matrixConverter.convert(raw)
    cv.imshow('frame', matrix)
    cv.imshow('input', raw)
    out.write(matrix)
    if cv.waitKey(20) == ord('q'):
        break

video.release()
out.release()

cv.destroyAllWindows()