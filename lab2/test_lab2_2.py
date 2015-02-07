__author__ = 'Pedram'
from hw2_set import OurSet
import unittest

class TestQueue1(unittest.TestCase):
    def setUp(self):
        self.set1 = OurSet()
        self.set2 = OurSet()
        self.set3 = OurSet()
        self.set1.addList([1,5,6])
        self.set2.addList([6,4,3])
        self.set3.addList([2,4,7])

    def test_union_one_shared(self):
        set3 = self.set1.union(self.set2)
        self.assertEqual(str(set3), "<1, 5, 6, 4, 3>", "Union error shared")

    def test_union_empty_shared(self):
        set3 = self.set1.union(OurSet())
        self.assertEqual(str(set3), "<1, 5, 6>", "test union empty failed")

    def test_intersection_all(self):
        set3 = self.set1.intersection(self.set1)
        self.assertEqual(str(set3), str(self.set1), "test intersection all failed")

    def test_intersection_none(self):
        set3 = self.set1.intersection(self.set3)
        self.assertEqual(str(set3), "<>", "test intersection none failed")



