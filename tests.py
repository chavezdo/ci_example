"""A testing suite for testing task.py."""
import unittest
from task import conv_endian, my_datetime


class TestTask(unittest.TestCase):
    """Test cases for testing task.py."""
    # ======================================================================
    # Function 2 Tests
    def test1(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test2(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test3(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test4(self):
        self.assertEqual(my_datetime(201653971200), "02-29-8360")

    # ======================================================================
    # Function 3 Tests
    def test_F3_1(self):
        """Test for positive value with big endian."""
        self.assertTrue(conv_endian(954786, 'big'), '0E 91 A2')

    def test_F3_2(self):
        """Test for postive value with no endian."""
        self.assertTrue(conv_endian(954786), '0E 91 A2')

    def test_F3_3(self):
        """Test for negative value with no endian."""
        self.assertTrue(conv_endian(-954786), '-0E 91 A2')

    def test_F3_4(self):
        """Test for positive value with little endian."""
        self.assertTrue(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_F3_5(self):
        """Test for positive value with little ending."""
        self.assertTrue(conv_endian(954786, 'little'), '-A2 91 0E')

    def test_F3_6(self):
        """Test for negative value with little endian using intializing arguments."""
        self.assertTrue(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test_F3_7(self):
        """Test for negative value with invalid endian using intializing arguments."""
        self.assertIsNone(conv_endian(num=-954786, endian='small'), None)

    def test_F3_8(self):
        """Test for postive value with big endian."""
        self.assertTrue(conv_endian(2147483647, 'big'), '7F FF FF FF')

    def test_F3_9(self):
        """Test for positive value with little endian"""
        self.assertTrue(conv_endian(2147483647, 'little'), 'FF FF FF 7F')

    def test_F3_10(self):
        """Test for negative value with big endian."""
        self.assertTrue(conv_endian(-2147483647, 'big'), '-7F FF FF FF')

    def test_F3_11(self):
        """Test for negative value with little endian."""
        self.assertTrue(conv_endian(-2147483647, 'little'), '-FF FF FF 7F')

    def test_F3_12(self):
        """Test for 0 with big endian."""
        self.assertTrue(conv_endian(0, 'big'), '00')

    def test_F3_13(self):
        """Test for 0 with little endian."""
        self.assertTrue(conv_endian(0, 'little'), '00')


if __name__ == '__main__':
    unittest.main(verbosity=2)