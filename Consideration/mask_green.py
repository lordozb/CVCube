import cv2
import numpy as np
from calc_area import calc_area

def mask_green(hsv):	
	lowerBound=np.array([33,80,40])
	upperBound=np.array([102,255,255])
	mask=cv2.inRange(hsv,lowerBound,upperBound)
	
	area = calc_area(mask)
	return area


