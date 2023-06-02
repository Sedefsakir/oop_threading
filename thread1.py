import cv2
import time
import threading
from webcam import RGBCamThread
from webcam import HSVCamThread

def test_webcam_threads():
    rgb_thread = RGBCamThread()
    rgb_thread.start()

    time.sleep(2)

    cv2.destroyAllWindows()

    hsv_thread = HSVCamThread()
    hsv_thread.start()

    rgb_thread.join()
    hsv_thread.join()

test_webcam_threads()

cv2.waitKey(0)
