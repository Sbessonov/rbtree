class RBTree:
    def __init__(self):
        self.root = None
        pass

    def find(self, key):
        if self.root is None:
            return None
        return self.root.find(key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return True
        res = self.root.insert(key)
        while self.root.parent is not None:
            self.root = self.root.parent
        return res

    def delete(self, key):
        if self.root is None:
            return False
        res = self.root.delete(key)
        while self.root.parent is not None:
            self.root = self.root.parent
        if self.root.key is None:
            self.root = None
        return res


class Node:
    color = 0

    def __init__(self, key=None, parent=None):
        self.parent, self.key = parent, key
        if key is not None:
            self.left, self.right = Node(None, self), Node(None, self)
        else:
            self.left, self.right = None, None
