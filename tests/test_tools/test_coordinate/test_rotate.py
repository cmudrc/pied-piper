import unittest
from piperabm.tools.coordinate.rotate import rotate, preprocess


class TestRotate(unittest.TestCase):

    def test_rotate_x(self):
        vector = [0, 1, 0]
        angle = 45
        rotated_vector = rotate.x(vector, angle, unit="degree", rotate="axis")
        self.assertAlmostEqual(rotated_vector[0], 0, places=2)
        self.assertAlmostEqual(rotated_vector[1], 0.7071, places=2)
        self.assertAlmostEqual(rotated_vector[2], -0.7071, places=2)

    def test_rotate_y(self):
        vector = [0, 1, 0]
        angle = 45
        rotated_vector = rotate.y(vector, angle, unit="degree", rotate="axis")
        self.assertAlmostEqual(rotated_vector[0], 0, places=2)
        self.assertAlmostEqual(rotated_vector[1], 1, places=2)
        self.assertAlmostEqual(rotated_vector[2], 0, places=2)

    def test_rotate_z(self):
        vector = [0, 1, 0]
        angle = 45
        rotated_vector = rotate.z(vector, angle, unit="degree", rotate="axis")
        self.assertAlmostEqual(rotated_vector[0], 0.7071, places=2)
        self.assertAlmostEqual(rotated_vector[1], 0.7071, places=2)
        self.assertAlmostEqual(rotated_vector[2], 0, places=2)

    def test_preprocess(self):
        vector = [0, 1]
        angle = 45
        vector_processed, angle_radians, factor = preprocess(
            vector, angle, unit="degree", rotate="vector"
        )
        self.assertListEqual(list(vector_processed), [0, 1, 0])
        self.assertAlmostEqual(angle_radians, 0.785, places=2)
        self.assertEqual(factor, -1)


if __name__ == "__main__":
    unittest.main()
