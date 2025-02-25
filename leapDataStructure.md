# How Data is Structured in Leap Motion (Python Bindings)

## Events (leap.Event)
These are triggered by Leap Motion and sent to the listener methods.

Example: `on_tracking_event(event)` fires when a new frame of tracking data arrives.
Tracking Event (event in on_tracking_event)

Each tracking event contains data for one frame.
It has properties like:
`event.tracking_frame_id`: The unique ID for that frame.
`event.hands`: A list of Hand objects.

## `Hand` (hand in event.hands)
### Important
The hand is fit with a skeleton model with bones connected by joints.  
*Only the joints have x, y, z coordinates*


This contains all the data for an individual hand.
Properties include:
`hand.palm.position.x, .y, .z`: The palm's position in 3D space.
`hand.digits`: A list of Digit objects.

## `Digit` (digit in hand.digits) 
(was`Finger` (finger in hand.fingers))

Digits have IDs and bones. Confusingly, the digit ID property is called `finger_id`
Represents a single finger.
Properties include:
### finger.tip_position.x, .y, .z: The position of the fingertip.

The key is that the joints are the things with positions

## Summary
Each tracking event is effectively a "frame" or snapshot of the
hand data at a given time point.
The `event` contains a list of hand objects.
Each `hand` contains palm and digit (finger) data as
objects of class `Palm` and `Digit`, respectively.