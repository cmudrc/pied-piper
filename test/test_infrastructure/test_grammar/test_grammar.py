import unittest

from piperabm.infrastructure import Infrastructure
from piperabm.infrastructure.grammar import Grammar


class TestInfrastructureGrammarClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0.1, 0], pos_2=[10, 0])
        self.infrastructure.add_street(pos_1=[0, 0.1], pos_2=[0, 10])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 2)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 3)
        self.assertEqual(stat['edge']['street'], 2)
        self.assertTrue(self.infrastructure.baked)

    def test_apply_1(self):
        self.infrastructure.add_street(pos_1=[0.1, 0], pos_2=[0, 0.1])
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 6)
        self.assertEqual(stat['edge']['street'], 3)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 3)
        self.assertEqual(stat['edge']['street'], 2)
        self.assertTrue(self.infrastructure.baked)

    def test_apply_2(self):
        self.infrastructure.add_street(pos_1=[0.1, 0], pos_2=[0, 0.1])
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[-10, 0])
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 8)
        self.assertEqual(stat['edge']['street'], 4)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 3)
        self.assertTrue(self.infrastructure.baked)


class TestInfrastructureGrammarClass_1(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[2, 0], pos_2=[10, 0])
        self.infrastructure.add_street(pos_1=[0, 2], pos_2=[0, 10])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 2)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 2)
        self.assertTrue(self.infrastructure.baked)

    def test_apply_1(self):
        self.infrastructure.add_street(pos_1=[2, 0], pos_2=[0, 2])
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 6)
        self.assertEqual(stat['edge']['street'], 3)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 3)
        self.assertTrue(self.infrastructure.baked)


class TestInfrastructureGrammarClass_2(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_street(pos_1=[0, 5], pos_2=[0, -5])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 2)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 3)
        self.assertTrue(self.infrastructure.baked)


class TestInfrastructureGrammarClass_3(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_street(pos_1=[0.1, 5], pos_2=[0.1, -5])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 2)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 3)
        self.assertTrue(self.infrastructure.baked)


class TestInfrastructureGrammarClass_4(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_street(pos_1=[-0.1, 5], pos_2=[-0.1, -5])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 2)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 4)
        self.assertEqual(stat['edge']['street'], 3)
        self.assertTrue(self.infrastructure.baked)


class TestInfrastructureGrammarClass_5(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[-2, 2])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 0)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 1)
        self.assertTrue(self.infrastructure.baked)


class TestInfrastructureGrammarClass_6(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[2, 2])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 0)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 3)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 2)
        self.assertEqual(stat['edge']['neighborhood_access'], 1)
        self.assertTrue(self.infrastructure.baked_streets)


class TestInfrastructureGrammarClass_7(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[0.1, 2])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 0)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 3)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 2)
        self.assertEqual(stat['edge']['neighborhood_access'], 1)
        self.assertTrue(self.infrastructure.baked_streets)


class TestInfrastructureGrammarClass_8(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[-0.1, 2])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 0)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 1)
        self.assertTrue(self.infrastructure.baked_streets)


class TestInfrastructureGrammarClass_9(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[0, 0])

    def test_apply_0(self):
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 0)
        self.infrastructure.bake(report=False)
        stat = self.infrastructure.stat
        self.assertEqual(stat['node']['junction'], 2)
        self.assertEqual(stat['node']['home'], 1)
        self.assertEqual(stat['edge']['street'], 1)
        self.assertEqual(stat['edge']['neighborhood_access'], 1)
        self.assertTrue(self.infrastructure.baked_streets)


if __name__ == "__main__":
    unittest.main()