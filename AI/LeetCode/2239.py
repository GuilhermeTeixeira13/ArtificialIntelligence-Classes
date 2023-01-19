class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        closest = 1000000
        for num in nums:
            if abs(closest) == abs(num):
                closest = max(closest, num)
            elif abs(num) < abs(closest):
                closest = num

        return closest


print(Solution().findClosestNumber([-4,-2,1,4,8]))