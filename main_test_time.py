import unittest
import time
from classes import DataClass


class TimeTest(unittest.TestCase):
  def test_time_mult(self):
    file = open("test_time_3.txt", "r")
    array = DataClass(file.readline().split(" "))
    start = time.perf_counter()
    tmp = array._mult()
    finish = time.perf_counter()
    file.close()
    self.assertLess(finish - start, 0.001)
if __name__ == "__main__":
  unittest.main()
