# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution2(object):
    res = 0
    depth = 0

    def travasal(self, root):
        if root is None:
            Solution2.res = max(Solution2.depth, Solution2.res)
            return

        Solution2.depth += 1

        self.travasal(root.left)

        self.travasal(root.right)

        Solution2.depth -= 1

    def maxDepth(self, root):
        self.travasal(root)

        return Solution2.res
