import unittest

from piperabm.tools import ElementExists
from piperabm.unit import Date


class TestElementExistsClass(unittest.TestCase):
    """
    Guide:
        item: [start--end]
        timeline: --|start----end|--
        days on timeline: 1-2-3|-4-5-|6-7-8
    """
    ee = ElementExists()

    time_start = Date(2020, 1, 3)
    time_end = Date(2020, 1, 6)

    def test_0(self):
        """
        -[ ]-|--|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 1)
        item_end = Date(2020, 1, 2)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertFalse(result)

    def test_1(self):
        """
        --[ ]|--|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 2)
        item_end = Date(2020, 1, 3)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertFalse(result)

    def test_2(self):
        """
        --[|]--|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 2)
        item_end = Date(2020, 1, 4)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_3(self):
        """
        --|[ ]--|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 3)
        item_end = Date(2020, 1, 4)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_4(self):
        """
        --|-[ ]-|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 4)
        item_end = Date(2020, 1, 5)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_5(self):
        """
        --|--[ ]|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 5)
        item_end = Date(2020, 1, 6)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_6(self):
        """
        --|--[|]--
        """
        ee = self.ee
        item_start = Date(2020, 1, 5)
        item_end = Date(2020, 1, 7)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_7(self):
        """
        --|--|[ ]--
        """
        ee = self.ee
        item_start = Date(2020, 1, 6)
        item_end = Date(2020, 1, 7)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertFalse(result)

    def test_8(self):
        """
        --|--|-[ ]-
        """
        ee = self.ee
        item_start = Date(2020, 1, 7)
        item_end = Date(2020, 1, 8)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertFalse(result)

    def test_9(self):
        """
        --|[ ]|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 3)
        item_end = Date(2020, 1, 6)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_10(self):
        """
        --|[--|-]-
        """
        ee = self.ee
        item_start = Date(2020, 1, 3)
        item_end = Date(2020, 1, 7)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_11(self):
        """
        -[-|--]|--
        """
        ee = self.ee
        item_start = Date(2020, 1, 2)
        item_end = Date(2020, 1, 6)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)

    def test_12(self):
        """
        -[-|--|-]-
        """
        ee = self.ee
        item_start = Date(2020, 1, 2)
        item_end = Date(2020, 1, 7)
        result = ee.check(
            item_start=item_start,
            item_end=item_end,
            time_start=self.time_start,
            time_end=self.time_end
            )
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()