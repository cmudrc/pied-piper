import unittest

from piperabm.environment import check_existance, Environment
from piperabm.unit import Date, DT
from piperabm.degradation import DiracDelta
from piperabm.boundary import Circular


class TestExistanecFunction(unittest.TestCase):

    start_date = Date(2020, 1, 2)
    end_date = Date(2020, 1, 4)

    def test_0(self):
        initiation_date = Date(2020, 1, 1)
        result = check_existance(initiation_date, None, None)
        self.assertTrue(result)

    def test_1(self):
        initiation_date = Date(2020, 1, 1)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)
    
    def test_2(self):
        initiation_date = Date(2020, 1, 2)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)

    def test_3(self):
        initiation_date = Date(2020, 1, 3)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertTrue(result)

    def test_4(self):
        initiation_date = Date(2020, 1, 4)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertFalse(result)

    def test_5(self):
        initiation_date = Date(2020, 1, 5)
        result = check_existance(initiation_date, self.start_date, self.end_date)
        self.assertFalse(result)


class TestEnvironmentClass(unittest.TestCase):

    env = Environment()

    env.add_settlement(
        name="John's Home",
        pos=[-2, -2],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_settlement(
        name="Peter's Home",
        pos=[20, 20],
        boundary=Circular(radius=5),
        initiation_date=Date(2020, 1, 4),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    env.add_link(
        "John's Home",
        [20, 0],
        initiation_date=Date(2020, 1, 2),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )
    env.add_link(
        [20.3, 0.3],
        "Peter's Home",
        initiation_date=Date(2020, 1, 4),
        degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
    )

    def test_1(self):
        path = self.env.to_path(start_date=Date(2020, 1, 1), end_date=Date(2020, 1, 1)+DT(hours=12))
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_2(self):
        path = self.env.to_path(start_date=Date(2020, 1, 1), end_date=Date(2020, 1, 2))
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 0)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 0)

    def test_3(self):
        path = self.env.to_path(start_date=Date(2020, 1, 1), end_date=Date(2020, 1, 3))
        nodes_count = path.G.number_of_nodes()
        self.assertEqual(nodes_count, 1)
        edges_count = path.G.number_of_edges()
        self.assertEqual(edges_count, 1)

if __name__ == "__main__":
    unittest.main()