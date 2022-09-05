class Solution(object):
    dp = {}

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        if Solution.dp.get(amount, None):
            return Solution.dp[amount]

        res = 9999
        for coin in coins:
            if amount - coin < 0:
                continue

            re = self.coinChange(coins, amount - coin)
            if re != -1:
                res = min(res, re + 1)
                Solution.dp[amount] = res

        if res == 9999:
            return -1
        else:
            return res


print(Solution().coinChange([2], 3))
