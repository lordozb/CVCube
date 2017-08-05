import cv2
import numpy as np
from img import shape

cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 1) 
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 360)
count = 0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	cv2.imshow('frame',frame)

	if count % 100 == 0:
		cv2.imwrite('img.png',frame)

	text = shape()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()	
