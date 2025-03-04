# How Data are Structured in the Leap Motion Python Bindings
These are the python bindings to the LeapC API provided by
Ultraleap (formerly Leap Motion) for the Leap Controller 2.  

The full description of the C structures that are being converted to Python objects are [here](https://docs.ultraleap.com/api-reference/tracking-api/group/group___structs.html) (https://docs.ultraleap.com/api-reference/tracking-api/group/group___structs.html).

## Events (leap.Event)
These are generated automatically by the Leap Controller and are "heard"
by the `Listener` methods.

Example: `on_tracking_event(event)` fires when a new frame of tracking data arrives.

## Tracking Event (event returned by `on_tracking_event()`)

A tracking event occurs whenever the leap controller has valid data. Tracking
events occur as fast as 120 Hz (events per second), but the actual speed
depends on the computer being used with the leap controller.  

Each tracking event contains data for one frame.
It has properties like:
`event.tracking_frame_id`: The unique ID for that frame.
`event.hands`: A list of Hand objects.

## `Hand` (hand in event.hands)
### Important
> [!IMPORTANT]
>
> The hand is fit with a skeleton model with *bones* connected by *joints*.  
> *Only the joints have x, y, z coordinates*. Thus, whenever we want
> positional data, we need drill down from the "event" to the joint position:  
> event -> hand -> digit (finger) -> bone -> joint (`joint_next` or `joint_previous`)

Hand contains all the data for an individual hand.
Properties include:

`hand.type` - either `HandType.Right`or `HandType.Left`

`hand.palm.position.x, .y, .z`: The palm's position in 3D space.
`hand.digits`: A list of Digit objects.

## `Digit` (digit in hand.digits)

Represents a single finger.  

> [!WARNING]
>
> (note: this used to be `Finger` (finger in hand.fingers), and this confuses AI)

Digits have IDs and bones. Confusingly, the digit ID property is called `finger_id`

Properties include:

`bones` - a list of the bones

and each bone, `metacarpal`, `proximal`, `intermediate`, and `distal` , e.g. 

`digit.distal`

## Bone (bone in digit.bones)

Represents a single bone (on a single finger of a single hand)

Properties:

`previous.joint` - the proximal joint of the bone

`next.joint` - the distal joint of the bone

`width` - the average width of the finger (flesh) on the bone

`rotation` - (presumably) the four entries of the rotation matrix of the bone from the forward (z) direction (don't know in what order yet)

To get the position of the fingertip, we get the position of the "next joint" of the distal bone. Since the distal bone is the last bone, the distal "joint" is actually the position of the fingertip, e.g.,

`digit.distal.next_joint.x, .y, .z`: The position of the fingertip. 

The key is that the *joints* are the things with positions. So to get finger positions, we get the  "previous" (proximal) joint and a "next" (distal) joint.

## Summary
Each tracking event is effectively a "frame" or snapshot of the
hand data at a given time point.
The `event` contains a list of hand objects.
Each `hand` contains palm and digit (finger) data as
objects of class `Palm` and `Digit`, respectively. The digits have bones, the bones have joints, and the joints have the x, y, z positions in space.

The digits each have 4 bones, and the bones each have 2 joints, and it is the joints that contain the x,y,z positional data.