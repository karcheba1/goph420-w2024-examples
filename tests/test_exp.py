import unittest

from goph420_examples.functions import (
    exp,
)


class TestExp0(unittest.TestCase):
    def setUp(self):
        self.x = 0.0
    def test_value(self):
        expected = 1.0
        self.assertEqual(exp(self.x), expected)
    def test_type(self):
        self.assertIsInstance(exp(self.x), float)

if __name__ == "__main__":
    unittest.main()
