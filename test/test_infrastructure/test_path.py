import unittest

from piperabm import Model


class TestPathClass(unittest.TestCase):
    """
    Test path finding algorithm
    """

    def setUp(self):
        self.model = Model(seed=2)
        point_1 = [0, 0]
        point_2 = [10, 0]
        point_3 = [10, 10]
        point_4 = [0, 10]
        self.model.infrastructure.add_street(pos_1=point_1, pos_2=point_2)
        self.model.infrastructure.add_street(pos_1=point_3, pos_2=point_4)
        self.model.infrastructure.add_home(pos=point_1, id=1)
        self.model.infrastructure.add_home(pos=point_2, id=2)
        self.model.infrastructure.add_home(pos=point_3, id=3)
        self.model.infrastructure.add_home(pos=point_4, id=4)
        self.model.bake()

    def test_path_0(self):
        """
        A possible path to itself
        """
        path = self.model.infrastructure.path(id_start=1, id_end=1)
        expected_result = [1]
        self.assertListEqual(path, expected_result)

    def test_path_1(self):
        """
        A possible path to other home
        """
        path = self.model.infrastructure.path(id_start=1, id_end=2)
        expected_result = [1, 8042686386972756495, 478254495130285640, 2]
        self.assertListEqual(path, expected_result)

    def test_path_2(self):
        """
        Am impossible path to other home
        """
        path = self.model.infrastructure.path(id_start=1, id_end=3)
        expected_result = None
        self.assertEqual(path, expected_result)


if __name__ == "__main__":
    unittest.main()
