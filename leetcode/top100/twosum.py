def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lstep, rstep = 0, 0
    for i in nums:
        lstep += 1
        rstep = 0
        for j in nums[::-1]:
            rstep += 1
            if (lstep + rstep) > len(nums):
                break
            if i + j == target:
                return [lstep - 1, len(nums) - rstep]


def twoSum_2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    otherIndex = -1

    for i in nums:

        other = target - i
        if other in nums:
            if other == i and nums.count(i) == 1:
                continue
            else:
                otherIndex = nums.index(other, nums.index(i) + 1)

        if otherIndex > 0:
            return [nums.index(i), otherIndex]


def twoSum_3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map = {}
    for i, n in enumerate(nums):
        other = target - n
        if map.get(other) is not None:
            return [i, map.get(other)][::-1]
        map[n] = i


print(twoSum_3([2, 6, 3, 11], 9))
