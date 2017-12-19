import cv2
import numpy as np
from mask_green import mask_green
from mask_blue import mask_blue
from mask_red import mask_red
from mask_yellow import mask_yellow 
from mask_purple import mask_purple
from mask_orange import mask_orange

def doMagic(img):

	med_blur = cv2.medianBlur(img, 5)
	#cv2.imshow('median', med_blur)

	hsv = cv2.cvtColor(med_blur, cv2.COLOR_BGR2HSV)
	#cv2.imwrite('hsv.png',hsv)
	red = mask_red(hsv)
	green = mask_green(hsv)
	blue = mask_blue(hsv)
	yellow = mask_yellow(hsv)
	purple = mask_purple(hsv)
	orange = mask_orange(hsv)	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return red,green,blue,yellow,purple,orange
