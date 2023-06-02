import cv2
import time
import threading


class RGBCamThread(threading.Thread):

    def __init__(self, ):
        threading.Thread.__init__(self)

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow('RGB WebCam', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
               break
        cap.release()
        cv2.destroyAllWindows()


class HSVCamThread(threading.Thread):

    def __init__(self, ):
        threading.Thread.__init__(self)

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('HSV WebCam', hsv_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()



