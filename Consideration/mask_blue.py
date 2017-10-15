import cv2
import numpy as np
from calc_area import calc_area

def mask_blue(hsv):

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	area = calc_area(mask)
	return area
