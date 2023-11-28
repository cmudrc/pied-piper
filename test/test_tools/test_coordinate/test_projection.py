import unittest

from piperabm.tools.coordinate.projection.flatten import Flatten, deg_to_rad,rad_to_deg


class TestFlattenClass_0(unittest.TestCase):

    def setUp(self) -> None:
        radius = 1
        latitude_0 = deg_to_rad(0)
        longitude_0 = deg_to_rad(0)
        self.projection = Flatten(latitude_0, longitude_0, radius)

    def test_0(self):
        latitude = deg_to_rad(0)
        longitude = deg_to_rad(0)
        alpha, theta = self.projection.calcualte_alpha_theta(latitude, longitude)
        alpha_deg = rad_to_deg(alpha)
        theta_deg = rad_to_deg(theta)
        self.assertAlmostEqual(alpha_deg, 0, places=2)
        self.assertAlmostEqual(theta_deg, 90, places=2)
        latitude_prime, longitude_prime = self.projection.calculate_latitude_longitude_prime(alpha, theta)
        latitude_prime_deg = rad_to_deg(latitude_prime)
        longitude_prime_deg = rad_to_deg(longitude_prime)
        self.assertAlmostEqual(latitude_prime_deg, 0, places=2)
        self.assertAlmostEqual(longitude_prime_deg, 0, places=2)
        x, y = self.projection.mercator_projection(latitude_prime, longitude_prime)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)

        x, y = self.projection.convert(latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)

    def test_1(self):
        latitude = deg_to_rad(90)
        longitude = deg_to_rad(0)
        alpha, theta = self.projection.calcualte_alpha_theta(latitude, longitude)
        alpha_deg = rad_to_deg(alpha)
        theta_deg = rad_to_deg(theta)
        self.assertAlmostEqual(alpha_deg, 90, places=2)
        self.assertAlmostEqual(theta_deg, 0, places=2)
        latitude_prime, longitude_prime = self.projection.calculate_latitude_longitude_prime(alpha, theta)
        latitude_prime_deg = rad_to_deg(latitude_prime)
        longitude_prime_deg = rad_to_deg(longitude_prime)
        self.assertAlmostEqual(latitude_prime_deg, 90, places=2)
        self.assertAlmostEqual(longitude_prime_deg, 0, places=2)
        x, y = self.projection.mercator_projection(latitude_prime, longitude_prime)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 37.33, places=2)

        x, y = self.projection.convert(latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 37.33, places=2)

    def test_2(self):
        latitude = deg_to_rad(0)
        longitude = deg_to_rad(90)
        alpha, theta = self.projection.calcualte_alpha_theta(latitude, longitude)
        alpha_deg = rad_to_deg(alpha)
        theta_deg = rad_to_deg(theta)
        self.assertAlmostEqual(alpha_deg, 90, places=2)
        self.assertAlmostEqual(theta_deg, 90, places=2) 
        latitude_prime, longitude_prime = self.projection.calculate_latitude_longitude_prime(alpha, theta)
        latitude_prime_deg = rad_to_deg(latitude_prime)
        longitude_prime_deg = rad_to_deg(longitude_prime)
        self.assertAlmostEqual(latitude_prime_deg, 0, places=2)
        self.assertAlmostEqual(longitude_prime_deg, 90, places=2)
        x, y = self.projection.mercator_projection(latitude_prime, longitude_prime)
        self.assertAlmostEqual(x, 1.57, places=2)
        self.assertAlmostEqual(y, 0, places=2)

        x, y = self.projection.convert(latitude, longitude)
        self.assertAlmostEqual(x, 1.57, places=2)
        self.assertAlmostEqual(y, 0, places=2)

    def test_3(self):
        latitude = deg_to_rad(90)
        longitude = deg_to_rad(90)
        alpha, theta = self.projection.calcualte_alpha_theta(latitude, longitude)
        alpha_deg = rad_to_deg(alpha)
        theta_deg = rad_to_deg(theta)
        self.assertAlmostEqual(alpha_deg, 90, places=2)
        self.assertAlmostEqual(theta_deg, 0, places=2) 
        latitude_prime, longitude_prime = self.projection.calculate_latitude_longitude_prime(alpha, theta)
        latitude_prime_deg = rad_to_deg(latitude_prime)
        longitude_prime_deg = rad_to_deg(longitude_prime)
        self.assertAlmostEqual(latitude_prime_deg, 90, places=2)
        self.assertAlmostEqual(longitude_prime_deg, 0, places=2)
        x, y = self.projection.mercator_projection(latitude_prime, longitude_prime)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 37.33, places=2)

        x, y = self.projection.convert(latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 37.33, places=2)


class TestFlattenClass_1(unittest.TestCase):

    def setUp(self) -> None:
        radius = 1
        latitude_0 = deg_to_rad(45)
        longitude_0 = deg_to_rad(45)
        self.projection = Flatten(latitude_0, longitude_0, radius)

    def test_0(self):
        latitude = deg_to_rad(45)
        longitude = deg_to_rad(45)
        alpha, theta = self.projection.calcualte_alpha_theta(latitude, longitude)
        alpha_deg = rad_to_deg(alpha)
        theta_deg = rad_to_deg(theta)
        self.assertAlmostEqual(alpha_deg, 0, places=2)
        self.assertAlmostEqual(theta_deg, 45, places=2)
        latitude_prime, longitude_prime = self.projection.calculate_latitude_longitude_prime(alpha, theta)
        latitude_prime_deg = rad_to_deg(latitude_prime)
        longitude_prime_deg = rad_to_deg(longitude_prime)
        self.assertAlmostEqual(latitude_prime_deg, 0, places=2)
        self.assertAlmostEqual(longitude_prime_deg, 0, places=2)
        x, y = self.projection.mercator_projection(latitude_prime, longitude_prime)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)

        x, y = self.projection.convert(latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)


class TestMercatorFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.projection = Flatten()

    def test_0(self):
        latitude = deg_to_rad(0)
        longitude = deg_to_rad(0)
        x, y = self.projection.mercator_projection(latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 0, places=2)

    def test_1(self):
        latitude = deg_to_rad(90)
        longitude = deg_to_rad(0)
        x, y = self.projection.mercator_projection(latitude, longitude)
        self.assertAlmostEqual(x, 0, places=2)
        self.assertAlmostEqual(y, 37.33, places=2)

    def test_2(self):
        latitude = deg_to_rad(0)
        longitude = deg_to_rad(90)
        x, y = self.projection.mercator_projection(latitude, longitude)
        self.assertAlmostEqual(x, 1.57, places=2)
        self.assertAlmostEqual(y, 0, places=2)


if __name__ == "__main__":
    unittest.main()