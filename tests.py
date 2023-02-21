import unittest
from task import conv_endian


class TestTask(unittest.TestCase):

    def test_1(self):
        self.assertTrue(conv_endian(954786, 'big'), '0E 91 A2')

    def test_2(self):
        self.assertTrue(conv_endian(954786), '0E 91 A2')

    def test_3(self):
        self.assertTrue(conv_endian(-954786), '-0E 91 A2')

    def test_4(self):
        self.assertTrue(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_5(self):
        self.assertTrue(conv_endian(954786, 'little'), '-A2 91 0E')

    def test_6(self):
        self.assertTrue(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test_7(self):
        self.assertIsNone(conv_endian(num=-954786, endian='small'), None)

    def test_8(self):
        self.assertTrue(conv_endian(2147483647, 'big'), '7F FF FF FF')

    def test_9(self):
        self.assertTrue(conv_endian(2147483647, 'little'), 'FF FF FF 7F')

    def test_10(self):
        self.assertTrue(conv_endian(-2147483647, 'big'), '-7F FF FF FF')

    def test_11(self):
        self.assertTrue(conv_endian (-2147483647, 'little'), '-FF FF FF 7F')


if __name__ == '__main__':
    unittest.main(verbosity=2)
