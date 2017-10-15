lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])
mask=cv2.inRange(hsv,lowerBound,upperBound)
