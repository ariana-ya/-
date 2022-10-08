import unittest
from main import _sum, _mult

class ValuesTest(unittest.TestCase):
  def test_values_sum(self):
    self.assertEqual(_sum([1, 2, 3, 9, 15]), 30)
    self.assertEqual(_sum([1, 2, 3, 9, 16]), 31)
    self.assertEqual(_sum([1, 2, 3, 9, 17]), 32)
    self.assertEqual(_sum([1, 2, 3, 9, 18]), 33)
    self.assertEqual(_sum([1, 2, 3, 9, 19]), 34)
  def test_values_mult(self):
    self.assertEqual(_mult([1, 2, 3, 0]), 0)
    self.assertEqual(_mult([1, 2, 3, 10]), 60)
    self.assertEqual(_mult([1, 2, 3, 11]), 66)
    self.assertEqual(_mult([1, 2, 3, 4]), 24)
    self.assertEqual(_mult([1, 2, 3, 6]), 36)


if __name__ == "__main__":
  unittest.main()