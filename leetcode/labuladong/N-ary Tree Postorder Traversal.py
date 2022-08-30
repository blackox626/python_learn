# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):

    def traversal(self, lst, root):
        if root is None:
            return

        for node in root.children:
            self.traversal(lst, node)

        lst.append(root.val)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        _lst = []
        self.traversal(_lst, root)
        return _lst
