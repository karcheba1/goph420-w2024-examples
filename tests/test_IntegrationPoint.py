import unittest

from goph420_examples.classes import (
    IntegrationPoint,
)


class TestIntegrationPointValidInitializer(unittest.TestCase):

    def setUp(self):
        self.ip = IntegrationPoint(
            local_coord=0.5,
            weight=1.0,
            x=3.5,
            temp=-4.8,
            density=1.3,
            thrm_cond=1.5e6,
            spec_heat_cap=2.22,
            heat_trans_coef=1.8,
        )

    def test_local_coord_value(self):
        self.assertAlmostEqual(self.ip.local_coord, 0.5)

    def test_local_coord_type(self):
        self.assertIsInstance(self.ip.local_coord, float)

    def test_weight_value(self):
        self.assertAlmostEqual(self.ip.weight, 1.0)

    def test_weight_type(self):
        self.assertIsInstance(self.ip.weight, float)

    def test_pos_value(self):
        self.assertAlmostEqual(self.ip.x, 3.5)

    def test_pos_type(self):
        self.assertIsInstance(self.ip.x, float)

    def test_temp_value(self):
        self.assertAlmostEqual(self.ip.temp, -4.8)

    def test_temp_type(self):
        self.assertIsInstance(self.ip.temp, float)

    def test_density_value(self):
        self.assertAlmostEqual(self.ip.density, 1.3)

    def test_density_type(self):
        self.assertIsInstance(self.ip.density, float)

    def test_thrm_cond_value(self):
        self.assertAlmostEqual(self.ip.thrm_cond, 1.5e6)

    def test_thrm_cond_type(self):
        self.assertIsInstance(self.ip.thrm_cond, float)

    def test_spec_heat_cap_value(self):
        self.assertAlmostEqual(self.ip.spec_heat_cap, 2.22)

    def test_spec_heat_cap_type(self):
        self.assertIsInstance(self.ip.spec_heat_cap, float)

    def test_heat_trans_coef_value(self):
        self.assertAlmostEqual(self.ip.heat_trans_coef, 1.8)

    def test_heat_trans_coef_type(self):
        self.assertIsInstance(self.ip.heat_trans_coef, float)


class TestIntegrationPointInvalidInitializers(unittest.TestCase):

    def test_no_local_coord(self):
        with self.assertRaises(TypeError):
            IntegrationPoint(weight=1.0, x=1.5)

    def test_invalid_local_coord(self):
        with self.assertRaises(ValueError):
            IntegrationPoint(local_coord="five", weight=1.0, x=1.5)

    def test_no_weight(self):
        with self.assertRaises(TypeError):
            IntegrationPoint(local_coord=0.5, x=1.5)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            IntegrationPoint(local_coord=0.5, weight=-0.1, x=1.5)

    def test_no_position(self):
        with self.assertRaises(TypeError):
            IntegrationPoint(local_coord=0.5, weight=1.0)

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            IntegrationPoint(local_coord=0.5, weight=1.0, x="five")


class TestIntegrationPointSetters(unittest.TestCase):

    def setUp(self):
        self.ip = IntegrationPoint(
            local_coord=0.5,
            weight=1.0,
            x=3.5,
        )

    def test_invalid_set_local_coord(self):
        with self.assertRaises(AttributeError):
            self.ip.local_coord = 0.8

    def test_invalid_set_weight(self):
        with self.assertRaises(AttributeError):
            self.ip.weight = 0.7

    def test_invalid_set_position(self):
        with self.assertRaises(AttributeError):
            self.ip.x = 3.0

    def test_valid_set_temp(self):
        self.ip.temp = 5.2
        self.assertAlmostEqual(self.ip.temp, 5.2)

    def test_invalid_set_temp(self):
        with self.assertRaises(ValueError):
            self.ip.temp = "five"

    def test_valid_set_density(self):
        self.ip.density = 1.6
        self.assertAlmostEqual(self.ip.density, 1.6)

    def test_invalid_set_density_type(self):
        with self.assertRaises(ValueError):
            self.ip.density = "five"

    def test_invalid_set_density_value(self):
        with self.assertRaises(ValueError):
            self.ip.density = -1.3

    def test_valid_set_thrm_cond(self):
        self.ip.thrm_cond = 1.6e3
        self.assertAlmostEqual(self.ip.thrm_cond, 1.6e3)

    def test_invalid_set_thrm_cond_type(self):
        with self.assertRaises(ValueError):
            self.ip.thrm_cond = "five"

    def test_invalid_set_thrm_cond_value(self):
        with self.assertRaises(ValueError):
            self.ip.thrm_cond = -1.3e5

    def test_valid_set_spec_heat_cap(self):
        self.ip.spec_heat_cap = 1.9
        self.assertAlmostEqual(self.ip.spec_heat_cap, 1.9)

    def test_invalid_set_spec_heat_cap_type(self):
        with self.assertRaises(ValueError):
            self.ip.spec_heat_cap = "five"

    def test_invalid_set_spec_heat_cap_value(self):
        with self.assertRaises(ValueError):
            self.ip.spec_heat_cap = -1.9

    def test_valid_set_heat_trans_coef(self):
        self.ip.heat_trans_coef = 5.2
        self.assertAlmostEqual(self.ip.heat_trans_coef, 5.2)

    def test_invalid_set_heat_trans_coef_type(self):
        with self.assertRaises(ValueError):
            self.ip.heat_trans_coef = "five"

    def test_invalid_set_heat_trans_coef_value(self):
        with self.assertRaises(ValueError):
            self.ip.heat_trans_coef = -1.9


if __name__ == "__main__":
    unittest.main()
