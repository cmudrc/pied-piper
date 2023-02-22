import unittest
from copy import deepcopy

from piperabm.resource import Resource, DeltaResource
from piperabm.measure import Accessibility
from piperabm.unit import DT


class TestAccessibilityClass(unittest.TestCase):

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
    accessibility = Accessibility()
    duration = DT(seconds=10).total_seconds()

    r1_d_current = r1.to_delta_resource()
    r2_d_current = r2.to_delta_resource()
    current_resources = r1_d_current + r2_d_current
    r1_d_max = DeltaResource(batch=r1.max_resource)
    r2_d_max = DeltaResource(batch=r2.max_resource)
    max_resources = r1_d_max + r2_d_max
    accessibility.add(current_resources, max_resources, duration)

    r2_d_current /= 2
    r1.current_resource['food'] += 5
    r1_d_current = r1.to_delta_resource()
    current_resources = r1_d_current + r2_d_current
    r1_d_max = DeltaResource(batch=r1.max_resource)
    r2_d_max = DeltaResource(batch=r2.max_resource)
    max_resources = r1_d_max + r2_d_max
    accessibility.add(current_resources, max_resources, duration)

    r1_d_current *= 1.2
    r2_d_current *= 1.2
    current_resources = r1_d_current + r2_d_current
    r1_d_max = DeltaResource(batch=r1.max_resource)
    r2_d_max = DeltaResource(batch=r2.max_resource)
    max_resources = r1_d_max + r2_d_max
    accessibility.add(current_resources, max_resources, duration)

    def test_calculate(self):
        acc = deepcopy(self.accessibility)
        efficiency = acc.calculate()
        expected_result = {
            'food': 0.5,
            'water': 0.405,
            'energy': 0.49333333333333335,
        }
        self.assertDictEqual(efficiency.batch, expected_result)

    def test_show(self):
        acc = deepcopy(self.accessibility)
        #acc.to_plt('water')
        #acc.show('water')


if __name__ == "__main__":
    unittest.main()
