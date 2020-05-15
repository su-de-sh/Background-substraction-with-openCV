import cv2 

camera = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	_,frame = camera.read()

	fgmask = fgbg.apply(frame)
	fgmask = cv2.erode(fgmask,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),3)
	fgmask = cv2.dilate(fgmask,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),2)

	cv2.imshow("original",frame)
	cv2.imshow("mask",fgmask)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

camera.release()
cv2.destroyAllwindows()