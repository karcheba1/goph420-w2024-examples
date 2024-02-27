import unittest

from goph420_examples.classes import (
    Node,
)


class TestNodeValidInitializer(unittest.TestCase):

    def setUp(self):
        self.nd = Node(
            index=2,
            x=3.5,
            temp=-4.8,
        )

    def test_index_value(self):
        self.assertEqual(self.nd.index, 2)

    def test_index_type(self):
        self.assertIsInstance(self.nd.index, int)

    def test_pos_value(self):
        self.assertAlmostEqual(self.nd.x, 3.5)

    def test_pos_type(self):
        self.assertIsInstance(self.nd.x, float)

    def test_temp_value(self):
        self.assertAlmostEqual(self.nd.temp, -4.8)

    def test_temp_type(self):
        self.assertIsInstance(self.nd.temp, float)


class TestNodeInvalidInitializers(unittest.TestCase):

    def test_no_index(self):
        with self.assertRaises(TypeError):
            Node(x=1.0)

    def test_invalid_index(self):
        with self.assertRaises(TypeError):
            Node(index="one", x=1.0)

    def test_no_position(self):
        with self.assertRaises(TypeError):
            Node(index=1)

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            Node(index=1, x="five")


class TestNodeSetters(unittest.TestCase):

    def setUp(self):
        self.nd = Node(
            index=2,
            x=3.5,
            temp=-4.8,
        )

    def test_invalid_set_index(self):
        with self.assertRaises(AttributeError):
            self.nd.index = 2

    def test_invalid_set_position(self):
        with self.assertRaises(AttributeError):
            self.nd.x = 3.0

    def test_valid_set_temp(self):
        self.nd.temp = 5.2
        self.assertAlmostEqual(self.nd.temp, 5.2)

    def test_invalid_set_temp(self):
        with self.assertRaises(ValueError):
            self.nd.temp = "five"


if __name__ == "__main__":
    unittest.main()
