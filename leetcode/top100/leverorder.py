# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        lst = []

        queue = []
        queue.append(root)
        while len(queue) > 0:

            _lst = []

            for i in range(len(queue)):
                node = queue.pop(0)
                _lst.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            lst.append(_lst)

        return lst
