from keyfunctions import create_key
from keyfunctions import create_element_rand
import unittest
import struct


class CoreTestSuite(unittest.TestCase):
    """Testing of core functions."""

    def test_createKey(self):
        key = create_key([0.2, 0.001, 0.223], 10)
        self.assertEqual(key, "0055401502")

        key = create_key([0.92, 0.12001, 0.11223], 10)
        self.assertEqual(key, "1116763170")

        key = create_key([0.92, 0.12001, 0.11223], 2)
        self.assertEqual(key, "11")

    def test_create_element_rand(self):
        long_value = (long(1039935063) << 32) + long(24434444)
        self.assertEqual(long_value, 4466487085573134092L)
        rand = create_element_rand(struct.pack('q', long_value))

        self.assertEqual(rand, 411538470)

        rand = create_element_rand(long_value)

        self.assertEqual(rand, 411538470)


if __name__ == '__main__':
    unittest.main()
