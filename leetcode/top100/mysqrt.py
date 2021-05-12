class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r, ans = 0, x, 0
        while l <= r:
            mid = (l + r) // 2
            if (mid * mid) <= x :
                ans = mid
                l = mid + 1
            else :
                r = mid - 1
        return ans
