import cv2
import numpy as np
from calc_area import calc_area

def mask_black(hsv):

	lower_black = np.array([0,0,0])
	upper_black = np.array([0,30,60])

	# Threshold the HSV image to get only black colors
	mask = cv2.inRange(hsv, lower_black, upper_black)
	area = calc_area(mask)
	return area
