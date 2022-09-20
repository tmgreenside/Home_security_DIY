import socket
import pickle
import struct
import threading
import queue
import cv2

class Camera_receiver_IP:

    # TODO Figure out adding a function to execute on the received data
    # Plan B: Try using a producer-consumer with a queue and function from
    # init class retrieves that data. Data receiver still in a separate
    # thread.
    def __init__(self, ip_addr: str, port: int):
        self.serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serv_socket.bind((ip_addr, port))
        self.serv_socket.listen(10)

        self.stop_listening_mutex = threading.Lock()
        self.stop_listening = False

        self.receive_camera_thread = threading.Thread(target = self._receive_camera_func)

        self.received_frames_mutex = threading.Lock()
        self.received_frames_queue = queue.Queue()
    
    def receive_camera_start(self):
        self.receive_camera_thread.start() 
    
    def set_stop_listening(self, stop_listening: bool):
        self.stop_listening_mutex.acquire()
        self.stop_listening = stop_listening
        self.stop_listening_mutex.release() 

        if stop_listening:
            self.receive_camera_thread.join()
    
    def read_latest_frame(self):
        frame = None 
        self.received_frames_mutex.acquire()
        if not self.received_frames_queue.empty():
            frame = self.received_frames_queue.get()
        self.received_frames_mutex.release()
        return frame

    def _receive_camera_func(self):
        self.stop_listening = False
        conn, addr = self.serv_socket.accept()
        payload_size = struct.calcsize("L") 
        while not self.stop_listening:
            data_in = bytearray()
            while len(data_in) < payload_size:
                data_in += conn.recv(4096)
            packed_msg_size = data_in[:payload_size]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            data_in = data_in[payload_size:]
            while len(data_in) < msg_size:
                data_in += conn.recv(4096)
            frame_data = data_in[:msg_size]
            frame=pickle.loads(frame_data)
            self.received_frames_mutex.acquire()
            self.received_frames_queue.put(frame)
            self.received_frames_mutex.release()
            

