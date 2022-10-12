import unittest
from classes import DataClass

class TimeTest1(unittest.TestCase):
  def test_time_1_min(self):
    self.assertEqual(array._min(), 1)
  def test_time_1_max(self):
    self.assertEqual(array._max(), 99999)
  def test_time_1_sum(self):
    self.assertEqual(array._sum(), 4999950007)
  def test_time_1_mult(self):
    self.assertEqual(array._mult(), ans)
if __name__ == "__main__":
  file = open("test_time_5.txt", "r", encoding="utf-8")
  file_ans = open("answers_for_time_testing_5.txt", "r", encoding="utf-8")
  ans = int(file_ans.readline())
  array = DataClass(file.readline().split(' '))

  unittest.main()