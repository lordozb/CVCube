import cv2
import numpy as np
from calc_area import calc_area

def mask_yellow(hsv):

	lower_blue = np.array([20,100,100])
	upper_blue = np.array([30,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	area = calc_area(mask)
	return area
