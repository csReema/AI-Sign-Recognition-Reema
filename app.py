"""
AI Sign Language Recognition (starter demo)
Recognizes a small set of static hand gestures using MediaPipe landmarks.
This is a gesture demo, not a full sign-language translator.
"""

import cv2
import mediapipe as mp
import math

CAMERA_INDEX = 0

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def finger_is_up(landmarks, tip_id, pip_id):
    # For a mirrored webcam image, fingertip above its middle joint usually means raised.
    return landmarks[tip_id].y < landmarks[pip_id].y

def classify_gesture(hand):
    lm = hand.landmark

    index_up = finger_is_up(lm, 8, 6)
    middle_up = finger_is_up(lm, 12, 10)
    ring_up = finger_is_up(lm, 16, 14)
    pinky_up = finger_is_up(lm, 20, 18)

    # Thumb check is approximate and depends on hand orientation.
    thumb_open = abs(lm[4].x - lm[2].x) > 0.06

    if index_up and middle_up and ring_up and pinky_up:
        return "OPEN HAND"
    if index_up and not middle_up and not ring_up and not pinky_up:
        return "ONE FINGER"
    if index_up and middle_up and not ring_up and not pinky_up:
        return "TWO FINGERS"
    if not index_up and not middle_up and not ring_up and not pinky_up and not thumb_open:
        return "CLOSED FIST"
    if thumb_open and not index_up and not middle_up and not ring_up and not pinky_up:
        return "THUMB GESTURE"
    return "GESTURE NOT RECOGNIZED"

def main():
    camera = cv2.VideoCapture(CAMERA_INDEX)
    if not camera.isOpened():
        print("Could not open webcam. Check camera permissions and CAMERA_INDEX.")
        return

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6,
    ) as hands:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Could not read webcam frame.")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            label = "Show one hand to the camera"
            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                label = classify_gesture(hand)

            cv2.rectangle(frame, (10, 10), (frame.shape[1] - 10, 80), (30, 30, 30), -1)
            cv2.putText(frame, "AI Sign Language Recognition - Gesture Demo",
                        (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.58, (255, 255, 255), 2)
            cv2.putText(frame, f"Detected: {label}",
                        (20, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, "Press Q to quit", (20, frame.shape[0] - 18),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.imshow("AI Sign Language Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
