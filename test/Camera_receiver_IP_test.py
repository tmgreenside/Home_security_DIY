import unittest
import cv2
from surveillence_cam.Camera_receiver_IP import Camera_receiver_IP

test_img_path = "test_files/frame1.jpg"        

class Camera_receiver_IP_test(unittest.TestCase):

    def setUp(self) -> None:
        self.test_host = "127.0.0.1"
        self.test_port = 8080
        
        self.uut = Camera_receiver_IP(self.test_host, self.test_port)
        return super().setUp()
    
    def tearDown(self) -> None:
        self.uut.set_stop_listening(True)
        return super().tearDown()

    def test_receive_data(self):
        self.uut.receive_camera_start()
        
        
    
