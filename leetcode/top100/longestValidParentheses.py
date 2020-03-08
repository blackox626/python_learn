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

        topIndex = -1

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
