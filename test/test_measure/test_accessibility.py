import unittest
from copy import deepcopy

from piperabm.resource import Resource
from piperabm.measure import Accessibility
from piperabm.unit import DT


class TestAccessibilityClass(unittest.TestCase):

    def setUp(self):
        self.accessibility = Accessibility()

        r1 = Resource(
            current_resource={
                'food': 2,
                'water': 3,
                'energy': 4
            },
            max_resource={
                'food': 10,
                'water': 10,
                'energy': 10
            }
        )
        r2 = Resource(
            current_resource={
                'food': 6,
                'water': 7,
                'energy': 8
            },
            max_resource={
                'food': 10,
                'water': 10,
                'energy': 10
            }
        )
        
        duration = 10 # seconds

        ## Entry 1:
        r1_d_current = r1.val()
        r2_d_current = r2.val()
        current_resources, _ = r1_d_current + r2_d_current
        r1_d_max = r1.val('max')
        r2_d_max = r2.val('max')
        max_resources, _ = r1_d_max + r2_d_max
        self.accessibility.add(current_resources, max_resources, duration)
        #print(current_resources, max_resources, duration)

        ## Entry 2:
        r2_d_current /= 2
        r1.current_resource['food'] += 5
        r1_d_current = r1.val()
        current_resources, _ = r1_d_current + r2_d_current
        r1_d_max = Resource(r1.max_resource)
        r2_d_max = Resource(r2.max_resource)
        max_resources, _ = r1_d_max + r2_d_max
        self.accessibility.add(current_resources, max_resources, duration)
        #print(current_resources, max_resources, duration)

        ## Entry 3:
        r1_d_current *= 1.2
        r2_d_current *= 1.2
        current_resources, _ = r1_d_current + r2_d_current
        r1_d_max = Resource(r1.max_resource)
        r2_d_max = Resource(r2.max_resource)
        max_resources, _ = r1_d_max + r2_d_max
        self.accessibility.add(current_resources, max_resources, duration)
        #print(current_resources, max_resources, duration)

        #accessibility.show('water')

    def test_calculate(self):
        acc = deepcopy(self.accessibility)
        efficiency = acc.efficiency()
        expected_result = {
            'food': 0.5,
            'water': 0.405,
            'energy': 0.49333333333333335,
        }
        self.assertDictEqual(efficiency.current_resource, expected_result)


if __name__ == "__main__":
    unittest.main()
