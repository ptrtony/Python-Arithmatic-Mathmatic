# 二叉树 （不一定是完全的二叉树）
# 每个节点的键值大于左孩子
# 每个节点的键值小于右孩子
# 以左右孩子为根的子树仍为二叉树
#                   28
#
#          16              30
#
#    13           22   29         42

class Node(object):

    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    root = Node

    def insert(self, key, value):
        self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            node = Node(key, value, None, None)
        if node.key == key:
            node.value = value
        elif node.key > key:
            self._insert(node.left, value)
        elif node.key < key:
            self._insert(node.right, key, value)

    def search(self, key):
        node = self._search(self.root, key)
        return node

    def _search(self, node, key):

        if node is None:
            return None
        if node.key == key:
            return node

        if node.key > key:
            self._search(node.left, key)

        elif node.key < key:
            self._search(node.right, key)

    def contain(self, key):
        return self._contain(self.root, key)

    def _contain(self, node, key):

        if node is None:
            return False

        if node.key == key:
            return True

        if node.key < key:
            self._contain(node.right, key)

        if node.key > key:
            self._contain(node.left, key)

    # def minHeap(self):
