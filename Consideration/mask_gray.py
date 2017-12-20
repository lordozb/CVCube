import cv2
import numpy as np
from calc_area import calc_area

def mask_gray(hsv):

	lower_gray = np.array([0,0,70])
	upper_gray = np.array([0,0,255])

	# Threshold the HSV image to get only gray colors
	mask = cv2.inRange(hsv, lower_gray, upper_gray)
	area = calc_area(mask)
	return area
