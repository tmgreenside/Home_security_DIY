import cv2
import socket
import pickle
import struct
import time

class Camera_reader_IP:

    # Constructor.
    # ip_addr: IP address of host to send frames to
    # port: Port on host to send frames to
    def __init__(self, ip_addr, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip_addr, port))

        self.stop_stream = False

    def stream_camera(self):
        self.stop_stream = False

        vid = cv2.VideoCapture(0)

        while not self.stop_stream:
            ret,frame=vid.read()
            data = pickle.dumps(frame) ### new code
            self.client_socket.sendall(struct.pack("L", len(data))+data) ### new code
            print("Sent frame")
            time.sleep(1.0)
        
        vid.release()
        # cv2.destroyAllWindows()
 
        # LEFT OFF HERE
        # See https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv







