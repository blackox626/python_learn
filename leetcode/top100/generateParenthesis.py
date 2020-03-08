class Solution(object):

    # 思想：动态规划   由n-1 的 情况 推测 n 的情况
    # Dynamic programming dp
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        all = []
        all.append([None])
        all.append(['()'])
        for i in range(2, n + 1):

            lst = []

            for j in range(i):
                list_1 = all[j]
                list_2 = all[i - j - 1]

                for k in list_1:
                    for m in list_2:
                        if k is None: k = ''
                        if m is None: m = ''

                        str = '(' + m + ')' + k

                        lst.append(str)

            all.append(lst)

        return all[n]

    # 精简
    def generateParenthesis2(self, n):

        if n == 0:
            return [None]
        if n == 1:
            return ['()']
        lst = []
        for i in range(n):
            list_1 = self.generateParenthesis2(i)
            list_2 = self.generateParenthesis2(n - i - 1)
            for k in list_1:
                for m in list_2:
                    if k is None: k = ''
                    if m is None: m = ''

                    str = '(' + m + ')' + k

                    lst.append(str)
        return lst

    # 继续精简
    def generateParenthesis3(self, n):
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        lst = []
        for i in range(n):
            for left in self.generateParenthesis2(i):
                for right in self.generateParenthesis2(n - i - 1):
                    lst.append('(' + left + ')' + right)
        return lst

    #  回溯不是那么容易 理解，，似乎有点规律 ：如果是排列组合问题，可以想到回溯
    def generateParenthesis4(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans


print(Solution().generateParenthesis4(3))
