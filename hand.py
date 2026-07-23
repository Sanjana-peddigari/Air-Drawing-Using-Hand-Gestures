import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, model_complexity=1, min_detection_confidence=0.6, min_tracking_confidence=0.6)

def track(frame, image_rgb):
    results = hands.process(image_rgb)
    if not results.multi_hand_landmarks:
        return None
    hand = results.multi_hand_landmarks[0]
    mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
    return hand.landmark