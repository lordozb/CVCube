import cv2
import numpy as np
from mask_green import mask_green
from mask_blue import mask_blue
from mask_red import mask_red
 

def doMagic(img):

	#cv2.imshow('original', img)

	med_blur = cv2.medianBlur(img, 5)
	cv2.imshow('median', med_blur)

	hsv = cv2.cvtColor(med_blur, cv2.COLOR_BGR2HSV)
	
	red = mask_red(hsv)
	green = mask_green(hsv)
	blue = mask_blue(hsv)

	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return red,green,blue
