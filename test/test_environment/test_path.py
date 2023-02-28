import unittest
from copy import deepcopy

from piperabm.environment.sample import env_0
from piperabm.transportation import Walk
from piperabm.unit import Date


class TestPathClass(unittest.TestCase):

    env = env_0
    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 7)
    env.update_elements(start_date, end_date)
    path_graph = env.to_path_graph(start_date, end_date)
    all_settlements = env.all_nodes('settlement')
    path = path_graph.edge_info(all_settlements[0], all_settlements[1], 'path')
    #print(path)

    def test_adjusted_length(self):
        path = deepcopy(self.path)
        result = path.adjusted_length()
        expected_result = 42.09
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_duration(self):
        transportation = Walk()
        expected_result = self.path.adjusted_length() / transportation.speed
        result = self.path.duration(transportation)
        #print(result)
        self.assertAlmostEqual(result, expected_result, places=3)

    def test_progress(self):
        transportation = Walk()
        result = self.path.progress(0, transportation)
        expected_result = 0
        self.assertAlmostEqual(result, expected_result, places=2)
        duration = self.path.duration(transportation)
        result = self.path.progress(duration, transportation)
        expected_result = 1
        self.assertAlmostEqual(result, expected_result, places=2)
        result = self.path.progress(15.025, transportation)
        expected_result = 0.5
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_find_active_track(self):
        transportation = Walk()
        track, index = self.path.find_active_track(0, transportation)
        expected_result = 0
        self.assertEqual(index, expected_result)
        duration = self.path.duration(transportation)
        track, index = self.path.find_active_track(duration, transportation)
        expected_result = 1
        self.assertEqual(index, expected_result)
        track, index = self.path.find_active_track(16, transportation)
        expected_result = 1
        self.assertEqual(index, expected_result)

    def test_pos(self):
        transportation = Walk()
        pos = self.path.pos(0, transportation)
        expected_result = [-2, -2]
        self.assertListEqual(pos, expected_result)
        duration = self.path.duration(transportation)
        pos = self.path.pos(duration, transportation)
        expected_result = [20, 20]
        self.assertListEqual(pos, expected_result)
        pos = self.path.pos(15.9054, transportation)
        expected_result = [20, 0]
        self.assertAlmostEqual(pos[1], expected_result[1], places=3)


if __name__ == "__main__":
    unittest.main()