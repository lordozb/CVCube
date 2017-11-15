import cv2
import matplotlib.pyplot as plt
import numpy as np
from masking import doMagic


def shape(name):

	# ORIGINAL IMAGE
	img = cv2.imread(name)
	cv2.imshow('img',img)
	
	temp = img.copy()	
	
	# BLUR TO EVEN OUT THE COLOR AND KEEP EDGES CLEAN
	blur = cv2.bilateralFilter(img,9,75,75)

	# COVERTING IT INTO 1 CHANNEL
	blur_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

	# APPLYING THRESHOLD
	ret, img_threshold = cv2.threshold(blur_gray, 120, 255, cv2.THRESH_BINARY_INV)
	
	# FINDING THE NUMBER OF CONTOURS
	cnt, h = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	print('Number of objects = '+str(len(cnt)))

	for c in cnt:
	
		# DRAWING CONTOURS
		cv2.drawContours(temp, [c], -1, (0, 255, 255), 3)
		
		# CALCULATING NUMBER OF SIDES	
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		sides = len(approx)

		x,y,w,h = cv2.boundingRect(c)

		print('I see a :') 	
		shape = ''	

		if sides == 3:
			print 'Triangle'
			shape = 'Triangle'

		elif sides == 4:		
			diff = ((max(w,h) - min(w,h)) / float(min(w,h))) * 100
	
			if diff < 5:
				print 'Square'
				shape = 'Square'
			elif diff > 5:
				print 'Rectangle'
				shape = 'Rectangle'

		elif sides == 7 or sides == 8:
			print 'circle'
			shape = 'Circle'

		else :
			print(str(sides)+" sided figure")
			shape = str(sides)+' sided figure'
		
		area = cv2.contourArea(c)

		#cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		red,green,blue,yellow = doMagic(img[y:y+h, x:x+w])
		cv2.imshow("small", img[y:y+h, x:x+w])
		rect = cv2.minAreaRect(c)
		print "Dimensions = "+str(rect[1])
		print "red = "+str(red)
		print "green = "+str(green)
		print "yellow = "+str(yellow)
		print "blue = "+str(blue)
		cv2.waitKey(0)
		cv2.destroyAllWindows()




