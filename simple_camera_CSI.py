"""import cv2

print("OpenCV Version:", cv2.__version__)
print("Checking GStreamer support...")

# Print OpenCV build information
print(cv2.getBuildInformation())

# Try opening a GStreamer video capture
pipeline = "nvarguscamerasrc ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink"

cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: GStreamer pipeline failed to open in OpenCV.")
else:
    print("Success: GStreamer pipeline works in OpenCV!")
    cap.release()



import gi
import cv2
print(cv2.getBuildInformation())"""
import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst

Gst.init(None)
pipeline = Gst.parse_launch("nvarguscamerasrc ! nvvidconv ! xvimagesink")
pipeline.set_state(Gst.State.PLAYING)

input("Press Enter to exit...\n")
pipeline.set_state(Gst.State.NULL)

