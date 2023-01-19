class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        def dfs(r):
            if r == [m-1, n-1]:
                return 1

            count = 0
            # Andar para baixo
            if r[0] + 1 < m:
                count += dfs([r[0] + 1, r[1]])
            # Andar para a frente
            if r[1] + 1 < n:
                count += dfs([r[0], r[1] + 1])
            return count

        return dfs([0,0])
        '''
        # Dynamic Programming

        # Bottom row
        row = [1] * n

        # All rows above the bottom one
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]



print(Solution().uniquePaths(3, 7))