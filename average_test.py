import unittest
import average

class testAverage(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(average.listAverage([]), 0)

    def test_integers(self):
        self.assertEqual(average.listAverage([2, 4, 6, 8]), 5)
        self.assertEqual(average.listAverage([1, 3, 5, 7, 9]), 5)

    def test_negatives(self):
        self.assertEqual(average.listAverage([-10, -6, -2]), -6)
        self.assertEqual(average.listAverage([-100, -20]), -60)


if __name__ == "__main__":
    unittest.main()
