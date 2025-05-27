# Gesture as Enhancement of Online Education

This project allows users to control software functions via hand gestures using the **Leap Motion** controller. Recognized gestures are mapped to keyboard shortcuts using Python.

## 🔧 Features

- Real-time hand gesture recognition using Leap Motion
- Maps gestures to specific keyboard actions
- Lightweight, extensible, and easy to customize
- Includes five basic gestures: fist, open hand, two fingers, point, and thumbs-up

## 🧠 How It Works

1. **Detect Gestures**: The Leap Motion sensor tracks the hand and finger positions.
2. **Classify Intent**: The system classifies the hand pose into predefined gesture categories.
3. **Trigger Action**: Recognized gestures are mapped to keyboard shortcuts and executed using `pynput`.

## ✨ Supported Gestures

| Gesture        | Description           | Keyboard Trigger |
|----------------|------------------------|------------------|
| Fist           | All fingers folded     | `Space`          |
| Open Hand      | All fingers extended   | `a`              |
| Two Fingers    | Index + Middle         | `b`              |
| Point          | Only index finger      | `c`              |
| Thumbs-Up      | Only thumb extended    | `d`              |

## 🧰 Requirements

- Python 3.6+
- [Leap Motion SDK](https://developer.leapmotion.com/sdk)
- `pynput` Python package

Install dependencies:

```bash
pip install pynput
