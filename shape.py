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
	print colors(bgr[0],bgr[1],bgr[2])	
	
	# DRAWING CONTOURS
	cv2.drawContours(img, [c], -1, (0, 0, 255), 3)	

cv2.imshow('img', img)		 

cv2.waitKey(0)
cv2.destroyAllWindows()
