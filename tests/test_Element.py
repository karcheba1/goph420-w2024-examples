import unittest

import numpy as np

from goph420_examples.classes import (
    Node,
    Element,
)


class TestElementValidInitializer(unittest.TestCase):

    def setUp(self):
        self.nodes = (
            Node(1, 3.5),
            Node(2, 5.0),
        )
        self.e = Element(
            self.nodes,
            order=1,
        )

    def test_order_value(self):
        self.assertEqual(self.e.order, 1)

    def test_order_type(self):
        self.assertIsInstance(self.e.order, int)

    def test_nodes_value(self):
        self.assertIs(self.e.nodes[0], self.nodes[0])
        self.assertIs(self.e.nodes[1], self.nodes[1])

    def test_nodes_type(self):
        self.assertIsInstance(self.e.nodes, tuple)

    def test_num_nodes_value(self):
        self.assertEqual(self.e.num_nodes, 2)

    def test_num_nodes_type(self):
        self.assertIsInstance(self.e.num_nodes, int)

    def test_jacobian_value(self):
        expected = np.abs(self.nodes[1].x - self.nodes[0].x)
        self.assertAlmostEqual(self.e.jacobian, expected)

    def test_jacobian_type(self):
        self.assertIsInstance(self.e.jacobian, float)


class TestElementInvalidInitializers(unittest.TestCase):

    def test_no_nodes(self):
        with self.assertRaises(TypeError):
            Element(order=1)

    def test_invalid_nodes(self):
        with self.assertRaises(TypeError):
            Element(nodes=(1, 2), order=1)

    def test_no_order(self):
        with self.assertRaises(TypeError):
            Element((Node(1, 1.5), Node(2, 2.0)))

    def test_invalid_order_float(self):
        with self.assertRaises(TypeError):
            Element(
                (Node(1, 1.5), Node(2, 2.0)),
                order=1.0,
            )

    def test_invalid_order_str(self):
        with self.assertRaises(TypeError):
            Element(
                (Node(1, 1.5), Node(2, 2.0)),
                order="1",
            )

    def test_invalid_order_zero(self):
        with self.assertRaises(ValueError):
            Element(
                (Node(1, 1.5), Node(2, 2.0)),
                order=0,
            )

    def test_invalid_order_neg(self):
        with self.assertRaises(ValueError):
            Element(
                (Node(1, 1.5), Node(2, 2.0)),
                order=-1,
            )

    def test_invalid_nodes_too_few(self):
        with self.assertRaises(ValueError):
            Element(
                (Node(1, 1.5), Node(2, 2.0)),
                order=3,
            )

    def test_invalid_nodes_too_many(self):
        with self.assertRaises(ValueError):
            Element(
                (
                    Node(0, 1.0),
                    Node(1, 1.5),
                    Node(2, 2.0),
                    Node(3, 2.5),
                ),
                order=2,
            )


class TestElementMatricesAndVectors(unittest.TestCase):
    def setUp(self):
        self.e = Element(
            (Node(0, 1.5), Node(1, 2.0), ),
            order=1,
        )
        for ip in self.e.int_pts:
            ip.thrm_cond = 1.3e6
            ip.density = 1.5e3
            ip.spec_heat_cap = 2.5
            ip.heat_trans_coef = 1.2

    def test_storage_matrix(self):
        expected = (
            1.5e3 * 2.5 * 0.5 / 6.0
            * np.array([[2.0, 1.0], [1.0, 2.0]])
        )
        self.assertTrue(np.allclose(expected, self.e.storage_matrix))


if __name__ == "__main__":
    unittest.main()
