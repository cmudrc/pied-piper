import unittest

from piperabm.model import Model
from piperabm.infrastructure import Junction, Settlement, Road
from piperabm.infrastructure.grammar.rules import Rule_0


class TestGrammarRule0CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Junction(pos=[0, 0])
        object.id = 0
        self.model.add(object)

    def test_0(self):
        object = Junction(pos=[0, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model)
        result = rule.check(node_id=0, other_node_id=1)
        self.assertTrue(result)

    def test_1(self):
        object = Junction(pos=[1, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model)
        result = rule.check(node_id=0, other_node_id=1)
        self.assertFalse(result)
    
    def test_2(self):
        object = Settlement(pos=[0.5, 0.5])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model)
        result = rule.check(node_id=0, other_node_id=1)
        self.assertFalse(result)


class TestGrammarRule0ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Junction(pos=[0, 0])
        object.id = 0
        self.model.add(object)

    def test_apply_0(self):
        """
        Two nodes close to each other
        """
        object = Junction(pos=[0, 0])
        object.id = 1
        self.model.add(object)
        self.assertListEqual(self.model.infrastructure_nodes, [0, 1])
        rule = Rule_0(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 1)
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 1)
        self.assertEqual(len(self.model.infrastructure_edges), 0)

    def test_apply_1(self):
        """
        Two nodes far from each other
        """
        object = Settlement(pos=[2, 2])
        object.id = 1
        self.model.add(object)
        self.assertListEqual(self.model.infrastructure_nodes, [0, 1])
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule = Rule_0(self.model)
        rule.apply()
        self.assertListEqual(self.model.infrastructure_nodes, [0, 1])
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule.apply()
        self.assertListEqual(self.model.infrastructure_nodes, [0, 1])
        self.assertEqual(len(self.model.infrastructure_edges), 0)

    def test_apply_2(self):
        """
        Three nodes close to each other.
        """
        object = Junction(pos=[0.1, 0])
        object.id = 1
        self.model.add(object)
        object = Junction(pos=[0, 0.1])
        object.id = 2
        self.model.add(object)
        self.assertListEqual(self.model.infrastructure_nodes, [0, 1, 2])
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule = Rule_0(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 2)
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 1)
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 1)
        self.assertEqual(len(self.model.infrastructure_edges), 0)

    '''
    def test_apply_3(self):
        """
        Node id replacement
        """
        object = Road(pos_1=[0.1, 0], pos_2=[10, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model)
        rule.apply()
        #self.assertTrue(0 in self.model.infrastructure_nodes)
        #road = self.model.get(1)
        #self.assertListEqual(road.pos_1, [0, 0])
        #self.assertEqual(road.id_1, 0)
    '''
    

if __name__ == "__main__":
    unittest.main()