import numpy as np
import matplotlib.pyplot as plt

# Load the saved NumPy data
data = np.load("leap_motion_data.npy")

# Extract time and position data
time_stamps = data[:, 0]  # First column = time
palm_x, palm_y, palm_z = data[:, 1], data[:, 2], data[:, 3]  # Columns 1-3 = palm position
index_x, index_y, index_z = data[:, 4], data[:, 5], data[:, 6]  # Columns 4-6 = fingertip position

# Create a figure with subplots for Palm and Index Finger
plt.figure(figsize=(12, 6))

# Plot Palm Position
plt.subplot(2, 1, 1)
plt.plot(time_stamps, palm_x, label="Palm X")
plt.plot(time_stamps, palm_y, label="Palm Y")
plt.plot(time_stamps, palm_z, label="Palm Z")
plt.xlabel("Time (s)")
plt.ylabel("Palm Position")
plt.title("Palm Position Over Time")
plt.legend()
plt.grid(True)

# Plot Index Finger Tip Position
plt.subplot(2, 1, 2)
plt.plot(time_stamps, index_x, label="Index X", linestyle="dashed")
plt.plot(time_stamps, index_y, label="Index Y", linestyle="dashed")
plt.plot(time_stamps, index_z, label="Index Z", linestyle="dashed")
plt.xlabel("Time (s)")
plt.ylabel("Index Finger Position")
plt.title("Index Finger Tip Position Over Time")
plt.legend()
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()
