import cv2
import numpy as np

cam = cv2.VideoCapture(1)
index = 0
flagPressedC = False
while True:
	img = cam.read()[1]
	keypress = cv2.waitKey(1)
	if keypress == ord('c'):
		flagPressedC = not flagPressedC
	if flagPressedC:
		if np.random.randint(1, 10) in (5, 9):
			cv2.imwrite('unlabelled_images/image%d.jpg'%(index,), img)
			index += 1
	cv2.imshow('img', img)