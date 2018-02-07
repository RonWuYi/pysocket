import unittest
from test import AW1

AW = AW1(0)
class TestAW(unittest.TestCase):

    # def test_time1(self):
    #     self.assertEqual(AW.SecondsChange(AW._TimeDiff(12, 59))[0:5], '08:37')
    #
    def test_time2(self):
        self.assertEqual(AW.SecondsChange(AW._TimeDiff(13))[0:8], '00:11:47')

    def test_time3(self):
        self.assertEqual(AW.SecondsChange(360000), '04:08:00:00')

if __name__ == '__main__':
    unittest.main()