# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def compare(self, left, right):
        if left is not None and right is None:
            return False
        elif right is not None and left is None:
            return False
        elif right is None and left is None:
            return True
        elif left.val != right.val:
            return False
        else:
            return self.compare(left.left, right.right) and self.compare(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.compare(root.left, root.right)



