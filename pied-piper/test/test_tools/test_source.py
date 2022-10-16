import unittest

from tools.source import Storage, Deficiency
from tools.source import Use, Produce
from tools import Unit


class TestUseProduceClass(unittest.TestCase):
    def test_refill(self):
        p = Produce(rate=Unit(5, 'ton/day').to_SI())
        p.refill(delta_t=Unit(1, 'day').to_SI())
        self.assertEqual(p.current_amount, Unit(5, 'ton').to('kg').to_SI(), msg="refill")

    def test_sub(self):
        p = Produce(rate=Unit(5, 'ton/day').to_SI())
        p.refill(delta_t=Unit(1, 'day').to_SI())
        p.sub(Unit(10, 'ton').to('kg').to_SI())
        self.assertEqual(p.current_amount, 0, msg="refill")


class TestDeficiencyClass(unittest.TestCase):
    def test_add(self):
        d = Deficiency(
            current_amount=Unit(1, 'kg').to_SI(),
            max_amount=Unit(5, 'kg').to_SI()
        )
        d.add(Unit(1, 'kg').to_SI())
        val = d.current_amount
        self.assertEqual(val, 2, msg='add')

    def test_add_max(self):
        d = Deficiency(
            current_amount=Unit(1, 'kg').to_SI(),
            max_amount=Unit(5, 'kg').to_SI()
        )
        d.add(Unit(5, 'kg').to_SI())
        val = d.current_amount
        self.assertEqual(val, 5, msg='add')

    def test_add_max_alive(self):
        d = Deficiency(
            current_amount=Unit(1, 'kg').to_SI(),
            max_amount=Unit(5, 'kg').to_SI()
        )
        d.add(Unit(5, 'kg').to_SI())
        self.assertFalse(d.is_alive(), msg='not alive')