import cv2
import numpy as np
import socket
import sys
import pickle
import struct ### new code
import time

cap=cv2.VideoCapture(0)

# Verified: this works. DO NOT MODIFY THIS CODE
while True:

    # Client side
    ret,frame=cap.read()
    data = pickle.dumps(frame) 
    send_buffer = struct.pack("L", len(data)) + data

    # Receive side
    payload_size = struct.calcsize("L") 
    data_in = send_buffer[payload_size:]
    packed_msg_size = send_buffer[:payload_size]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    frame_data = data_in[:msg_size]
    frame_in = pickle.loads(frame_data)

    if (frame_in == frame).all():
        cv2.imshow('frame',frame_in)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(1.0)

# Release camera TODO
cap.release()