import cv2

CAM_ID = 0 # 카메라 번호
MOSAIC_RATE = 25 # 모자이크 율

# 실시간 비디오
capture = cv2.VideoCapture(CAM_ID)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640) # 가로
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # 세로

# 얼굴찾기
def detect(frame):
    # 그레이를 이용해서 프레임을 변환시킨다.
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 10, minSize=(50, 50), flags = cv2.CASCADE_SCALE_IMAGE)
    # 변환
    for (x, y, w, h) in faces:
        # 사각형
        cv2.rectangle(frame, (x, y), (x+w, y+h), color = (255, 0, 0), thickness = 5)
        # 모자이크
        try:
            face_img = frame[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (w//MOSAIC_RATE, h//MOSAIC_RATE))
            face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
            frame[y:y+h, x:x+w] = face_img
        except Exception as e:
            print(str(e))
    return frame

while True:
    ret, frame = capture.read()
    # 그리기
    canvas = detect(frame)
    # 이미지 출력
    cv2.imshow("VideoFrame", canvas)
    if cv2.waitKey(1) > 0:
        break

capture.release()
cv2.destroyAllWindows()