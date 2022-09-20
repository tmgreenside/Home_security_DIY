import threading
import time

from surveillence_cam.Camera_reader_IP import Camera_reader_IP
from surveillence_cam.Camera_receiver_IP import Camera_receiver_IP

host = "127.0.0.1"
port = 8080

serv = Camera_receiver_IP(host, port)
serv_thread = threading.Thread(target=serv.receive_camera)
serv_thread.start()

cam = Camera_reader_IP(host, port)
cam_thread = threading.Thread(target=cam.stream_camera)
cam_thread.start()

time.sleep(10)
cam.stop_stream = True
time.sleep(2)
serv.stop_listening = True 

cam_thread.join()
serv_thread.join()

