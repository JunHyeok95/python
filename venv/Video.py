import cv2
import numpy
from pprint import pprint
# video_file_path = './myVideo.avi' # 저장 경로
# capture = cv2.VideoCapture(video_file_path)

one = True
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,400) # 가로
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300) # 세로
time, xy = 0, 0

# 얼굴찾기
def detect(frame):
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
	faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10, minSize=(50, 50), flags = cv2.CASCADE_SCALE_IMAGE)
	if type(faces) == numpy.ndarray:
		global xy, time
		xy, time = faces, 15
	pprint(xy)
	time -= 1
	print(time)
	if time < 0:
		xy = 0
	if time > 0:
		for (x, y, w, h) in xy:
			cv2.rectangle(frame, (x, y), (x+w, y+h), color = (255, 0, 0), thickness = 5)
	return frame

while True:
	ret, frame = capture.read()
	canvas = detect(frame)
	cv2.imshow("VideoFrame", canvas)
	if one == True:
		cv2.moveWindow("VideoFrame", 100, 100)
		one = False
	if cv2.waitKey(1) > 0:
		break
	
capture.release()
cv2.destroyAllWindows()