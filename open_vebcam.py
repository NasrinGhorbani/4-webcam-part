import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

width = int(width)
height = int(height)
#print(width, height)

while True:
	ret, frame = cap.read()
	#print(frame.shape)
	#quit()

	if ret:
		# RBG part
		frame = cv2.flip(frame, 1)
		frame1 = frame.copy()
		#frame1 = frame1.reshape((480, 640, 1))

		# Gray Part
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = gray.reshape((height, width, 1))
		gray = np.concatenate([gray, gray, gray], 2)
		#print(gray.shape)
		
		# Inv Part
		frame3  = 255 - frame

		# Red Part
		frame[: , : ,2] = 255


		my_webcam_1 = np.concatenate([frame1 , frame], 1)
		my_webcam_2 = np.concatenate([frame3 , gray], 1)

		my_webcam = np.concatenate([my_webcam_1 , my_webcam_2], 0)

		my_webcam = cv2.resize( my_webcam ,(1100, 700))

		cv2.imshow("my webcam", my_webcam)

		q = cv2.waitKey(1)

		if q == ord('q'):
			break

cv2.destroyAllWindows() 
cap.release()