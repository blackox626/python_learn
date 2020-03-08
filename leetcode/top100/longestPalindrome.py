class Solution(object):
    """
    暴力
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longestStr = ''

        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subStr = s[i:j]
                if self.isPalindrome(subStr):
                    if len(subStr) > len(longestStr):
                        longestStr = subStr
        return longestStr

    def isPalindrome(self, s):
        return s == s[::-1]

    """
    中心扩展
    """

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s is None or len(s) < 1:
            return ''

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.getPalindromeLen(s, i, i)
            len2 = self.getPalindromeLen(s, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen - 1 > end - start:
                start = i - (maxLen - 1) // 2
                end = start + maxLen - 1
        return s[start: end + 1]

    def getPalindromeLen(self, s, l, r):
        left, right = l, r
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - 1 - left - 1 + 1


print(f'longest : {Solution().longestPalindrome2("bb")}')
