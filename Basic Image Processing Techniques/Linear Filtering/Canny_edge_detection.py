"""
This code shows the steps and the process followed to detect edges in an images

This is an multi step algorithm which follows the steps:

1) Noise reduction using 5x5 guassian filter

2) Finding intensity gradient in both vertical and horizontal direction of the image

3) Non max supression for removing pixels which doesn't contribute to the edge detection

4) Doing Hysteresis Thresholding for maintaining continutaion in the edges
"""

import cv2

#change the directory of the image accordingly
image = cv2.imread('/home/s1th/Documents/Computer-Vision-/test_images/test01.jpg',0)

edges = cv2.Canny(image,75,150,apertureSize=3,L2gradient=False)

# Arguments:
# 1-> input image
# 2-> max and min value
# 3-> Its the apeture size of the sobel kernal (by default it is 3)
# 4-> Last argument is l2 gradient which is false by defualt

cv2.imshow('Edged Image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()