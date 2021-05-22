'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        firstMatch = bool(s and p[0] in [s[0], '.'])

        if len(p) >= 2:

            if p[1] == '*':
                # 匹配0个 | 多个
                return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
            else:
                return firstMatch and self.isMatch(s[1:], p[1:])

        else:
            return firstMatch and self.isMatch(s[1:], p[1:])


print(Solution().isMatch('aab', 'c*a*b'))
