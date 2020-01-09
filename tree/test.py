import unittest
import tree
import random


def grow():
    ct = tree.RBTree()
    ct.root = tree.Node(3)
    ct.root.left = tree.Node(1, ct.root)
    ct.root.right = tree.Node(5, ct.root)
    ct.root.left.left = tree.Node(0, ct.root.left)
    ct.root.left.right = tree.Node(2, ct.root.left)
    ct.root.right.left = tree.Node(4, ct.root.right)
    ct.root.right.right = tree.Node(7, ct.root.right)
    ct.root.right.right.left = tree.Node(6, ct.root.right.right)
    ct.root.right.right.right = tree.Node(8, ct.root.right.right)
    ct.root.right.right.right.right = tree.Node(9, ct.root.right.right.right)
    return ct


def only_keys_comparator(t1, t2):
    if t1.key == t2.key:
        return True
    return False


def tree_compare(t1: tree.Node, t2: tree.Node, comparator=only_keys_comparator):
    if t1 == None or t2 == None:
        return t1 == t2
    if not tree_compare(t1.left, t2.left):
        return False
    if not tree_compare(t1.right, t2.right):
        return False
    return comparator(t1, t2)


class TestRBTree(unittest.TestCase):
    def test_creation(self):
        t = tree.RBTree()
        self.assertNotEqual(t, None)

    def test_insert_one(self):
        t = tree.RBTree()
        t.insert(2)
        self.assertEqual(t.root.key, 2)

    def test_find_none(self):
        t = tree.RBTree()
        self.assertFalse(t.find(2))

    def test_find_one(self):
        t = tree.RBTree()
        t.insert(2)
        self.assertTrue(t.find(2))

    def test_find_none_small(self):
        t = tree.RBTree()
        t.insert(2)
        self.assertFalse(t.find(1))

    def test_find_none_big(self):
        t = tree.RBTree()
        t.insert(2)
        self.assertFalse(t.find(3))

    def test_insert_many(self):
        t = tree.RBTree()
        for i in range(10):
            t.insert(i)
        ct = grow()
        self.assertTrue(tree_compare(t.root, ct.root))

    def test_find_many(self):
        t = tree.RBTree()
        for i in range(0, 100, 3):
            t.insert(i)
        for i in range(1, 100, 3):
            t.insert(i)
        for i in range(2, 100, 3):
            t.insert(i)
        for i in range(10):
            self.assertTrue(t.find(i))

    def test_find_many2(self):
        t = tree.RBTree()
        for i in range(10, 0, -1):
            t.insert(i)
        for i in range(1, 11):
            self.assertTrue(t.find(i))

    def test_delete_none(self):
        t = tree.RBTree()
        self.assertFalse(t.delete(2))

    def test_delete_leaf(self):
        t = tree.RBTree()
        for i in range(10):
            t.insert(i)
        self.assertTrue(t.delete(9))
        ct = grow()
        ct.root.right.right.right.right = tree.Node(None, ct.root.right.right.right)
        self.assertTrue(tree_compare(t.root, ct.root))

    def test_delete_root(self):
        t = tree.RBTree()
        t.insert(1)
        self.assertTrue(t.delete(1))
        self.assertEqual(t.root, None)

    def test_delete_not_exist_small(self):
        t = tree.RBTree()
        t.insert(1)
        self.assertFalse(t.delete(-1))

    def test_delete_not_exist_big(self):
        t = tree.RBTree()
        t.insert(1)
        self.assertFalse(t.delete(2))