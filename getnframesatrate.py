import leap
import numpy as np
import time


class MyListener(leap.Listener):
    def __init__(self, max_frames=600, sample_rate=120):
        super().__init__()
        self.max_frames = max_frames
        self.sample_rate = 1.0 / sample_rate  # Interval in seconds
        self.data = []  # List to store collected frames
        self.start_time = time.time()
        self.frame_count = 0  # Keep track of frames collected

    def on_tracking_event(self, event):
        """Collects tracking data at a fixed sampling rate."""
        if self.frame_count >= self.max_frames:
            return  # Stop collecting once we have enough frames

        current_time = time.time() - self.start_time  # Get relative timestamp
        right_hand = next((hand for hand in event.hands if str(hand.type) == "HandType.Right"), None)

        if right_hand:
            palm_pos = right_hand.palm.position
            index_finger = next((f for f in right_hand.fingers if str(f.type) == "FingerType.Index"), None)

            if index_finger:
                index_tip = index_finger.tip_position
                frame_data = [
                    current_time,            # Time since start
                    palm_pos.x, palm_pos.y, palm_pos.z,  # Palm position
                    index_tip.x, index_tip.y, index_tip.z  # Index fingertip position
                ]
                self.data.append(frame_data)
                self.frame_count += 1
                print(f"Frame {self.frame_count}: Time {current_time:.2f}s, Palm {palm_pos}, Index {index_tip}")

                # Sleep to match sampling rate
                time.sleep(self.sample_rate)

    def get_numpy_data(self):
        """Converts the collected data into a NumPy array."""
        return np.array(self.data)


def collect_frames(max_frames=600, sample_rate=120, save_path="leap_motion_data.npy"):
    """Connects to the Leap Motion controller, collects frames, and saves them to a file."""
    my_listener = MyListener(max_frames, sample_rate)
    connection = leap.Connection()
    connection.add_listener(my_listener)

    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)

        # Wait until we collect enough frames
        while my_listener.frame_count < max_frames:
            time.sleep(0.01)  # Avoid excessive CPU usage

    # Convert collected data to NumPy array
    data_array = my_listener.get_numpy_data()

    # Save to file
    np.save(save_path, data_array)
    print(f"Data saved to {save_path}")

    return data_array


if __name__ == "__main__":
    collected_data = collect_frames(sample_rate=120)  # Set sampling rate to 120 Hz
    print("Final Shape of Data:", collected_data.shape)  # Should be (600, 7)
