import cv2
import numpy as np
from calc_area import calc_area

def mask_pink(hsv):

	lower_pink = np.array([140,100,100])
	upper_pink = np.array([170,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_pink, upper_pink)
	area = calc_area(mask)
	return area
