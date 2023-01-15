class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        totalSteps = 0
        currentStep = 1
        previousStep = 1

        for i in range(n-1):
            totalSteps = currentStep + previousStep
            currentStep = previousStep
            previousStep = totalSteps

        return previousStep


print(Solution().climbStairs(int(input())))
