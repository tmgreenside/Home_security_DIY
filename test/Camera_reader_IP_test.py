import unittest
from surveillence_cam.Camera_reader_IP import Camera_reader_IP

class Camera_reader_IP_test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
