class Solution(object):
    """
    普通的线性查找 ：正向遍历找第一个，反向遍历找最后一个
    """

    # 还是 二分查找的思想，找到 target 的 index 之后，还要根据 left right 继续找
    def searchRange(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def searchIndex(l, r, lst, target, left):

            if l > r:
                return -1

            mid = (l + r) // 2

            if lst[mid] == target:
                if left:
                    index = searchIndex(l, mid - 1, lst, target, left)
                else:
                    index = searchIndex(mid + 1, r, lst, target, left)

                return mid if index == -1 else index

            elif lst[mid] > target:
                return searchIndex(l, mid - 1, lst, target, left)
            else:
                return searchIndex(mid + 1, r, lst, target, left)

            lindex = searchIndex(0, len(nums) - 1, nums, target, True)
            rindex = searchIndex(0, len(nums) - 1, nums, target, False)

            return [lindex, rindex]
