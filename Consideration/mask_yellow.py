import cv2
import numpy as np
from calc_area import calc_area

def mask_yellow(hsv):

	lower_yellow = np.array([20,100,100])
	upper_yellow = np.array([30,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	area = calc_area(mask)
	return area
