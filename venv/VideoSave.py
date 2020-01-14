import cv2

CAM_ID = 0 # 카메라 번호
storage_path = './Video/' # 저장 경로

# 실시간 비디오
capture = cv2.VideoCapture(CAM_ID)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640) # 가로
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # 세로

# 화면 사이즈
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# XVID 코덱으로 지정 Four Character Code
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# OUT 설정 파일명, 코덱, 프레임 수, 사이즈
out = cv2.VideoWriter(storage_path + 'myVideo.avi', fourcc, 30.0, (width,height))

while True:
    ret, frame = capture.read()
    # 작성
    out.write(frame)
    # 출력
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0:
        break

# 끄기
out.release()
capture.release()
cv2.destroyAllWindows()