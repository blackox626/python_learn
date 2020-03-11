from functools import reduce


class Solution(object):

    # 还是 回溯  。。  回溯 其实也就是 递归，，关键要 判断好 return 条件

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def sum(lst):
            if len(lst) == 0: return 0
            return reduce(lambda x, y: x + y, lst)

        res = []

        def backtrack(lst, candidates, target):
            if sum(lst) == target:
                res.append(lst)
                return
            elif sum(lst) > target:
                return
            else:
                for index, i in enumerate(candidates):
                    _lst = lst[:]
                    _lst.append(i)
                    backtrack(_lst, candidates[index:], target)

        backtrack([], candidates, target)

        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
