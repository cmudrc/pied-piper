import unittest

from pr.tools import Entity


class TestEntityClass(unittest.TestCase):
    def test_entity_distance(self):
        e_1 = Entity(pos=[0, 0])
        e_2 = Entity(pos=[0, 1])
        d = e_1.distance(e_2)
        self.assertAlmostEqual(d, 1, places=5, msg="distance")


if __name__ == "__main__":
    unittest.main()