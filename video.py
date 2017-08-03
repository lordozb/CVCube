import cv2
from shape import shape

cap = cv2.VideoCapture(0)
count = 0
while True:
	ret, frame = cap.read()
	if ret:
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xff == ord('q'):
			break
	if count == 0:
		cv2.imwrite('img.png', frame)

	count = (count + 1) % 50
	
shape()

cap.release()
cv2.destroyAllWindows()
