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


Solution().lengthOfLongestSubstring("anaconda3")
