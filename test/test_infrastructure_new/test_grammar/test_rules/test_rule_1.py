import unittest

from piperabm.infrastructure_new import Infrastructure, Junction, Street, Home
from piperabm.infrastructure_new.grammar.rules import Rule_1


class TestGrammarRule1Class_Check(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object = Street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add(object)

    def test_check_0(self):
        object = Junction(pos=[0, 0])
        id_1 = self.infrastructure.add(object)
        id_2 = self.infrastructure.edges_id[0]
        rule = Rule_1(self.infrastructure)
        result = rule.check(node_id=id_1, edge_id=id_2)
        self.assertFalse(result)
    
    def test_check_1(self):
        object = Junction(pos=[-0.5, 0.5])
        id_1 = self.infrastructure.add(object)
        id_2 = self.infrastructure.edges_id[0]
        rule = Rule_1(self.infrastructure)
        result = rule.check(node_id=id_1, edge_id=id_2)
        self.assertFalse(result)
    
    def test_check_2(self):
        object = Junction(pos=[0.5, 0.5])
        id_1 = self.infrastructure.add(object)
        id_2 = self.infrastructure.edges_id[0]
        rule = Rule_1(self.infrastructure)
        result = rule.check(node_id=id_1, edge_id=id_2)
        self.assertFalse(result)
    
    def test_check_3(self):
        object = Home(pos=[3, 0.5])
        id_1 = self.infrastructure.add(object)
        id_2 = self.infrastructure.edges_id[0]
        rule = Rule_1(self.infrastructure)
        result = rule.check(node_id=id_1, edge_id=id_2)
        self.assertTrue(result) # Won't happen in run
    
    def test_check_4(self):
        object = Junction(pos=[3, 0.5])
        id_1 = self.infrastructure.add(object)
        id_2 = self.infrastructure.edges_id[0]
        rule = Rule_1(self.infrastructure)
        result = rule.check(node_id=id_1, edge_id=id_2)
        self.assertTrue(result)
    
    def test_check_5(self):
        object = Junction(pos=[3, 3])
        id_1 = self.infrastructure.add(object)
        id_2 = self.infrastructure.edges_id[0]
        rule = Rule_1(self.infrastructure)
        result = rule.check(node_id=id_1, edge_id=id_2)
        self.assertFalse(result)


class TestGrammarRule1Class_0(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Junction(pos=[3, 0.5])
        object_2 = Street(pos_1=[0, 0], pos_2=[10, 0])
        self.id_1 = self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.rule = Rule_1(self.infrastructure)

    def test_apply(self):
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 1)
        id_2 = self.infrastructure.streets[0]
        self.rule.apply(node_id=self.id_1, edge_id=id_2)
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)

    def test_find(self):
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 1)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)
        anything_happened = self.rule.find()
        self.assertFalse(anything_happened)

        edges_id = self.infrastructure.edges_id
        object_1 = self.infrastructure.get(edges_id[0])
        object_2 = self.infrastructure.get(edges_id[1])
        self.assertEqual(object_1.pos_1, [0, 0])
        self.assertEqual(object_1.pos_2, [3, 0.5])
        self.assertEqual(object_2.pos_1, [3, 0.5])
        self.assertEqual(object_2.pos_2, [10, 0])
        #self.infrastructure.show()

        
if __name__ == "__main__":
    unittest.main()