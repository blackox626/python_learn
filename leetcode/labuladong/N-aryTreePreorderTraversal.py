"""
n叉树的前序遍历
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# object 是所有类的父类  未显示制定 默认就是object
class Solution:

    def traversal(self, lst, root):

        if root is None:
            return

        lst.append(root.val)

        for node in root.children:
            self.traversal(lst, node)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        _lst = []
        self.traversal(_lst, root)
        return _lst
