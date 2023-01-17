class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        total = sum(nums)
        for i in range(len(nums)):
            right = total - nums[i] - left
            if left == right:
                return i
            left += nums[i]

        return -1


print(Solution().pivotIndex([1,7,3,6,5,6]))
print(Solution().pivotIndex([1,2,3]))
print(Solution().pivotIndex([2,1,-1]))