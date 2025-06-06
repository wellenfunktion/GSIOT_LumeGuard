import mediapipe as mp
import cv2

class GestureDetector:
    def __init__(self, detection_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=detection_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gestures(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        landmarks = []
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)
                for lm in handLms.landmark:
                    h, w, _ = frame.shape
                    landmarks.append((int(lm.x * w), int(lm.y * h)))
        return frame, landmarks
