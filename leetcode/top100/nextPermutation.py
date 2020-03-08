class Solution(object):

    # 中间 有个 冒泡排序  。。。从小到大 排序

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if nums is None or len(nums) == 0:
            return None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:

                for j in range(len(nums) - 1, i - 1, -1):
                    for k in range(len(nums) - 1, i, -1):
                        if nums[k] < nums[k - 1]:
                            nums[k], nums[k - 1] = nums[k - 1], nums[k]

                for t in range(i, len(nums)):
                    if nums[t] > nums[i - 1]:
                        nums[t], nums[i - 1] = nums[i - 1], nums[t]
                        return nums

        return nums.sort()

    # 还可以 优化下 无需冒泡 只需reverse 一下 就好

    def nextPermutation2(self, nums):

        if nums is None or len(nums) == 0:
            return None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                # reverse

                l = i
                r = len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            for t in range(i, len(nums)):
                if nums[t] > nums[i - 1]:
                    nums[t], nums[i - 1] = nums[i - 1], nums[t]
                    return nums

        return nums.sort()


print(Solution().nextPermutation2([5, 4, 7, 5, 3, 2]))
