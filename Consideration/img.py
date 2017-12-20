import cv2
import matplotlib.pyplot as plt
import numpy as np
from masking import doMagic
import os


def shape(name, pic):
	fp = open("dataset.csv",'a')
	fp.write(pic+",")
	path, dirs, files = os.walk("./Images").next()
	var = len(files)/3

	# ORIGINAL IMAGE
	img = cv2.imread(name)
	cv2.imshow('img',img)
	
	temp = img.copy()	
	
	# BLUR TO EVEN OUT THE COLOR AND KEEP EDGES CLEAN
	blur = cv2.bilateralFilter(img,9,75,75)

	# COVERTING IT INTO 1 CHANNEL
	blur_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

	# APPLYING THRESHOLD
	ret, img_threshold = cv2.threshold(blur_gray, 150, 255, cv2.THRESH_BINARY_INV)
	cv2.imwrite(str(var)+"_threshold.png",img_threshold)
	cv2.imshow("bin", img_threshold)	

	# FINDING THE NUMBER OF CONTOURS
	cnt, h = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	print('Number of objects = '+str(len(cnt)))	

	c = max(cnt, key = cv2.contourArea)
	
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
	
	fp.write(str(shape)+",")
	area = cv2.contourArea(c)
	#cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	red,green,blue,yellow,pink,orange,cyan,gray,black = doMagic(img[y:y+h, x:x+w])
	cv2.imshow("small", img[y:y+h, x:x+w])
	rect = cv2.minAreaRect(c)

	print "Dimensions = "+str(rect[1])
	fp.write(str(rect[1])+",")

	total_area = max(area,red+green+blue+yellow+pink+orange+cyan+gray+black)

	print "area = "+str(total_area)
	fp.write(str(total_area)+",")
	
	
	
	
	print "black = "+str(black)
	fp.write(str(black)+",")

	print "blue = "+str(blue)
	fp.write(str(blue)+",")

	print "cyan = "+str(cyan)
	fp.write(str(cyan)+",")

	print "gray = "+str(gray)
	fp.write(str(gray)+",")

	print "green = "+str(green)
	fp.write(str(green)+",")

	print "orange = "+str(orange)
	fp.write(str(orange)+",")

	print "pink = "+str(pink)
	fp.write(str(pink)+",")

	print "red = "+str(red)
	fp.write(str(red)+",")	

	print "yellow = "+str(yellow)
	fp.write(str(yellow)+"\n")

	
	fp.close()
	
	
	cv2.imwrite(str(var)+"_contour.png",temp)	
	name = str(var)+".png"
	cmd = "mv img.png "+name
	os.system(cmd)
	cmd = "mv "+name+" Images"
	os.system(cmd)
	cmd = "mv "+str(var)+"_threshold.png Images"
	os.system(cmd)
	cmd = "mv "+str(var)+"_contour.png Images"
	os.system(cmd)

	cv2.waitKey(0)
	cv2.destroyAllWindows()




