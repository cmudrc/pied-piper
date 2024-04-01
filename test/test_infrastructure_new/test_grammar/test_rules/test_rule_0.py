import unittest

from piperabm.infrastructure_new import Infrastructure, Street
from piperabm.infrastructure_new.grammar.rules import Rule_0


class TestGrammarRule0Class_0(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        object_1 = Street(pos_1=[0, 0.1], pos_2=[0, 10])
        object_2 = Street(pos_1=[0.1, 0], pos_2=[10, 0])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.rule = Rule_0(self.infrastructure, proximity_radius=1)
        self.id_1 = self.infrastructure.find([0, 0.1])
        self.id_2 = self.infrastructure.find([0.1, 0])
        self.id_3 = self.infrastructure.find([0, 10])
        self.id_4 = self.infrastructure.find([10, 0])

    def test_check(self):
        result = self.rule.check(node_id=self.id_1, other_node_id=self.id_2)
        self.assertTrue(result)
        result = self.rule.check(node_id=self.id_1, other_node_id=self.id_3)
        self.assertFalse(result)

    def test_apply(self):
        self.assertEqual(len(self.infrastructure.junctions), 4)
        self.assertEqual(len(self.infrastructure.streets), 2)
        self.rule.apply(node_id=self.id_1, other_node_id=self.id_2)
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)

    def test_find(self):
        self.assertEqual(len(self.infrastructure.junctions), 4)
        self.assertEqual(len(self.infrastructure.streets), 2)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)
        anything_happened = self.rule.find()
        self.assertFalse(anything_happened)

        edges_id = self.infrastructure.edges_id
        object_1 = self.infrastructure.get(edges_id[0])
        object_2 = self.infrastructure.get(edges_id[1])
        self.assertEqual(object_1.pos_1, [0.05, 0.05])
        self.assertEqual(object_1.pos_2, [0, 10])
        self.assertEqual(object_2.pos_1, [0.05, 0.05])
        self.assertEqual(object_2.pos_2, [10, 0])


class TestGrammarRule0Class_1(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        object_1 = Street(pos_1=[0, 0.1], pos_2=[0, 10])
        object_2 = Street(pos_1=[0.1, 0], pos_2=[10, 0])
        object_3 = Street(pos_1=[0, 0.1], pos_2=[0.1, 0])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)
        self.rule = Rule_0(self.infrastructure, proximity_radius=1)

    def test_find(self):
        self.assertEqual(len(self.infrastructure.junctions), 6)
        self.assertEqual(len(self.infrastructure.streets), 3)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 5)
        self.assertEqual(len(self.infrastructure.streets), 3)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 4)
        self.assertEqual(len(self.infrastructure.streets), 2)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)
        anything_happened = self.rule.find()
        self.assertFalse(anything_happened)

        edges_id = self.infrastructure.edges_id
        object_1 = self.infrastructure.get(edges_id[0])
        object_2 = self.infrastructure.get(edges_id[1])
        self.assertEqual(object_1.pos_1, [0.05, 0.05])
        self.assertEqual(object_1.pos_2, [0, 10])
        self.assertEqual(object_2.pos_1, [0.05, 0.05])
        self.assertEqual(object_2.pos_2, [10, 0])


class TestGrammarRule0Class_2(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        object_1 = Street(pos_1=[0, 2], pos_2=[0, 10])
        object_2 = Street(pos_1=[2, 0], pos_2=[10, 0])
        object_3 = Street(pos_1=[0, 2], pos_2=[2, 0])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)
        self.rule = Rule_0(self.infrastructure, proximity_radius=1)

    def test_find(self):
        self.assertEqual(len(self.infrastructure.junctions), 6)
        self.assertEqual(len(self.infrastructure.streets), 3)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 5)
        self.assertEqual(len(self.infrastructure.streets), 3)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 4)
        self.assertEqual(len(self.infrastructure.streets), 3)
        anything_happened = self.rule.find()
        self.assertFalse(anything_happened)


class TestGrammarRule0Class_3(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        object_1 = Street(pos_1=[0.1, 0], pos_2=[0.5, 10])
        object_2 = Street(pos_1=[-0.1, 0], pos_2=[0, 10])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.rule = Rule_0(self.infrastructure, proximity_radius=1)
        id_1 = self.infrastructure.find([0.1, 0])
        id_2 = self.infrastructure.find([-0.1, 0])
        self.rule.apply(id_1, id_2)

    def test_find(self):
        self.assertEqual(len(self.infrastructure.junctions), 3)
        self.assertEqual(len(self.infrastructure.streets), 2)
        self.rule.find()
        self.assertEqual(len(self.infrastructure.junctions), 2)
        self.assertEqual(len(self.infrastructure.streets), 1)
        anything_happened = self.rule.find()
        self.assertFalse(anything_happened)
    

if __name__ == "__main__":
    unittest.main()