import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.samples import environment_0
from piperabm.environment.items import Junction, Settlement, Road


class TestGrammarRule1Class(unittest.TestCase):

    def test_0(self):
        """
        A single settlement node
        """

        env = deepcopy(environment_0)
        env_copy = deepcopy(env)

        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)
        
        ''' apply step by step '''
        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply all '''
        env_copy.apply_grammars()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

    def test_1(self):
        """
        Add one junction node near an existing settlement node
        """
        env = deepcopy(environment_0)
        new_item = Junction(pos=[0, 0.05])
        env.add(new_item)
        env_copy = deepcopy(env)

        self.assertEqual(len(env.all_nodes), 2)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply step by step '''
        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply all '''
        env_copy.apply_grammars()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

    def test_2(self):
        """
        Add two junction nodes near an existing settlement node
        """
        env = deepcopy(environment_0)
        new_item_1 = Junction(pos=[0, 0.05])
        new_item_2 = Junction(pos=[0.05, 0])
        env.add(new_item_1)
        env.add(new_item_2)
        env_copy = deepcopy(env)

        self.assertEqual(len(env.all_nodes), 3)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply step by step '''
        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply all '''
        env_copy.apply_grammars()
        self.assertEqual(len(env.all_nodes), 1)
        self.assertEqual(len(env.all_edges), 0)

    def test_3(self):
        """
        Add one settlement node near an existing settlement node
        """
        env = deepcopy(environment_0)
        new_item = Settlement(pos=[0, 0.05])
        env.add(new_item)
        env_copy = deepcopy(env)

        self.assertEqual(len(env.all_nodes), 2)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply step by step '''
        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 2)
        self.assertEqual(len(env.all_edges), 0)

        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 2)
        self.assertEqual(len(env.all_edges), 0)

        ''' apply all '''
        env_copy.apply_grammars()
        self.assertEqual(len(env.all_nodes), 2)
        self.assertEqual(len(env.all_edges), 0)

    def test_4(self):
        """
        Add a road edge crossing an existing junction
        """
        env = deepcopy(environment_0)
        new_item = Road(pos_1=[-1, -1], pos_2=[1, 1])
        env.add(new_item)
        env_copy = deepcopy(env)

        self.assertEqual(len(env.all_nodes), 3)
        self.assertEqual(len(env.all_edges), 1)

        ''' apply step by step '''
        env.grammar_rule_2()
        self.assertEqual(len(env.all_nodes), 7)
        self.assertEqual(len(env.all_edges), 2)

        env.grammar_rule_2()
        self.assertEqual(len(env.all_nodes), 7)
        self.assertEqual(len(env.all_edges), 2)

        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 3)
        self.assertEqual(len(env.all_edges), 2)

        ''' apply all '''
        env_copy.apply_grammars()
        self.assertEqual(len(env.all_nodes), 3)
        self.assertEqual(len(env.all_edges), 2)

    def test_5(self):
        """
        Add a road edge crossing an existing road edge
        """
        env = Environment(proximity_radius=0.1)
        new_item_1 = Road(pos_1=[0, 0], pos_2=[2, 2])
        new_item_2 = Road(pos_1=[2, 0], pos_2=[0, 2])
        env.add(new_item_1)
        env.add(new_item_2)
        env_copy = deepcopy(env)

        self.assertEqual(len(env.all_nodes), 4)
        self.assertEqual(len(env.all_edges), 2)

        ''' apply step by step '''
        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 4)
        self.assertEqual(len(env.all_edges), 2)

        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 4)
        self.assertEqual(len(env.all_edges), 2)

        env.grammar_rule_2()
        self.assertEqual(len(env.all_nodes), 4)
        self.assertEqual(len(env.all_edges), 2)

        env.grammar_rule_2()
        self.assertEqual(len(env.all_nodes), 4)
        self.assertEqual(len(env.all_edges), 2)

        env.grammar_rule_3()
        self.assertEqual(len(env.all_nodes), 12)
        self.assertEqual(len(env.all_edges), 4)

        env.grammar_rule_1()
        self.assertEqual(len(env.all_nodes), 5)
        self.assertEqual(len(env.all_edges), 4)

        env.grammar_rule_2()
        self.assertEqual(len(env.all_nodes), 5)
        self.assertEqual(len(env.all_edges), 4)

        env.grammar_rule_3()
        self.assertEqual(len(env.all_nodes), 5)
        self.assertEqual(len(env.all_edges), 4)

        env.grammar_rule_3()
        self.assertEqual(len(env.all_nodes), 5)
        self.assertEqual(len(env.all_edges), 4)

        ''' apply all '''
        env_copy.apply_grammars()
        self.assertEqual(len(env.all_nodes), 5)
        self.assertEqual(len(env.all_edges), 4)


if __name__ == '__main__':
    unittest.main()