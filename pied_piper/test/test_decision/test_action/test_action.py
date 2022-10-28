import unittest
from tools import date, dt

from decision.action import Action


class TestActionClass(unittest.TestCase):

    def test_refine_inputs_0(self):
        start_date = date(2000, 1, 1)
        end_date = date(2000, 1, 2)
        a = Action(start_date, end_date, instant=False)
        self.assertFalse(a.instant)
        self.assertEqual(end_date, a.end_date)

    def test_refine_inputs_1(self):
        start_date = date(2000, 1, 1)
        end_date = date(2000, 1, 2)
        a = Action(start_date, end_date)
        self.assertTrue(a.instant)
        self.assertEqual(start_date, a.end_date)

    def test_refine_inputs_2(self):
        """ start_date > end_date """
        start_date = date(2000, 1, 2)
        end_date = date(2000, 1, 1)
        with self.assertRaises(ValueError):
            Action(start_date, end_date, instant=False)
    
    def test_refine_inputs_3(self):
        """ start_date > end_date """
        start_date = date(2000, 1, 2)
        end_date = date(2000, 1, 1)
        a = Action(start_date, end_date)   
        self.assertEqual(a.end_date, start_date) 
    
    def test_refine_inputs_4(self):
        """ empty end_date """
        start_date = date(2000, 1, 1)
        a = Action(start_date)
        self.assertTrue(a.instant)
        self.assertEqual(start_date, a.end_date)

    def test_refine_inputs_5(self):
        """ empty end_date, but not instant! """
        start_date = date(2000, 1, 1)
        with self.assertRaises(ValueError):
            Action(start_date, instant=False)
        
    def test_progress_0(self):
        start_date = date(2000, 1, 1)
        end_date = date(2000, 1, 3)
        a = Action(start_date, end_date, instant=False)
        self.assertEqual(a.progress(a.start_date - dt(days=1)), 0)

    def test_progress_1(self):
        start_date = date(2000, 1, 1)
        end_date = date(2000, 1, 3)
        a = Action(start_date, end_date, instant=False)
        self.assertEqual(a.progress(a.start_date + dt(days=1)), 0.5)

    def test_progress_2(self):
        start_date = date(2000, 1, 1)
        end_date = date(2000, 1, 3)
        a = Action(start_date, end_date, instant=False)
        self.assertEqual(a.progress(a.start_date + dt(days=2)), 1)
        
