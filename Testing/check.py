import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:	
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_orange = np.array([0,0,70])
	upper_orange = np.array([0,0,255])
	mask = cv2.inRange(hsv, lower_orange, upper_orange)
	cv2.imshow("hsv",hsv)
	cv2.imshow("frame", mask)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
