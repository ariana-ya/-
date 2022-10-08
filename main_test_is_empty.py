import unittest
from main import _min, _max, _sum, _mult

class ValuesTest(unittest.TestCase):
  def test_is_empty_min(self):
    self.assertEqual(_min(['']), 'array is empty')
  def test_is_empty_max(self):
    self.assertEqual(_max(['']), 'array is empty')
  def test_is_empty_sum(self):
    self.assertEqual(_sum(['']), 'array is empty')
  def test_is_empty_mult(self):
    self.assertEqual(_mult(['']), 'array is empty')

if __name__ == "__main__":
  unittest.main()