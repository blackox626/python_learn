class Solution(object):
    # 暴力

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = 0
        for i, l in enumerate(height):
            for j, r in enumerate(height):
                if j <= i: continue
                area = min(l, r) * (j - i)
                maxArea = max(area, maxArea)
        return maxArea

    # 双端移动
    def maxArea2(self, height):
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r += 1

        return area
