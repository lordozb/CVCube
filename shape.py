import cv2
import matplotlib.pyplot as plt
import numpy as np

# ORIGINAL IMAGE
img = cv2.imread('green.png')

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
	x = np.ravel(c)
	x = np.reshape(x,(len(x) / 2 , 2)).T
	bgr = np.array([0,0,0])
	for i in x:		
		px = img[i[0],i[1]]
		bgr = bgr + px

	bgr = bgr / len(x)
	from colors import colors
	color =  colors(bgr[0],bgr[1],bgr[2])	
	
	# DRAWING CONTOURS
	cv2.drawContours(img, [c], -1, (0, 0, 255), 3)
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

	cv2.putText(img, shape+"|"+color, (x + w / 2, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)


cv2.imshow('img', img)		 

cv2.waitKey(0)
cv2.destroyAllWindows()
