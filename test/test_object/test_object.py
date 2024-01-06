import unittest
from copy import deepcopy

from piperabm.object import PureObject


class TestObjectClass(unittest.TestCase):

    def setUp(self) -> None:
        
        class A(PureObject):

            def __init__(self, val=None):
                super().__init__()
                self.val = val
            
            def serialize(self) -> dict:
                dictionary = {}
                dictionary['val'] = self.val
                return dictionary

            def deserialize(self, dictionary: dict) -> None:
                self.val = dictionary['val']
        
        self.ClassA = A
        self.a = self.ClassA(val=5)
        self.a_new = self.ClassA(val=7)
    
    def test_str(self):
        txt = str(self.a)
        self.assertEqual(txt, "{'val': 5}")

    def test_serialize(self):
        dictionary = self.a.serialize()
        self.assertDictEqual(dictionary, {'val': 5})

    def test_deserialize(self):
        new_instance = self.ClassA()
        new_instance.deserialize(dictionary={'val': 5})
        self.assertDictEqual(new_instance.serialize(), {'val': 5})

    def test_create_delta(self):
        delta = self.a_new.create_delta(old=self.a)
        self.assertDictEqual(delta, {'val': 2})

    def test_apply_delta(self):
        a = deepcopy(self.a)
        a.apply_delta(delta={'val': 2})
        self.assertEqual(a, self.a_new)


if __name__ == "__main__":
    unittest.main()
    