class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        bt = []

        def backtrack(nums, btc):
            if len(btc) == len(nums):
                res.append(btc[:])
                return

            for num in nums:

                if num in btc:
                    continue

                btc.append(num)

                backtrack(nums, btc)
                btc.remove(num)

        backtrack(nums, bt)
        return res


print(Solution().permute([1, 2, 3]))
