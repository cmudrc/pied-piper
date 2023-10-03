import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0, environment_1
from piperabm.environment.items import Junction, Road
from piperabm.time import Date


class TestGrammarRule1Class(unittest.TestCase):

    def setUp(self):
        self.date_start = Date(2020, 1, 1)
        self.date_end = Date(2020, 1, 2)

    def test_0(self):
        """
        A single node
        """
        env = deepcopy(environment_0)
        infrastrucure = env.to_infrastrucure_graph(self.date_start, self.date_end)
        infrastrucure_copy = deepcopy(infrastrucure)

        ''' apply rules step by step '''
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

        ''' apply all rules '''
        infrastrucure_copy.apply_grammars()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

    def test_1(self):
        """
        Add one node near an existing node
        """
        env = deepcopy(environment_0)
        new_item = Junction(pos=[0, 0.05])
        env.add(new_item)
        infrastrucure = env.to_infrastrucure_graph(self.date_start, self.date_end)
        infrastrucure_copy = deepcopy(infrastrucure)

        ''' apply rules step by step '''
        self.assertEqual(len(infrastrucure.all_nodes()), 2)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

        ''' apply all rules '''
        infrastrucure_copy.apply_grammars()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

    def test_2(self):
        """
        Add two nodes near an existing node
        """
        env = deepcopy(environment_0)
        new_item_1 = Junction(pos=[0, 0.05])
        new_item_2 = Junction(pos=[0.05, 0])
        env.add(new_item_1)
        env.add(new_item_2)
        infrastrucure = env.to_infrastrucure_graph(self.date_start, self.date_end)
        infrastrucure_copy = deepcopy(infrastrucure)

        ''' apply rules step by step '''
        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

        ''' apply all rules '''
        infrastrucure_copy.apply_grammars()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)


class TestGrammarRule2Class(unittest.TestCase):

    def setUp(self):
        self.date_start = Date(2020, 1, 1)
        self.date_end = Date(2020, 1, 2)

    def test_0(self):
        """
        A single node
        """
        env = deepcopy(environment_0)
        infrastrucure = env.to_infrastrucure_graph(self.date_start, self.date_end)
        infrastrucure_copy = deepcopy(infrastrucure)

        ''' apply rules step by step '''
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_2()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)
        infrastrucure.grammar_rule_2()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

        ''' apply all rules '''
        infrastrucure_copy.apply_grammars()
        self.assertEqual(len(infrastrucure.all_nodes()), 1)
        self.assertEqual(len(infrastrucure.all_edges()), 0)

    def test_1(self):
        """
        Add one edge near an existing node
        """
        env = deepcopy(environment_0)
        new_item = Road(pos_1=[-1, -1], pos_2=[1, 1])
        env.add(new_item)
        infrastrucure = env.to_infrastrucure_graph(self.date_start, self.date_end)
        infrastrucure_copy = deepcopy(infrastrucure)

        ''' apply rules step by step '''
        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 1)
        
        infrastrucure.grammar_rule_2()
        all_edges = infrastrucure.all_edges()
        #print(infrastrucure.get_edge_item(*all_edges[0]))
        #print(infrastrucure.get_edge_item(*all_edges[1]))

        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 2)
        all_edges = infrastrucure.all_edges()
        #print(infrastrucure.get_edge_item(*all_edges[0]))
        #print(infrastrucure.get_edge_item(*all_edges[1]))
        infrastrucure.grammar_rule_2()
        #infrastrucure.show()
        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 2)

        ''' apply all rules '''
        infrastrucure_copy.apply_grammars()
        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 2)
        
'''
class TestGrammarClass_1(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_to_infrastrucure_graph(self):
        env = deepcopy(self.env)
        date_start = Date(2020, 1, 1)
        date_end = Date(2020, 1, 2)
        infrastrucure = env.to_infrastrucure_graph(date_start, date_end)
        infrastrucure.apply_grammars()
        self.assertEqual(len(infrastrucure.all_nodes()), 2)
        self.assertEqual(len(infrastrucure.all_edges()), 1)

    def test_add_edge_near_node(self):
        env = deepcopy(self.env)
        item = Road(
            pos_1=[-2, 2],
            pos_2=[2, -2]
        )
        env.add(item)
        date_start = Date(2020, 1, 1)
        date_end = Date(2020, 1, 2)
        infrastrucure = env.to_infrastrucure_graph(date_start, date_end)

        infrastrucure.grammar_rule_1()
        self.assertEqual(len(infrastrucure.all_nodes()), 4)
        self.assertEqual(len(infrastrucure.all_edges()), 2)

        infrastrucure.grammar_rule_2()
        self.assertEqual(len(infrastrucure.all_nodes()), 4)
        self.assertEqual(len(infrastrucure.all_edges()), 3)

    def test_add_node_near_edge(self):
        env = deepcopy(self.env)
        item = Junction(pos=[1, 1])
        env.add(item)
        date_start = Date(2020, 1, 1)
        date_end = Date(2020, 1, 2)
        infrastrucure = env.to_infrastrucure_graph(date_start, date_end)
        infrastrucure_copy = deepcopy(infrastrucure)

        infrastrucure.grammar_rule_1()
        #infrastrucure.show()
        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 1)

        infrastrucure.grammar_rule_2()
        #infrastrucure.show()
        self.assertEqual(len(infrastrucure.all_nodes()), 3)
        self.assertEqual(len(infrastrucure.all_edges()), 2)

        infrastrucure_copy.apply_grammars()
        #self.assertEqual(len(infrastrucure_copy.all_nodes()), 3)
        #self.assertEqual(len(infrastrucure_copy.all_edges()), 2)
        infrastrucure_copy.show()
'''

if __name__ == '__main__':
    unittest.main()