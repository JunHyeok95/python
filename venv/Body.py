import cv2

CAM_ID = 0 # 카메라 번호
# video_file_path = './Video/myVideo.avi' # 저장 경로
one = True # 화면 이동 ... dowhile 없음

# 비디오 선택 / 캠 or 파일
capture = cv2.VideoCapture(CAM_ID)
# capture = cv2.VideoCapture(video_file_path)

# 전신찾기 함수
def detect(frame):
    bodyCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_fullbody.xml')
    bodies = bodyCascade.detectMultiScale(frame)
    # 변환
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color = (255, 0, 0), thickness = 5)
    return frame

while True:
    ret, frame = capture.read()
    if ret == True:
        # 그리기
        canvas = detect(frame)
        # 이미지 출력
        cv2.imshow("VideoFrame", canvas)
        # 화면 이동
        if one == True:
            cv2.moveWindow("VideoFrame", 100, 100)
            one = False
        if cv2.waitKey(1) > 0:
            break
    else:
        print('nono')

capture.release()
cv2.destroyAllWindows()