import numpy as np
import cv2

def calc_area(mask):

	kernelOpen=np.ones((5,5))
	kernelClose=np.ones((20,20))
	maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
	maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
	maskFinal=maskClose

	conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	area = 0

	for i in range(len(conts)):
		x,y,w,h=cv2.boundingRect(conts[i])
		#cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
		area = area + cv2.contourArea(conts[i])
	
	return area
