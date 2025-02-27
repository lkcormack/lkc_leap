# How Data are Structured in the Leap Motion Python Bindings
These are the python bindings to the LeapC API provided by
Ultraleap (formerly Leap Motion) for the Leap Controller 2.  

## Events (leap.Event)
These are generated automatically by the Leap Controller and are "heard"
by the `Listener` methods.

Example: `on_tracking_event(event)` fires when a new frame of tracking data arrives.

## Tracking Event (event in on_tracking_event)
A tracking event occurs whenever the leap controller has valid data. Tracking
events occur as fast as 120 Hz (events per second), but the actual speed
depends on the computer being used with the leap controller.  

Each tracking event contains data for one frame.
It has properties like:
`event.tracking_frame_id`: The unique ID for that frame.
`event.hands`: A list of Hand objects.

## `Hand` (hand in event.hands)
### Important
The hand is fit with a skeleton model with *bones* connected by *joints*.  
*Only the joints have x, y, z coordinates*. Thus, whenever we want
positional data, we need drill down from the "event" to the joint position:  
event -> hand -> digit (finger) -> bone -> joint


This contains all the data for an individual hand.
Properties include:
`hand.palm.position.x, .y, .z`: The palm's position in 3D space.
`hand.digits`: A list of Digit objects.

## `Digit` (digit in hand.digits) 
(note: this was`Finger` (finger in hand.fingers))

Digits have IDs and bones. Confusingly, the digit ID property is called `finger_id`
Represents a single finger.
Properties include:
`digit.distal.next_joint.x, .y, .z`: The position of the fingertip.

The key is that the joints are the things with positions. Bones have a 
"previous" (proximal) joint and a "next" (distal) joint. It the above 
example, the `next_joint` is actually the tip of the finger because the 
`distal` bone is the last bone on the finger.

## Summary
Each tracking event is effectively a "frame" or snapshot of the
hand data at a given time point.
The `event` contains a list of hand objects.
Each `hand` contains palm and digit (finger) data as
objects of class `Palm` and `Digit`, respectively.