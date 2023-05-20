import unittest
from copy import deepcopy

from piperabm.society.samples import society_0, society_1


class TestSocietyClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.society = deepcopy(society_0)

    def test_all_indexes(self):
        nodes = self.society.all_indexes()
        self.assertListEqual(nodes, [0])

    def test_all_edges(self):
        edges = self.society.all_edges()
        self.assertListEqual(edges, [])

    def test_get_pos(self):
        pos = self.society.get_agent_pos(0)
        self.assertListEqual(pos, [-2, -2])

    def test_find(self):
        agent_index = self.society.find('John')
        self.assertEqual(agent_index, 0)
        agent_index = self.society.find(0)
        self.assertEqual(agent_index, 0)

    def test_bindings(self):
        self.assertEqual(self.society.environment.type, 'environment')
        self.assertEqual(self.society.environment.society.type, 'society')
        agent = self.society.get_agent_object(0)
        self.assertEqual(agent.environment.type, 'environment')
        self.assertEqual(agent.environment.society.type, 'society')        
        print(agent.queue.society.type)


class TestSocietyClass_1(unittest.TestCase):

    def setUp(self) -> None:
        self.society = deepcopy(society_1)

    def test_all_indexes(self):
        nodes = self.society.all_indexes()
        self.assertListEqual(nodes, [0, 1])

    def test_all_edges(self):
        edges = self.society.all_edges()
        self.assertListEqual(edges, [(0, 1)])

    def test_relationship(self):
        relationships = self.society.get_relationship_object(0, 1)
        self.assertListEqual(list(relationships.keys()), ['family', 'fellow citizen'])

        expected_result = {
            'type': 'family',
            'start_date': {'year': 2020, 'month': 1, 'day': 4, 'hour': 0, 'minute': 0, 'second': 0},
            'end_date': None,
            'distance': 0.0,
        }
        self.assertDictEqual(relationships['family'].to_dict(), expected_result)

        expected_result = {
            'type': 'fellow citizen',
            'start_date': {'year': 2020, 'month': 1, 'day': 4, 'hour': 0, 'minute': 0, 'second': 0},
            'end_date': None,
            'distance': 0.0
        }
        self.assertDictEqual(relationships['fellow citizen'].to_dict(), expected_result)


if __name__ == "__main__":
    unittest.main()