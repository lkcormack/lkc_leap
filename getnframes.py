import leap
import numpy as np
import time

class MyListener(leap.Listener):
    def __init__(self, max_frames=600):
        super().__init__()
        self.max_frames = max_frames
        self.data = []  # List to store collected frames
        self.start_time = time.time()

    def on_tracking_event(self, event):
        """Collects tracking data for a set number of frames."""
        if len(self.data) >= self.max_frames:
            return  # Stop collecting once we have enough frames

        current_time = time.time() - self.start_time  # Get relative timestamp
        # event.hands is a list of len 0, 1, or 2 ([left], [right], or [left, right]) 
        right_hand = next((hand for hand in event.hands if str(hand.type) == "HandType.Right"), None) # None in case no hand detected

        if right_hand:
            palm_pos = right_hand.palm.position
            index_finger = next((f for f in right_hand.digits if f.finger_id == 1), None)

            if index_finger:
                index_tip = index_finger.distal.next_joint
                frame_data = [
                    current_time,            # Time since start
                    palm_pos.x, palm_pos.y, palm_pos.z,  # Palm position
                    index_tip.x, index_tip.y, index_tip.z  # Index fingertip position
                ]
                self.data.append(frame_data)
                print(f"Frame {len(self.data)}: Time {current_time:.2f}s, Palm {palm_pos}, Index {index_tip}")

    def get_numpy_data(self):
        """Converts the collected data into a NumPy array."""
        return np.array(self.data)


def collect_frames(max_frames=600, save_path="leap_motion_data.npy"):
    """Connects to the Leap Motion controller, collects frames, and saves them to a file."""
    my_listener = MyListener(max_frames)
    connection = leap.Connection()
    connection.add_listener(my_listener)

    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)

        # Wait until we collect enough frames
        while len(my_listener.data) < max_frames:
            print(len(my_listener.data))

    # Convert collected data to NumPy array
    data_array = my_listener.get_numpy_data()

    # Save to file
    np.save(save_path, data_array)
    print(f"Data saved to {save_path}")

    return data_array


if __name__ == "__main__":
    input("Press Enter to start collecting frames...")
    collected_data = collect_frames()
    print("Final Shape of Data:", collected_data.shape)  # Should be (600, 7)
