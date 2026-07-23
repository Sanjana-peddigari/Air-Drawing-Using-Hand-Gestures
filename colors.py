import cv2

COLORS = {
    "BLUE": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "RED": (0, 0, 255),
    "YELLOW": (0, 255, 255),
    "PURPLE": (255, 0, 255),
    "ORANGE": (0, 165, 255),
    "BROWN": (19, 69, 139),
    "WHITE": (255, 255, 255),
}
BAR_WIDTH = 150

def get_color(name):
    return COLORS.get(name, COLORS["BLUE"])

def build_bar(height):
    names = list(COLORS.keys())
    cell = height // len(names)
    bar = []
    for i, name in enumerate(names):
        bar.append((name, i * cell, (i + 1) * cell))
    return bar, cell

def draw_bar(frame, bar, cell, width, selected):
    for name, top, bottom in bar:
        x, y, r = width - BAR_WIDTH // 2, (top + bottom) // 2, cell // 2 - 10
        cv2.circle(frame, (x, y), r, get_color(name), -1)
        if name == selected:
            cv2.circle(frame, (x, y), r + 4, (255, 255, 255), 2)

def pick(bar, finger_x, finger_y, width):
    if finger_x < width - BAR_WIDTH:
        return None
    for name, top, bottom in bar:
        if top <= finger_y < bottom:
            return name
    return None