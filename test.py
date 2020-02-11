
#### Unit testing to check if the returned results of the highest temperature are correct from the Weather_script.py.
import Weather_script

import unittest

class TestResults(unittest.TestCase):

    def test_region(self):
        self.assertEqual(Weather_script.Region_str, 'Highland & Eilean Siar')

    def test_temperature(self):
        self.assertEqual(Weather_script.Temperature_value,15.8)

    def test_datetime(self):
        self.assertEqual(Weather_script.Date_time_str,'2016-03-17T00:00:00')

if __name__ == '__main__':
    unittest.main()
