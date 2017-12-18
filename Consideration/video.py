import numpy as np
import cv2
from masking import doMagic

cap = cv2.VideoCapture(1)
count = 0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	if count % 100 == 0:
		cv2.imwrite('img.png',frame)		
		
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# BLUR TO EVEN OUT THE COLOR AND KEEP EDGES CLEAN
	blur = cv2.bilateralFilter(gray,9,75,75)
	ret, thresh_img = cv2.threshold(blur,120,255,cv2.THRESH_BINARY)

	contours, h =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		cv2.drawContours(frame, [c], -1, (0,255,0), 3)

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
	
		cv2.putText(frame, shape, (x + w / 2, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
		

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
