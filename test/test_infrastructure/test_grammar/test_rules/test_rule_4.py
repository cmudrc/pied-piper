import unittest

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.infrastructure.grammar.rules import Rule_4


class TestGrammarRule4CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)

    def test_0(self):
        object = Settlement(pos=[5, 4])
        object.id = 1
        self.model.add(object)
        rule = Rule_4(self.model.infrastructure)
        result, smallest_distance_vector = rule.check(node_id=1)
        self.assertTrue(result)
        self.assertListEqual(smallest_distance_vector, [0, -4])
    
    def test_1(self):
        object = Settlement(pos=[5, 1])
        object.id = 1
        self.model.add(object)
        rule = Rule_4(self.model.infrastructure)
        result, smallest_distance_vector = rule.check(node_id=1)
        self.assertFalse(result)
        self.assertListEqual(smallest_distance_vector, [0, -1])

    def test_2(self):
        object = Settlement(pos=[5, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_4(self.model.infrastructure)
        result, smallest_distance_vector = rule.check(node_id=1)
        self.assertFalse(result)
        self.assertListEqual(smallest_distance_vector, [0, 0])

    def test_3(self):
        object = Settlement(pos=[-2, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_4(self.model.infrastructure)
        result, smallest_distance_vector = rule.check(node_id=1)
        self.assertTrue(result)
        self.assertListEqual(smallest_distance_vector, [2, 0])

    def test_4(self):
        object = Settlement(pos=[-1, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_4(self.model.infrastructure)
        result, smallest_distance_vector = rule.check(node_id=1)
        self.assertFalse(result)
        self.assertListEqual(smallest_distance_vector, [1, 0])

    def test_4(self):
        object = Settlement(pos=[-2, -2])
        object.id = 1
        self.model.add(object)
        rule = Rule_4(self.model.infrastructure)
        result, smallest_distance_vector = rule.check(node_id=1)
        self.assertTrue(result)
        self.assertListEqual(smallest_distance_vector, [2, 2])


class TestGrammarRule4ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)
    '''
    def test_apply(self):
        object = Settlement(pos=[5, 4])
        object.id = 1
        self.model.add(object)
        self.assertEqual(len(self.model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 1)
        rule = Rule_4(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 5)
        self.assertEqual(len(model.all_environment_edges), 2)
    '''  

if __name__ == "__main__":
    unittest.main()