# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def traversal(self, lst, root):
        if root is None:
            return
        self.traversal(lst, root.left)
        lst.append(root.val)
        self.traversal(lst, root.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        _lst = []
        self.traversal(_lst, root)
        return _lst
