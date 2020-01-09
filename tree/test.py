import unittest
import test
import random


def makect():
    ct = test.RBTree()
    ct.root = test.Node(3)
    ct.root.left = test.Node(1, ct.root)
    ct.root.right = test.Node(5, ct.root)
    ct.root.left.left = test.Node(0, ct.root.left)
    ct.root.left.right = test.Node(2, ct.root.left)
    ct.root.right.left = test.Node(4, ct.root.right)
    ct.root.right.right = test.Node(7, ct.root.right)
    ct.root.right.right.left = test.Node(6, ct.root.right.right)
    ct.root.right.right.right = test.Node(8, ct.root.right.right)
    ct.root.right.right.right.right = test.Node(9, ct.root.right.right.right)
    return ct


def only_keys_comparator(t1, t2):
    if t1.key == t2.key:
        return True
    return False


def tree_compare(t1: test.Node, t2: test.Node, comparator=only_keys_comparator):
    if t1 == None or t2 == None:
        return t1 == t2
    if not tree_compare(t1.left, t2.left):
        return False
    if not tree_compare(t1.right, t2.right):
        return False
    return comparator(t1, t2)


class TestRBTree(unittest.TestCase):
    def test_creation(self):
        t = test.RBTree()
        self.assertNotEqual(t, None)

    def test_insert_one(self):
        t = test.RBTree()
        t.insert(2)
        self.assertEqual(t.root.key, 2)

    def test_find_none(self):
        t = test.RBTree()
        self.assertFalse(t.find(2))

    def test_find_one(self):
        t = test.RBTree()
        t.insert(2)
        self.assertTrue(t.find(2))

    def test_find_none_small(self):
        t = test.RBTree()
        t.insert(2)
        self.assertFalse(t.find(1))

