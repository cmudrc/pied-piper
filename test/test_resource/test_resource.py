import unittest
from copy import deepcopy

from piperabm.resource import Resource, DeltaResource


class TestResourceClass(unittest.TestCase):

    r = Resource(
        current_resource={
            'food': 5,
            'water': 8,
        },
        max_resource={
            'food': 10,
            'water': 10,
        }
    )

    def test_resource_add_0(self):
        """
        DeltaResource with 1 entry
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 2,
        })
        r, remaining = r + dr
        expected_result = {
            'food': 7,
            'water': 8
        }
        self.assertDictEqual(r.current_resource, expected_result)
        expected_result = {
            'food': 0,
            'water': 0
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_resource_add_1(self):
        """
        DeltaResource with 2 entries
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 2,
            'water': 2
        })
        r, remaining = r + dr
        expected_result = {
            'food': 7,
            'water': 10
        }
        self.assertDictEqual(r.current_resource, expected_result)
        expected_result = {
            'food': 0,
            'water': 0
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_resource_add_2(self):
        """
        Add more than capacity
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 2,
            'water': 3
        })
        r, remaining = r + dr
        expected_result = {
            'food': 7,
            'water': 10
        }
        self.assertDictEqual(r.current_resource, expected_result)
        expected_result = {
            'food': 0,
            'water': 1
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_resource_add_amount_0(self):
        """
        Test add_amount function
        """
        r = deepcopy(self.r)
        remaining = r.add_amount(
            name='food',
            amount=2
        )
        self.assertEqual(r.amount('food'), 7)
        self.assertEqual(remaining, 0)

    def test_resource_add_amount_1(self):
        """
        Test add_amount function
        """
        r = deepcopy(self.r)
        remaining = r.add_amount(
            name='food',
            amount=8
        )
        self.assertEqual(r.amount('food'), 10)
        self.assertEqual(remaining, 3)

    def test_resource_add_amount_2(self):
        """
        Test add_amount function
        """
        r = deepcopy(self.r)
        remaining = r.add_amount(
            name='food',
            amount=10
        )
        self.assertEqual(r.amount('food'), 10)
        self.assertEqual(remaining, 5)

    def test_resource_sub_0(self):
        """
        DeltaResource with 1 entry
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 2,
        })
        r, remaining = r - dr
        expected_result = {
            'food': 3,
            'water': 8
        }
        self.assertDictEqual(r.current_resource, expected_result)
        expected_result = {
            'food': 0,
            'water': 0
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_resource_sub_1(self):
        """
        DeltaResource with 2 entries
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 2,
            'water': 3
        })
        r, remaining = r - dr
        expected_result = {
            'food': 3,
            'water': 5,
        }
        self.assertDictEqual(r.current_resource, expected_result)
        expected_result = {
            'food': 0,
            'water': 0
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_resource_sub_2(self):
        """
        Subtract more than capacity
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 10,
            'water': 10
        })
        r, remaining = r - dr
        expected_result = {
            'food': 0,
            'water': 0
        }
        self.assertDictEqual(r.current_resource, expected_result)
        expected_result = {
            'food': 5,
            'water': 2
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_resource_sub_3(self):
        r = deepcopy(self.r)
        remaining = r.add_amount(
            name='food',
            amount=2
        )
        self.assertEqual(r.amount('food'), 7)
        self.assertEqual(remaining, 0)

    def test_resource_sub_amount_0(self):
        """
        Test add_amount function
        """
        r = deepcopy(self.r)
        remaining = r.sub_amount(
            name='food',
            amount=2
        )
        self.assertEqual(r.amount('food'), 3)
        self.assertEqual(remaining, 0)

    def test_resource_sub_amount_1(self):
        """
        Test add_amount function
        """
        r = deepcopy(self.r)
        remaining = r.sub_amount(
            name='food',
            amount=8
        )
        self.assertEqual(r.amount('food'), 0)
        self.assertEqual(remaining, 3)

    def test_resource_sub_amount_2(self):
        """
        Test add_amount function
        """
        r = deepcopy(self.r)
        remaining = r.sub_amount(
            name='food',
            amount=10
        )
        self.assertEqual(r.amount('food'), 0)
        self.assertEqual(remaining, 5)

    def test_mixed_case(self):
        r = Resource(
            current_resource={
                'food': 5,
                'water': 2,
            },
            max_resource={
                'food': 10,
                'water': 10,
            }
        )
        dr1 = DeltaResource({
            'water': 2,
        })
        dr2 = DeltaResource({
            'food': 6,
        })
        dr = dr2-dr1
        expected_result = {
            'food': 6,
            'water': -2,
        }
        self.assertDictEqual(dr.batch, expected_result)
        result, remaining = r-dr
        expected_result = {
            'food': 0,
            'water': 4,
        }
        self.assertDictEqual(result.current_resource, expected_result)
        expected_result = {
            'food': 1,
            'water': 0,
        }
        self.assertDictEqual(remaining.batch, expected_result)

    def test_true_div_0(self):
        """
        Test __truediv__
        """
        r = deepcopy(self.r)
        dr = DeltaResource({
            'food': 2,
        })
        result = r / dr
        expected_result = {
            'food': 2.5,
        }
        self.assertDictEqual(result, expected_result)

    def test_amount(self):
        r = deepcopy(self.r)
        self.assertEqual(r.amount('food'), r.current_resource['food'])

    def test_demand(self):
        r = deepcopy(self.r)
        result = r.demand()
        expected_result = {
            'food': 5,
            'water': 2,
        }
        self.assertDictEqual(result.batch, expected_result)


class TestDeltaResourceClass(unittest.TestCase):

    dr1 = DeltaResource({
        'food': 5,
        'water': 8,
    })

    def test_delta_resource_0(self):
        dr1 = deepcopy(self.dr1)
        dr2 = DeltaResource({
            'food': 6,
        })
        dr = dr1 + dr2
        expected_result = {
            'food': 11,
            'water': 8,
        }
        self.assertDictEqual(dr.batch, expected_result)

    def test_delta_resource_1(self):
        dr1 = deepcopy(self.dr1)
        dr2 = DeltaResource({
            'food': 6,
        })
        dr = dr1 - dr2
        expected_result = {
            'food': -1,
            'water': 8,
        }
        self.assertDictEqual(dr.batch, expected_result)

    def test_delta_resource_2(self):
        dr1 = deepcopy(self.dr1)
        dr = dr1 * 2
        expected_result = {
            'food': 10,
            'water': 16,
        }
        self.assertDictEqual(dr.batch, expected_result)

    def test_delta_resource_3(self):
        dr1 = deepcopy(self.dr1)
        dr = dr1 / 2
        expected_result = {
            'food': 2.5,
            'water': 4,
        }
        self.assertDictEqual(dr.batch, expected_result)


if __name__ == "__main__":
    unittest.main()