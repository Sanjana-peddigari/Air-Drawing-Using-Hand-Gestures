# Air-Drawing-Using-Hand-Gestures✋🎨

Draw in the air using hand gestures with real-time hand tracking powered by Python, OpenCV, and MediaPipe.


## Features

- ✋ Real-time hand tracking with all 21 hand landmarks.
- 🖊️ **Pinch** (thumb + index finger) to draw in the air
- 🎨 8 colors, selectable from a vertical color bar on the right
- 🗑️ Clear canvas
- Smooth Cursor Movement

## Demo Controls

| Action | How |
|---|---|
| Draw | Pinch thumb + index finger together, move your hand |
| Change color | Point your index finger at a circle in the right-side bar |
| Clear canvas | press `C` / `Space` |
| Quit | Press `Q` or `Esc` |

## Project Structure

```
air-draw/
├── main.py          # Camera loop, pinch detection, drawing logic
├── hand.py           # MediaPipe hand tracking (21 landmark points)
├── colors.py          # Color palette + color bar UI
├── requirements.txt
└── README.md
```

## Installation

> **Note:** MediaPipe currently supports Python **3.8 – 3.11**. If you're on a newer version, use a 3.12 virtual environment.

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/air-draw.git
   cd air-draw
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

A webcam window titled **"Air Draw"** will open. Show your hand to the camera and start drawing!

## How It Works

- **`hand.py`** uses MediaPipe's Hands solution to detect 21 landmarks per hand and draws the skeleton overlay each frame.
- **`colors.py`** stores colors as a simple name → BGR dict and renders them as circles along the right edge of the frame; it also hit-tests the fingertip position against each circle.
- **`main.py`** ties it together: it tracks the index fingertip and thumb tip, measures the pinch distance to decide when to draw, and merges the persistent drawing canvas onto the live camera feed each frame.

## Requirements

See [requirements.txt](requirements.txt):
- `opencv-python`
- `mediapipe`
- `numpy`
