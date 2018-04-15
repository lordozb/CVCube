import cv2
import numpy as np
from calc_area import calc_area

def mask_green(hsv):	
	lowerBound=np.array([35,50,50])
	upperBound=np.array([90,255,255])
	mask=cv2.inRange(hsv,lowerBound,upperBound)
	cv2.imshow("green",mask)
	area = calc_area(mask)
	return area


