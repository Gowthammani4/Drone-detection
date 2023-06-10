from flask import Flask, Response,jsonify,request
import cv2

from YOLO_Video import video_detection
app = Flask(__name__)

def generate_frames(path_x = '',):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        _,buffer=cv2.imencode('.jpg',detection_)
        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')
# @app.route("/img")
# def img():
    # return Response(generate_frames(path_x="pic.jpeg"))

@app.route('/video')
def video():
    return Response(generate_frames(path_x='drone_video.mp4'), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/webcam')
def webcam():
    pass
    # return Response(generate_frames(path_x=""), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)