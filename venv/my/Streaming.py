# pip install flask imutils
from flask import Flask, render_template, Response, stream_with_context
from imutils.video import VideoStream
import platform
import socket
import cv2
# from camera import Camera

# ip 찾기
# Windows, Darwin
if platform.system() == 'Windows' or platform.system() == 'Darwin':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myIp = s.getsockname()[0]
    print("현재 아이피 주소 :", myIp)
    myPort = 8282
    print("실행 포트번호 :", myPort)
else:
    print("Windos or Darwin please")
    exit()

app = Flask(__name__)

# vs = VideoStream(src=0).start()

# capture = cv2.VideoCapture(0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

@app.route('/')
def index():
    return "TEST"

def generate():
    while True:
        # ret, frame = capture.read()
        # yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return "TEST ing ..."
    # return Response(generate(),mimetype='multipart/x-mixed-replace; boundary=frame')

# ip, port check
if __name__ == '__main__':
    app.run(host=myIp, port=myPort, debug=True, threaded=True)