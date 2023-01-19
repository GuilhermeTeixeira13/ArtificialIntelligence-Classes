class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        max_cap = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                actual_cap = min(height[i], height[j]) * (j-i)
                max_cap = max(max_cap, actual_cap)

        return max_cap
        '''

        max_cap = 0
        l, r = 0, len(height) - 1

        while l < r:
            actual_cap = min(height[l], height[r]) * (r - l)
            max_cap = max(max_cap, actual_cap)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_cap

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))