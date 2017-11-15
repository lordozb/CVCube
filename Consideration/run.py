import cv2
from img import shape

cap = cv2.VideoCapture(0)
count = 0
while True:
	count += 1
	ret,frame = cap.read()
	cv2.imwrite('img.png',frame)
	if count > 10:
		cap.release()
		cv2.destroyAllWindows()
		break

shape('3.jpeg')
