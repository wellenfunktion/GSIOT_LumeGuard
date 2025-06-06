def is_hand_raised(landmarks):
    if not landmarks:
        return False
    wrist_y = landmarks[0][1]
    fingertips_y = [landmarks[i][1] for i in [8, 12, 16, 20]]
    return all(finger_y < wrist_y for finger_y in fingertips_y)
