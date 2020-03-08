def merge(lst, left, mid, right):
    lst_ = []

    p1 = left
    p2 = mid + 1

    while p1 <= mid and p2 <= right:
        if lst[p1] < lst[p2]:
            lst_.append(lst[p1])
            p1 += 1
        else:
            lst_.append(lst[p2])
            p2 += 1

    if p1 <= mid:
        lst_.extend(lst[p1:mid + 1])
    if p2 <= right:
        lst_.extend(lst[p2:right + 1])

    for i, l in enumerate(lst_):
        lst[left + i] = l


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1.extend(nums2)
        merge(nums1, 0, len(nums1) - len(nums2) - 1, len(nums1) - 1)

        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2.0

    def findMedianSortedArrays_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)
        i = 0
        left, right = -1, -1
        p1, p2 = 0, 0
        while i <= (m + n) // 2:
            left = right

            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    right = nums1[p1]
                    p1 += 1
                else:
                    right = nums2[p2]
                    p2 += 1
            elif p1 >= m:
                right = nums2[p2]
                p2 += 1
            else:
                right = nums1[p1]
                p1 += 1

            i += 1
        # 判断奇偶
        if m + n & 1 == 0:
            return (left + right) / 2.0
        else:
            return right


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays_2([1, 2], [3, 4]))
