import cv2
import numpy

img = cv2.imread('dobby.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()