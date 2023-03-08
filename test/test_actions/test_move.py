import unittest
from copy import deepcopy

from piperabm.unit import Date, DT
from piperabm.actions import Move, Walk
from piperabm.environment.sample import env_0


class TestMoveClass(unittest.TestCase):

    def setUp(self):
        env = env_0
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        all_settlements = env.all_nodes('settlement')
        path = path_graph.edge_info(all_settlements[0], all_settlements[1], 'path')
        #print(path)

        self.m = Move(
            start_date=Date(2020, 1, 1),
            path=path,
            transportation=Walk()
        )

    def test_end_date(self):
        m = deepcopy(self.m)
        #print(m.end_date)
        self.assertAlmostEqual(m.end_date.second, 30, places=2)

    def test_progress_0(self):
        m = deepcopy(self.m)
        date = Date(2020, 1, 1)
        self.assertEqual(m.progress(date), 0)

    def test_move_progress_1(self):
        m = deepcopy(self.m)
        date = Date(2020, 1, 2)
        self.assertEqual(m.progress(date), 1)
        #print(m.pos(date=Date(2020, 1, 1)+DT(hours=1)))
    
    def test_move_progress_2(self):
        m = deepcopy(self.m)
        date = Date(2020, 1, 1) + DT(seconds=15)
        self.assertAlmostEqual(m.progress(date), 0.5, places=1)

    def test_fuel_0(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = start_date
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption('food'), 0)
        self.assertAlmostEqual(fuel_consumption('water'), 0)

    def test_fuel_1(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(seconds=15)
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption('food'), 0.00035, places=4)
        self.assertAlmostEqual(fuel_consumption('water'), 0.00017, places=4)

    def test_fuel_2(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = start_date + DT(seconds=31)
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption('food'), 0.00070, places=4)
        self.assertAlmostEqual(fuel_consumption('water'), 0.00035, places=4)


if __name__ == "__main__":
    unittest.main()