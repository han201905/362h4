import unittest
import fullName


class testFullName(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(fullName.fullName('', ''), ' ')

    def test_regular(self):
        self.assertEqual(fullName.fullName('Jane', 'Doe'), 'Jane Doe')
        self.assertEqual(fullName.fullName('Jackie', 'Chan'), 'Jackie Chan')

    def test_numbers(self):
        self.assertEqual(fullName.fullName('9', '9'), '9 9')
        self.assertEqual(fullName.fullName('Jarven', '4'), 'Jarven 4')


if __name__ == "__main__":
    unittest.main()
