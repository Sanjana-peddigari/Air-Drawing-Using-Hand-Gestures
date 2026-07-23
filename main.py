import cv2
import numpy as np
from hand import track
from colors import build_bar, draw_bar, pick, get_color

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
height, width = frame.shape[:2]

canvas = np.zeros((height, width, 3), np.uint8)

color_bar, cell = build_bar(height)

selected_color = "RED"
last_point = None

# Variables for smoothing the cursor
smooth_x, smooth_y = None, None

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame = cv2.addWeighted(
        frame,
        0.15,
        np.full_like(frame, (2, 6, 10)),
        0.85,
        0
    )
    landmarks = track(frame, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if landmarks:
        # Index fingertip
        fx = int(landmarks[8].x * width)
        fy = int(landmarks[8].y * height)

        # Thumb tip
        tx = int(landmarks[4].x * width)
        ty = int(landmarks[4].y * height)

        # Smooth fingertip movement
        if smooth_x is None:
            smooth_x, smooth_y = fx, fy
        else:
            smooth_x += (fx - smooth_x) * 0.4
            smooth_y += (fy - smooth_y) * 0.4

        fx = int(smooth_x)
        fy = int(smooth_y)

        # Check pinch gesture
        is_pinching = np.hypot(fx - tx, fy - ty) < 40

        # Check if finger is over a color
        hovered = pick(color_bar, fx, fy, width)
        if hovered:
            selected_color = hovered
            last_point = None
        elif is_pinching:
            if last_point:
                cv2.line(
                    canvas,
                    last_point,
                    (fx, fy),
                    get_color(selected_color),
                    8
                )
            last_point = (fx, fy)
        else:
            last_point = None

        # Draw fingertip cursor
        cv2.circle(frame, (fx, fy), 8, get_color(selected_color), -1)

    else:
        last_point = None
        smooth_x, smooth_y = None, None

    # Overlay drawing on camera frame
    ink_mask = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY) > 0
    frame[ink_mask] = canvas[ink_mask]

    # Draw color palette
    draw_bar(frame, color_bar, cell, width, selected_color)
    cv2.imshow("Air Draw", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break
    if key == ord('c') or key == ord(' '):
        canvas[:] = 0

cap.release()
cv2.destroyAllWindows()