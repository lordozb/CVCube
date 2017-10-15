import cv2
import numpy as np 

def doMagic(pic):
	img = cv2.imread(pic)
	cv2.imshow('original', img)

	med_blur = cv2.medianBlur(img, 5)
	cv2.imshow('median', med_blur)

	hsv = cv2.cvtColor(med_blur, cv2.COLOR_BGR2HSV)

	# Call a function here which will contain all the mask for the image and will apply
	# it one by one to check which all colors are present in the image.

	lowerBound=np.array([33,80,40])
	upperBound=np.array([102,255,255])
	
	mask=cv2.inRange(hsv,lowerBound,upperBound)

	kernelOpen=np.ones((5,5))
	kernelClose=np.ones((20,20))


	maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
	maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

	maskFinal=maskClose

	conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	for i in range(len(conts)):
		x,y,w,h=cv2.boundingRect(conts[i])
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
		print cv2.contourArea(conts[i])
		
	cv2.imshow("maskClose",maskClose)	
	
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	
	import sys
	name = sys.argv[1]
	doMagic(name)
