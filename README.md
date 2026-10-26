# AI Sign Language Recognition — Gesture Demo

A beginner-friendly computer-vision demo that uses a webcam and MediaPipe Hands to identify a small set of **static hand gestures**.

## What it recognizes

- Open hand
- One finger raised
- Two fingers raised
- Closed fist (approximate)
- Thumb gesture (approximate)

**Important:** This is a gesture-recognition demo, not a complete sign-language translator. Real sign languages include hand shape, movement, orientation, facial expression, and context. The simple rules in this starter project can misclassify gestures depending on camera angle and hand orientation.

## Requirements

- Python version supported by your installed MediaPipe package
- Webcam

## Setup on macOS

From Terminal, enter the project folder, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If installation fails with Python 3.14, use a Python version supported by the current MediaPipe package for your platform (Python 3.12 is a common fallback), then recreate the virtual environment.

## Run

```bash
python app.py
```

Show one hand to the webcam. The app draws hand landmarks and displays the detected gesture. Press `q` while the webcam window is active to quit.

## macOS permissions

If the camera does not open, allow Terminal or the Python app under **System Settings → Privacy & Security → Camera**.

## Project files

- `app.py` — webcam and gesture classification
- `requirements.txt` — dependencies
- `README.md` — instructions
