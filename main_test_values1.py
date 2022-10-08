import unittest
from main import _min, _max

class ValuesTest(unittest.TestCase):
  def test_values_min(self):
    self.assertEqual(_min([1, 2, 3]), 1)
    self.assertEqual(_min([1, 2]), 1)
    self.assertEqual(_min([1]), 1)
    self.assertEqual(_min([1, 2, 3, -100]), -100)
    self.assertEqual(_min([1, 2, 3, 1, 1]), 1)
  def test_values_max(self):
    self.assertEqual(_max([1, 2, 3, 10]), 10)
    self.assertEqual(_max([-1, -2, -3, -10]), -1)
    self.assertEqual(_max([1, 2, 3, 10, 1000000]), 1000000)
    self.assertEqual(_max([1]), 1)
    self.assertEqual(_max([1, 2]), 2)

if __name__ == "__main__":
  unittest.main()