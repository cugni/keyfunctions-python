from keyfunctions import create_key
from keyfunctions import create_element_rand
import keyfunctions.globals as consts
import random
import unittest
import struct


class CoreTestSuite(unittest.TestCase):
    """Testing of core functions."""

    def test_createKey(self):
        key = create_key([0.2, 0.001, 0.223], 10)
        self.assertEqual(key, convert("0055401502"))

        key = create_key([0.92, 0.12001, 0.11223], 10)
        self.assertEqual(key, convert("1116763170"))

        key = create_key([0.92, 0.12001, 0.11223], 2)
        self.assertEqual(key, convert("11"))

    def test_createKey5dims(self):
        for size in [0, 2, 3, 10, 17]:
            key = create_key([random.random() for i in range(5)], size)
            self.assertEqual(len(key), size)

    def test_create_element_rand(self):
        long_value = (1039935063 << 32) + 24434444
        self.assertEqual(long_value, 4466487085573134092)
        rand = create_element_rand(struct.pack('q', long_value))

        self.assertEqual(rand, 411538470)

        rand = create_element_rand(long_value)

        self.assertEqual(rand, 411538470)


if __name__ == '__main__':
    unittest.main()


def convert(key):
    return "".join(map(lambda c: chr(int(c) + consts.PRINTABLE_OFFSET), key))
