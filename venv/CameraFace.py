import cv2

faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_eye.xml')

# 실시간 비디오
capture = cv2.VideoCapture(0)

# 얼굴찾기
def detect(gray, frame):
    # 얼굴 찾기
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5, minSize=(150,150), flags = cv2.CASCADE_SCALE_IMAGE)
    # 얼굴에 사각형 찾기
    for (x, y, w, h) in faces:
        # 얼굴 : 이미지에서 x,y 시작 , x+w , y+h 로 사각형 그림
        # rectangle(프레임, 포인트, 크기, 색, 굵기)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 얼굴 크기 만큼 잘라서 스레이스케일 이미지, 컬러 이미지 생성
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]
        # 눈에 사각형 처리
        eyes = eyeCascade.detectMultiScale(face_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
    return frame

while True: # 출력 반복
    ret, frame = capture.read() # ret 카메라의 상태, frame 프레임 받아옴
    # 이미지를 스레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # 사각형 칠해진 프레임
    canvas = detect(gray, frame)
    cv2.imshow("VideoFrame", canvas) # cv2 이용 윈도우 창 보기 (제목, 이미지)
    if cv2.waitKey(1) > 0: # 키입력이 있을 때 까지 반복
        break # waitKey(1) == ord('특정 키') 종료키 설정가능

# 종료
capture.release()
cv2.destroyAllWindows()