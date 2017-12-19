import cv2
import numpy as np
from calc_area import calc_area

def mask_purple(hsv):

	lower_purple = np.array([140,100,100])
	upper_purple = np.array([160,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_purple, upper_purple)
	area = calc_area(mask)
	return area
