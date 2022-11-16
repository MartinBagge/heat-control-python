import cv2
import time
import numpy as np

def analyze_frame(frame):
    avg = np.sum(frame)/(frame.shape[0]*frame.shape[1])
    if avg < 50:
        return 0
    return 1

def record(queue, source):
    while True:
        time_start = time.time()
        (_, img) = source.read()
        grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res = analyze_frame(grayFrame)
        print(res)
        queue.put(res)
        time.sleep(0.5-(time.time()-time_start))


def start_recording(queue):
    source = cv2.VideoCapture(0)
    source.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    source.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    source.set(cv2.CAP_PROP_FPS, 2)
    record(queue, source)