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

    """
    对称二叉树
    """

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.compare(root.left, root.right)

    """
    二叉树翻转
    """

    def reverse(self, root):
        if not root:
            return root
        root.right = self.reverse(root.left)
        root.left = self.reverse(root.right)
        return root

    """
    平衡二叉树
    """

    def hight(self, root):
        if not root:
            return 0
        return max(self.hight(root.left), self.hight(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            left_h = self.hight(root.left)
            right_h = self.hight(root.right)

            return abs(left_h - right_h) <= 1

        return False


treeList = [3, 9, 20, None, None, 15, 7]

stack = []

for i in treeList:
    treenode = TreeNode(i)
    stack.append(treenode)

for index, i in enumerate(stack):
    if (index * 2 + 1) < len(stack):
        i.left = stack[index * 2 + 1]
    if (index * 2 + 2) < len(stack):
        i.right = stack[index * 2 + 2]

print(Solution().isBalanced(stack[0]))
