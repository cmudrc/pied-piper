import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.model.samples import model_0
from piperabm.infrastructure import Junction, Road


class TestGrammarRule1Class(unittest.TestCase):

    def test_0(self):
        """
        A single settlement node
        """
        model = deepcopy(model_0)
        self.assertEqual(len(model.all_environment_nodes), 1)
        self.assertEqual(len(model.all_environment_edges), 0)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 1)
        self.assertEqual(len(model.all_environment_edges), 0)
    
    def test_1(self):
        """
        Add one junction node near an existing settlement node
        """
        model = deepcopy(model_0)
        new_item = Junction(pos=[0, 0.05])
        model.add(new_item)
        self.assertEqual(len(model.all_environment_nodes), 2)
        self.assertEqual(len(model.all_environment_edges), 0)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 1)
        self.assertEqual(len(model.all_environment_edges), 0)
    
    def test_2(self):
        """
        Add two junction nodes near an existing settlement node
        """
        model = deepcopy(model_0)
        new_item_1 = Junction(pos=[0, 0.05])
        new_item_2 = Junction(pos=[0.05, 0])
        model.add(new_item_1)
        model.add(new_item_2)
        self.assertEqual(len(model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 0)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 1)
        self.assertEqual(len(model.all_environment_edges), 0)
    
    def test_3(self):
        """
        Add a road edge crossing an existing junction
        """
        model = deepcopy(model_0)
        new_item = Road(pos_1=[-1, -1], pos_2=[1, 1])
        model.add(new_item)
        self.assertEqual(len(model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 1)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 2)

    def test_4(self):
        """
        Add a road edge crossing an existing road edge
        """
        model = Model(proximity_radius=0.1)
        new_item_1 = Road(pos_1=[0, 0], pos_2=[2, 2])
        new_item_2 = Road(pos_1=[2, 0], pos_2=[0, 2])
        model.add(new_item_1)
        model.add(new_item_2)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 2)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 5)
        self.assertEqual(len(model.all_environment_edges), 4)

    def test_5(self):
        """
        Add a road edge crossing two nodes
        """
        model = Model(proximity_radius=0.1)
        new_item_1 = Road(pos_1=[-2, -2], pos_2=[2, 2])
        new_item_2 = Junction(pos=[-1, -1])
        new_item_3 = Junction(pos=[1, 1])
        model.add(new_item_1)
        model.add(new_item_2)
        model.add(new_item_3)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 1)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 3)

    def test_6(self):
        """
        Add a road edge crossing both ends of an existing road edge
        """
        model = Model(proximity_radius=0.1)
        new_item_1 = Road(pos_1=[-1, -1], pos_2=[1, 1])
        new_item_2 = Road(pos_1=[-2, -2], pos_2=[2, 2])
        model.add(new_item_1)
        model.add(new_item_2)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 2)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 3)

    def test_7(self):
        """
        Add two edges with same start and ending
        """
        model = Model(proximity_radius=0.1)
        new_item_1 = Road(pos_1=[-1.05, -1], pos_2=[1, 1])
        new_item_2 = Road(pos_1=[-1, -1], pos_2=[1, 1])
        model.add(new_item_1)
        model.add(new_item_2)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 2)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 2)
        self.assertEqual(len(model.all_environment_edges), 1)

    def test_8(self):
        """
        Add two edges with same start and ending
        """
        model = Model(proximity_radius=0.1)
        new_item_1 = Road(pos_1=[-1.05, -1], pos_2=[1, 1])
        new_item_2 = Road(pos_1=[-1, -1], pos_2=[1, 1])
        model.add(new_item_1)
        model.add(new_item_2)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 2)
        model.apply_infrastructure_grammars()
        self.assertEqual(len(model.all_environment_nodes), 2)
        self.assertEqual(len(model.all_environment_edges), 1)
    

if __name__ == "__main__":
    unittest.main()