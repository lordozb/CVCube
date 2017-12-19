import cv2
import numpy as np
from calc_area import calc_area

def mask_orange(hsv):

	lower_orange = np.array([2,100,100])
	upper_orange = np.array([22,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_orange, upper_orange)
	area = calc_area(mask)
	return area
