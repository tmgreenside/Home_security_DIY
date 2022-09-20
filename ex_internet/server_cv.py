import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new

HOST=''
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

# Image capture works, just doesn't display as part of a frame.
# Protocol over socket verified.
payload_size = struct.calcsize("L") 
while True:
    data_in = bytearray()
    while len(data_in) < payload_size:
        data_in += conn.recv(4096)
    packed_msg_size = data_in[:payload_size]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    data_in = data_in[payload_size:]
    while len(data_in) < msg_size:
        data_in += conn.recv(4096)
    frame_data = data_in[:msg_size]
    
    print("Received frame")
    frame=pickle.loads(frame_data)
    cv2.imwrite('frame1.jpg', frame)