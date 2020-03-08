class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s

        firstMatch = bool(s and p[0] in [s[0], '.'])

        if len(p) >= 2:

            if p[1] == '*':
                return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
            else:
                return firstMatch and self.isMatch(s[1:], p[1:])

        else:
            return firstMatch and self.isMatch(s[1:], p[1:])


print(Solution().isMatch('ab', '.*c'))
