"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        indexStack = []

        maxLen = 0
        curLen = 0

        for index, i in enumerate(s):
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                    indexStack.pop()
                    curLen = index - (indexStack[-1] if len(indexStack) > 0 else -1)

                    maxLen = max(curLen, maxLen)
                else:
                    indexStack.append(index)
                    stack.append(i)
            else:
                indexStack.append(index)
                stack.append(i)

        return max(curLen, maxLen)


print(Solution().longestValidParentheses("(()))())("))
