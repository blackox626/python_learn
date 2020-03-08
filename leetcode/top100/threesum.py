class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        _set = set()

        for i in range(len(nums)):
            if len(nums) < 3: return []
            if nums[i] > 0: continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                _threeSum = nums[i] + nums[l] + nums[r]
                if _threeSum == 0:
                    _set.add(" ".join([str(n) for n in [nums[i], nums[l], nums[r]]]))
                    l += 1
                    r -= 1
                elif _threeSum >= 0:
                    r -= 1
                else:
                    l += 1

        def f(lst):
            for index, n in enumerate(lst):
                lst[index] = int(n)
            return lst

        return [f(k) for k in [x.split(" ") for x in _set]]

    def threeSum2(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res


print(Solution().threeSum2([-1, 0, 1, 2, -1, -4]))
