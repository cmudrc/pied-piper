import unittest
from copy import deepcopy

from piperabm.resource import Resource


class TestResourceAdd(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            },
            max_resource={
                'food': 10,
                'water': 10,
            }
        )
        self.dr = Resource(
            current_resource={
                'food': 6,
                'water': 6,
            }
        )

        self.r, self.dr = self.r + self.dr

        self.expected_r = Resource(
            current_resource={
                'food': 10,
                'water': 10,
            },
            max_resource={
                'food': 10,
                'water': 10,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )
        self.expected_dr = Resource(
            current_resource={
                'food': 1,
                'water': 4,
            },
            max_resource={
                'food': None,
                'water': None,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )

    def test_r_current(self):
        r, dr = deepcopy(self.r) + deepcopy(self.dr)
        expected_result = self.expected_r
        self.assertEqual(r, expected_result)

    def test_r_max(self):
        r = self.r
        expected_result = self.expected_r
        self.assertDictEqual(r.max_resource, expected_result.max_resource)

    def test_r_min(self):
        r = self.r
        expected_result = self.expected_r
        self.assertDictEqual(r.min_resource, expected_result.min_resource)

    def test_dr_current(self):
        dr = self.dr
        expected_result = self.expected_dr
        self.assertEqual(dr, expected_result)

    def test_dr_max(self):
        dr = self.dr
        expected_result = self.expected_dr
        self.assertDictEqual(dr.max_resource, expected_result.max_resource)

    def test_dr_min(self):
        dr = self.dr
        expected_result = self.expected_dr
        self.assertDictEqual(dr.min_resource, expected_result.min_resource)


class TestResourceSub(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            },
            max_resource={
                'food': 10,
                'water': 10,
            }
        )
        self.dr = Resource(
            current_resource={
                'food': 6,
                'water': 6,
            }
        )

        self.r, self.dr = self.r - self.dr

        self.expected_r = Resource(
            current_resource={
                'food': 0,
                'water': 2,
            },
            max_resource={
                'food': 10,
                'water': 10,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )
        self.expected_dr = Resource(
            current_resource={
                'food': 1,
                'water': 0,
            },
            max_resource={
                'food': None,
                'water': None,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        ) 

    def test_r_current(self):
        r = self.r
        expected_result = self.expected_r
        self.assertEqual(r, expected_result)
    
    def test_r_max(self):
        r = self.r
        expected_result = self.expected_r
        self.assertDictEqual(r.max_resource, expected_result.max_resource)

    def test_r_min(self):
        r = self.r
        expected_result = self.expected_r
        self.assertDictEqual(r.min_resource, expected_result.min_resource)

    def test_dr_current(self):
        dr = self.dr
        expected_result = self.expected_dr
        self.assertEqual(dr, expected_result)

    def test_dr_max(self):
        dr = self.dr
        expected_result = self.expected_dr
        self.assertDictEqual(dr.max_resource, expected_result.max_resource)

    def test_dr_min(self):
        dr = self.dr
        expected_result = self.expected_dr
        self.assertDictEqual(dr.min_resource, expected_result.min_resource)


class TestResourceMulInt(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            }
        )
        self.r = self.r * 2
        self.expected_result = Resource(
            current_resource={
                'food': 10,
                'water': 16,
            },
            max_resource={
                'food': None,
                'water': None,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )
    
    def test_r_current(self):
        r = self.r
        expected_result = self.expected_result
        self.assertEqual(r, expected_result)
    
    def test_r_max(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.max_resource, expected_result.max_resource)

    def test_r_min(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.min_resource, expected_result.min_resource)


class TestResourceMul(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            }
        )
        self.dr = Resource(
            current_resource={
                'food': 6,
                'water': 6,
            }
        )
        self.r = self.r * self.dr
        self.expected_result = Resource(
            current_resource={
                'food': 30,
                'water': 48,
            },
            max_resource={
                'food': None,
                'water': None,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )
    
    def test_r_current(self):
        r = self.r
        expected_result = self.expected_result
        self.assertEqual(r, expected_result)
    
    def test_r_max(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.max_resource, expected_result.max_resource)

    def test_r_min(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.min_resource, expected_result.min_resource)


class TestResourceDivInt(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            }
        )
        self.r = self.r / 2
        self.expected_result = Resource(
            current_resource={
                'food': 2.5,
                'water': 4,
            },
            max_resource={
                'food': None,
                'water': None,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )
    
    def test_r_current(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.current_resource, expected_result.current_resource)
    
    def test_r_max(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.max_resource, expected_result.max_resource)

    def test_r_min(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.min_resource, expected_result.min_resource)


class TestResourceDiv(unittest.TestCase):

    def setUp(self):
        self.r = Resource(
            current_resource={
                'food': 5,
                'water': 8,
            }
        )
        self.dr = Resource(
            current_resource={
                'food': 5,
                'water': 4,
            }
        )
        self.r = self.r / self.dr
        self.expected_result = Resource(
            current_resource={
                'food': 1,
                'water': 2,
            },
            max_resource={
                'food': None,
                'water': None,
            },
            min_resource={
                'food': 0,
                'water': 0,
            }
        )
    
    def test_r_current(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.current_resource, expected_result.current_resource)
    
    def test_r_max(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.max_resource, expected_result.max_resource)

    def test_r_min(self):
        r = self.r
        expected_result = self.expected_result
        self.assertDictEqual(r.min_resource, expected_result.min_resource)



if __name__ == "__main__":
    unittest.main()