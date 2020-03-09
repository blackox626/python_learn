class Solution(object):

    #  旋转之后，一分为二 总是有一边是 排好序的
    # 判断 target 是否在已经排好序的这一边
    # 剩下的就是 二分查找了
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def searchTarget(l, r, lst, target):
            if r >= l:
                mid = (l + r) // 2

                if lst[mid] == target: return mid

                if lst[l] <= lst[mid]:  # 左边有序
                    if lst[l] <= target < lst[mid]:
                        return searchTarget(l, mid - 1, lst, target)
                    else:
                        return searchTarget(mid + 1, r, lst, target)
                else:  # 右边有序
                    if lst[mid] < target <= lst[r]:
                        return searchTarget(mid + 1, r, lst, target)
                    else:
                        return searchTarget(l, mid - 1, lst, target)
            else:
                return -1

        return searchTarget(0, len(nums) - 1, nums, target)


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         if target not in nums:
#             return -1
#
#         def searchTarget(l, r, lst, target):
#             mid = (l + r) // 2
#
#             if lst[mid] == target: return mid
#
#             if lst[l] < lst[mid]:
#                 if target < lst[l] or target > lst[mid]:
#                     return searchTarget(mid + 1, r, lst, target)
#                 else:
#                     return searchTarget(l, mid, lst, target)
#             else:
#                 if target < lst[mid + 1] or target > lst[r]:
#                     return searchTarget(l, mid, lst, target)
#                 else:
#                     return searchTarget(mid + 1, r, lst, target)
#
#         return searchTarget(0, len(nums) - 1, nums, target)
