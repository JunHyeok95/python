import cv2

capture = cv2.VideoCapture(0) # 카메라 영상을 받아옴, 내장 카메라 번호 0
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640) # 가로
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # 세로

while True: # 출력 반복
    ret, frame = capture.read() # ret 카메라의 상태, frame 프레임 받아옴
    if ret == False: # 예외처리
        break
    cv2.imshow("VideoFrame", frame) # cv2 이용 윈도우 창 보기 (제목, 이미지)
    if cv2.waitKey(1) > 0: # 키입력이 있을 때 까지 반복
        break # waitKey(1) == ord('특정 키') 종료키 설정가능

capture.release() # 메모리 해제
cv2.destroyAllWindows() # 윈도우 창 종료 cv2.destroyWindow('특정 창') 종료 가능 