# Gesture recognition using Leap Motion and keyboard shortcuts
# Dependencies: Leap SDK, pynput, OpenCV (optional)

import Leap
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

# Mapping of gesture names to keyboard shortcuts
gesture_to_key = {
    "fist": Key.space,
    "open_hand": 'a',
    "two_fingers": 'b',
    "point": 'c',
    "thumb_up": 'd'
    # Extend as needed
}

class LeapListener(Leap.Listener):
    def on_connect(self, controller):
        print("Connected to Leap Motion")

    def on_frame(self, controller):
        frame = controller.frame()
        hands = frame.hands

        for hand in hands:
            gesture = self.identify_gesture(hand)
            if gesture and gesture in gesture_to_key:
                print(f"Recognized gesture: {gesture}, triggering key: {gesture_to_key[gesture]}")
                self.trigger_key(gesture_to_key[gesture])
                time.sleep(1)  # Debounce

    def identify_gesture(self, hand):
        fingers = hand.fingers
        extended_fingers = [f for f in fingers if f.is_extended]
        count = len(extended_fingers)

        if count == 0:
            return "fist"
        elif count == 5:
            return "open_hand"
        elif count == 2:
            return "two_fingers"
        elif count == 1:
            return "point"
        elif hand.thumb.is_extended and count == 1:
            return "thumb_up"
        else:
            return None

    def trigger_key(self, key):
        keyboard.press(key)
        keyboard.release(key)

if __name__ == "__main__":
    listener = LeapListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    print("Press Ctrl+C to quit")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        controller.remove_listener(listener)
