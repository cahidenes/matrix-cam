import sys
import cv2 as cv
import matrixConverter

if len(sys.argv) != 3:
    print("usage: python3 {} <input_image> <output_image>".format(sys.argv[0]))
    print("example: python3 {} image1.jpg image1_matrixed.jpg")
    exit(1)

input_image = cv.imread(sys.argv[1])
if input_image is None:
   print("{} not exists.".format(sys.argv[1]))
   exit(1)

matrixConverter.init(input_image.shape[1], input_image.shape[0])

output_image = matrixConverter.convert(input_image)
cv.imwrite(sys.argv[2], output_image)
cv.imshow('input', input_image)
cv.imshow('output', output_image)
cv.waitKey()