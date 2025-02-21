""" Example of tracking event usage with the Leap Motion Python SDK. 
This script is basically me learning how to get data from the Leap Motion
and store it in a way that I can use it later. e.g. as numpy arrays.

This script is based on the tracking_event_example.py script from leapc-python-bindings
and the tracking_event_example_lkc.py script from leapc-python-api.
"""

import leap
import numpy as np


class MyListener(leap.Listener):
    def __init__(self):
        super().__init__()
        self.right_palm_position = None  # To store the right hand's palm position

    def on_tracking_event(self, event):
        """ Collects a single frame of tracking data and extracts the right palm position. """
        for hand in event.hands:
            if str(hand.type) == "HandType.Right":  # Check if it's the right hand
                self.right_palm_position = np.array(
                    [hand.palm.position.x, hand.palm.position.y, hand.palm.position.z]
                )
                print(f"Right palm position captured: {self.right_palm_position}")
                return  # Stop after collecting the first valid frame


def collect_right_hand_position():
    """ Connects to the Leap Motion controller and collects a single frame's right palm position. """
    my_listener = MyListener()
    connection = leap.Connection()
    connection.add_listener(my_listener)
 
    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)

        # Wait for a frame to be collected
        while my_listener.right_palm_position is None:
            pass  # Keep waiting until data is captured

    return my_listener.right_palm_position


if __name__ == "__main__":
    right_hand_position = collect_right_hand_position()
    print("Stored Right Palm Position as NumPy Array:", right_hand_position)
