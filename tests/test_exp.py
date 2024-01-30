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


class TestExp1(unittest.TestCase):
    def setUp(self):
        self.x = 1.0

    def test_value(self):
        expected = 2.7182818284590452353602874713526624977572
        self.assertAlmostEqual(exp(self.x), expected,
                               delta=1e-15)

    def test_type(self):
        self.assertIsInstance(exp(self.x), float)


class TestExpInvalidInput(unittest.TestCase):

    def test_invalid_string_input(self):
        with self.assertRaises(ValueError):
            exp("one")


if __name__ == "__main__":
    unittest.main()
