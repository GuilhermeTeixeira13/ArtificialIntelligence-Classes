class Solution(object):
    def runningSum(self, nums):
        sum = 0
        res = []

        for count, num in enumerate(nums):
            sum += num
            res.append(sum)

        return res

print(Solution().runningSum([1,2,3,4]))
print(Solution().runningSum([1,1,1,1,1]))
print(Solution().runningSum([3,1,2,10,1]))
