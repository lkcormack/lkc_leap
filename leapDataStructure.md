How Data is Structured in Leap Motion (Python Bindings)
Events (leap.Event)

These are triggered by Leap Motion and sent to the listener methods.
Example: on_tracking_event(event) fires when a new frame of tracking data arrives.
Tracking Event (event in on_tracking_event)

Each tracking event contains data for one frame.
It has properties like:
event.tracking_frame_id: The unique ID for that frame.
event.hands: A list of Hand objects.
Hand (hand in event.hands)

This contains all the data for an individual hand.
Properties include:
hand.palm.position.x, .y, .z: The palm's position in 3D space.
hand.fingers: A list of Finger objects.
Finger (finger in hand.fingers)

Represents a single finger.
Properties include:
finger.tip_position.x, .y, .z: The position of the fingertip.
🔹 Summary: There is NO Frame Class
Unlike the older Leap Motion SDKs (which had a Frame class in Leap Motion V2/V3), the Python bindings of LeapC don't explicitly have a Frame class. Instead:

Each tracking event is effectively a frame.
The event contains a list of hands.
Each hand contains palm and finger data.