import unittest
from test import AW1

AW = AW1(0)
class TestAW(unittest.TestCase):

    def test_time1(self):
        self.assertEqual(AW.SecondsChange(AW._TimeDiff(12, 59))[0:5], '08:37')

    def test_time2(self):
        self.assertEqual(AW.SecondsChange(AW._TimeDiff(13, 10))[0:5], '08:48')

if __name__ == '__main__':
    unittest.main()