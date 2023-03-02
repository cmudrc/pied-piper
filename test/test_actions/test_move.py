import unittest
from copy import deepcopy

from piperabm.unit import Date, DT
from piperabm.actions import Move, Walk
from piperabm.environment.sample import env_0


class TestMoveClass(unittest.TestCase):

    env = env_0
    path_graph = env.to_path_graph(Date(2020, 1, 5), Date(2020, 1, 7))
    path = path_graph.edge_info(0, 1, 'path')

    m = Move(
        start_date=Date(2020, 1, 1),
        path=path,
        transportation=Walk()
    )

    def test_move_end_date(self):
        m = deepcopy(self.m)
        self.assertEqual(m.end_date.hour, 5, msg="it must take 5 hours.")

    def test_move_progress_0(self):
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
        date = Date(2020, 1, 1) + DT(hours=1)
        self.assertAlmostEqual(m.progress(date), 0.18)

    def test_fuel_0(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1)
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption['food'], 0)
        self.assertAlmostEqual(fuel_consumption['water'], 0)

    def test_fuel_1(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=1)
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption['food'], 36)
        self.assertAlmostEqual(fuel_consumption['water'], 72)

    def test_fuel_2(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=6)
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption['food'], 200)
        self.assertAlmostEqual(fuel_consumption['water'], 400)
    
    def test_fuel_3(self):
        m = deepcopy(self.m)
        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 1) + DT(hours=12)
        fuel_consumption = m.how_much_fuel(start_date, end_date)
        self.assertAlmostEqual(fuel_consumption['food'], 200)
        self.assertAlmostEqual(fuel_consumption['water'], 400)


if __name__ == "__main__":
    unittest.main()