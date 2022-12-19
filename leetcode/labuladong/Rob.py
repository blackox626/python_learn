class Solution(object):

    # 自顶向下
    def rob1(self, nums, start):
        count = len(nums)

        if start >= count:
            return 0

        res = max(nums[start] + self.rob1(nums, start + 2), self.rob1(nums, start + 1))

        return res

    # 自底向上
    def rob(self, nums):
        count = len(nums)
        list = [0] * (count + 2)

        for i in range(count - 1, -1, -1):
            list[i] = max(list[i + 1], list[i + 2] + nums[i])

        return list[0]

        # money = 0
        #
        # list_two[0][0] = 0
        # list_two[0][1] = nums[0]
        #
        # for i in range(1,count):
        #     list_two[i][0] = max(list_two[i - 1][1], list_two[i - 1][0])
        #     list_two[i][1] = list_two[i-1][0] + nums[i]
        #
        #
        # return max(list_two[count-1][0],list_two[count-1][1])


print(Solution().rob([2, 1, 7, 9, 3, 1]))
print(Solution().rob1([2, 1, 7, 9, 3, 1], 0))
