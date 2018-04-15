import cv2
import numpy as np
from calc_area import calc_area

def mask_cyan(hsv):

	lower_blue = np.array([80,100,100])
	upper_blue = np.array([100,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	area = calc_area(mask)
	cv2.imshow("cyan",mask)
	return area
