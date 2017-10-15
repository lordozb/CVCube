import cv2
import numpy as np
from calc_area import calc_area

def mask_red(hsv):

	# lower mask (0-10)
	lower_red = np.array([0,50,50])
	upper_red = np.array([10,255,255])
	mask0 = cv2.inRange(hsv, lower_red, upper_red)

	# upper mask (170-180)
	lower_red = np.array([170,50,50])
	upper_red = np.array([180,255,255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)

	# join my masks
	mask = mask0+mask1
	area = calc_area(mask)	

	return area
