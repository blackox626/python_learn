class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        o = []

        for i in s:
            if i in ['(', '[', '{']:
                o.append(i)
            else:
                if len(o) == 0: return False
                if [o[-1], i] in [['(', ')'], ['[', ']'], ['{', '}']]:
                    o = o[0:-1]
                else:
                    return False
        return True if len(o) == 0 else False

    # 居然没有一开始想到用栈的方式。。。。。
    def isValid2(self, s):
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack
