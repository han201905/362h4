import unittest
import volume

class testVolume(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(volume.cubeVolome(5), 125)
        self.assertEqual(volume.cubeVolome(10), 1000)

    def test_decimal(self):
        self.assertEqual(volume.cubeVolome(5.5), 166.375)
        self.assertEqual(volume.cubeVolome(10.1), 1030.301)

    def test_negative(self):
        self.assertEqual(volume.cubeVolome(-5), 0)
        self.assertEqual(volume.cubeVolome(-10), 0)
    
if __name__ == "__main__":
    unittest.main()