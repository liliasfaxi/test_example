import unittest
from library.toolbox.btree import BTree

class TestBTree(unittest.TestCase):

    def setUp(self):
        self.btree = BTree()

    def test_add(self):
        self.assertEqual(self.btree.sum(2, 3), 5)
        self.assertEqual(self.btree.sum(-1, 1), 0)
        print("hello")

    def test_subs(self):
        self.assertEqual(self.btree.subs(3,2),1)