import unittest
from calculadora import somar, subtrair

class TestCalculadora(unittest.TestCase):
  def test_somar(self):
    self.assertEqual(somar(2,3),5)

  def test_subtrair(self):
    self.assertEqual(subtrair(5,2),3)

if __name__ == "__main__":
  unittest.main()
