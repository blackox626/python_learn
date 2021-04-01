class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        lSub = ''
        sliceSub = ''
        maxCount = 0
        for i in s:
            if i not in sliceSub:
                sliceSub = sliceSub + i
            else:
                maxCount = max(maxCount, len(sliceSub))
                if maxCount == len(sliceSub):
                    lSub = sliceSub
                print(f'str:{sliceSub} len: {len(sliceSub)}')
                index = sliceSub.index(i)
                sliceSub = sliceSub[index + 1:] + i

        maxCount = max(maxCount, len(sliceSub))
        if maxCount == len(sliceSub):
            lSub = sliceSub
        print(f'substr:{sliceSub} len: {len(sliceSub)}')

        print(f'longest substr is {lSub}')

        return maxCount

    def lengthOfLongestSubstring2(self, s: str):
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])
        return max_len


Solution().lengthOfLongestSubstring("anaconda3")
