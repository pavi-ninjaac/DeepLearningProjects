import cv2
import mediapipe as mp

vedio_capture = cv2.VideoCapture(0)

class hand_detector:
    """
    This will detect 20 points of hands in the image/video stream with the help of
    mediapipe(a build-in python package for hand tracking/detecting).
    """
    def __init__(self, static_image_mode=False, max_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """
        """
        self.mp_hand = mp.solutions.hands
        self.hands = self.mp_hand.Hands(static_image_mode, max_hands, min_detection_confidence, min_tracking_confidence)
        self.draw_utils = mp.solutions.drawing_utils
        
        
while -1:
    _,img = vedio_capture.read()

    cv2.imshow("image frame",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vedio_capture.release()
cv2.destroyAllWindows()