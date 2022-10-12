import unittest
from classes import DataClass

class ValuesEmptyTest(unittest.TestCase):
  def test_is_empty_min(self):
    self.assertEqual(array._min(), 'array is empty')
  def test_is_empty_max(self):
    self.assertEqual(array._max(), 'array is empty')
  def test_is_empty_sum(self):
    self.assertEqual(array._sum(), 'array is empty')
  def test_is_empty_mult(self):
    self.assertEqual(array._mult(), 'array is empty')

if __name__ == "__main__":
  array = DataClass([''])
  unittest.main()